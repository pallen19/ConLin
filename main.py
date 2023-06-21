import requests 
from bs4 import BeautifulSoup 
url = 'https://www.publix.com/search?searchTerm=meat%20&srt=products'

data = requests.get(url)

s= BeautifulSoup(data.content, "html.parser")

results = s.find(id='body-wrapper')

item_title = results.find_all('a')
# item_price = results.find_all('span', class_='p-text paragraph-md strong context--default color--null')

# print(results)

# print(data.content)
#print(item_title[0].text)


for item in item_title:
    print(item.text)

# for item2 in item_price:
#     print(item2.text)
   
