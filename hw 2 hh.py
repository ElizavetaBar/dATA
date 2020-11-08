from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

a = input('Введите вакансию, которую хотите найти: ')

# https://hh.ru/search/vacancy?clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=фотограф
main_link = 'https://hh.ru'

params = {'area': '1',
          'st': 'searchVacancy',
          'text': a,
          'fromSearchLine': 'true'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

response = requests.get(main_link + '/search/vacancy', params=params, headers=headers)
soup = bs(response.text, 'html.parser')

vacancies_list = soup.findAll('div', {'class': 'vacancy-serp-item__info'})

print()

vacancies = []
for v in vacancies_list:
    v_data = {}
    v_name = v.find('a')
    v_name = v.getText()


    v_data['name'] = v_name

    vacancies.append(v_data)

pprint(vacancies)





     if html.ok:
        parsed_html = bs(html.text,'html.parser')

        page_block = parsed_html.find('div', {'data-qa': 'pager-block'})
        if not page_block:
            last_page = '1'
        else:
            last_page = int(page_block.find_all('a', {'class': 'HH-Pager-Control'})[-2].getText())

    for page in range(0, last_page):
        params['page'] = page
        html = requests.get(link, params=params, headers=headers)

        if html.ok:
            parsed_html = bs(html.text,'html.parser')

            vacancy_items = parsed_html.find('div', {'data-qa': 'vacancy-serp__results'}) \
                                        .find_all('div', {'class': 'vacancy-serp-item'})

            for item in vacancy_items:
                vacancy_date.append(_parser_item_hh(item))

    return vac_date

def_item_hh(item):

    vac_date = {}

    # название вакансии
    vac_name = item.find('div', {'class': 'resume-search-item__name'}) \
                        .getText() \
                        .replace(u'\xa0', u' ')

    vac_date['vac_name'] = vac_name

    # название компании
    com_name = item.find('div', {'class': 'vacancy-serp-item__meta-info'}) \
                        .find('a') \
                        .getText()

    vac_date['com_name'] = com_name

    # зарплата
    sal = item.find('div', {'class': 'vacancy-serp-item__compensation'})
    if not sal:
        sal_min = None
        sal_max = None
        sal_currency = None
    else:
        sal = sal.getText() \
                        .replace(u'\xa0', u'')

        sal = re.split(r'\s|-', sal)

        if sal[0] == 'до':
            sal_min = None
            sal_max = int(sal[1])
        elif sal[0] == 'от':
            sal_min = int(sal[1])
            sal_max = None
        else:
            sal_min = int(sal[0])
            sal_max = int(sal[1])

        sal_currency = sal[2]

    vac_date['sal_min'] = sal_min
    vac_date['sal_max'] = sal_max
    vac_date['sal_currency'] = sal_currency

    # ссылка
    is_ad = item.find('span', {'class': 'vacancy-serp-item__controls-item vacancy-serp-item__controls-item_last'}) \
                .getText()

    vaca_link = item.find('div', {'class': 'resume-search-item__name'}) \
                        .find('a')['href']

    if is_ad != 'Реклама':
        vacancy_link = vacancy_link.split('?')[0]

    vac_date['vac_link'] = vac_link

    # сайт
    vac_date['site'] = 'hh.ru'

    return vac_date

def parser_vac(vac):

    vac_date = []
    vacancy_date.extend(_parser_hh(vac))

    pd = pd.DataFrame(vacancy_date)

    return pd