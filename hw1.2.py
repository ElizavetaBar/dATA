import requests
method = 'groups.get'
user_id = 'user_ids=id618901872'
ACCESS_TOKEN = 'aa5762b8d3cd8942a7f4587715bbdf3a398972a7941e83d48c76171d78bc0d928edba77970818cae9fbd3'
link = f'https://api.vk.com/method/{method}?{user_id}&access_token={ACCESS_TOKEN}&v=5.124'

response = requests.post(link)
print(response.text)