import requests 
from bs4 import BeautifulSoup 
url = 'https://www.publix.com/'

data = requests.get(url)

s= BeautifulSoup(data.content, "html.parser")

results = s.find(id='body-wrapper')

item_title = results.find_all('a', class_='p-text paragraph-md normal context--default color--null line-clamp title')
#item_price = results.find_all('span', class_='cfpn1d')

print(data.content)