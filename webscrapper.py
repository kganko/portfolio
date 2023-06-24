

import requests
from bs4 import BeautifulSoup
mainContent = requests.get('https://www.lifehack.org/')
print(mainContent.text)

soup = BeautifulSoup(mainContent.text,'lxml')
print(soup)
titleall = soup.find_all('h3', class_='best-of-card').get_text()
print(titleall)

title_list =[]
for item in titleall:
   individualtitle = item.get_text()
   title_list.append(individualtitle)
print(title_list)


print(f"this is the list of the things that you can find in BBC Culture today: {title}")
'''

import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org/page/1/'

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})

print(titles[4].text)
'''