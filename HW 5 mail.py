from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from pymongo import MongoClient
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains

client = MongoClient('127.0.0.1', 27017)
db_mongo2 = client['mail']
mails = db_mongo2.mails

chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

driver.get('https://mail.ru/')
login = driver.find_element_by_id('mailbox:login-input')
login.send_keys('study.ai_172@mail.ru')
time.sleep(5)
login.send_keys(Keys.ENTER)
time.sleep(5)
passw = driver.find_element_by_id('mailbox:password-input')
passw.send_keys('NextPassword172')
time.sleep(5)
passw.send_keys(Keys.ENTER)
time.sleep(5)
letter = driver.find_element_by_xpath("//a[contains(@class, 'llc js-tooltip-direction_letter-bottom')]")
mess = driver.get(letter.get_attribute('href'))
time.sleep(5)
# от кого, дата отправки, тема письма, текст письма полный
date = driver.find_element_by_class_name('letter__date').text
sent_by = driver.find_element_by_class_name('letter-contact').text
theme = driver.find_element_by_class_name('thread__subject').text
text = driver.find_element_by_class_name('letter__body').text
print(date, sent_by, theme, text)
# result = []
# button2__wrapper
pages = 0
while True:
    try:

        # button = driver.find_element_by_class_name('special-offers__more-btn')


        date = driver.find_element_by_class_name('letter__date').text
        sent_by = driver.find_element_by_class_name('letter-contact').text
        theme = driver.find_element_by_class_name('thread__subject').text
        text = driver.find_element_by_class_name('letter__body').text
        #print(date, sent_by, theme, text)
        mails.insert_one({'Date': date,
                              'Sender': sent_by,
                              'theme': theme,
                              'text': text,
                              })
        pages += 1
        driver.find_element_by_css_selector('body').send_keys(Keys.CONTROL + Keys.DOWN)
        time.sleep(3)


    except Exception as e:
        print(e)
        print(f'Раскрыто {pages} страниц')
        break

