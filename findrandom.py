# let's do some random things in the Internet and get smart!

#random Wikipedia page
import webbrowser
url = "https://en.wikipedia.org/wiki/Special:Random"
webbrowser.open(url)


# random youtube video
import string
import random
letters = (list(string.ascii_letters))
letters.extend([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
link = "https://youtu.be/"


for i in range(11):
    randomletter = random.choice(str(letters))
    link = link + randomletter

webbrowser.open(link)



import requests
from bs4 import BeautifulSoup


url = 'https://www.bbc.com/news'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
   # print(link.get('href'))
    if ("https") in link.get('href') == True:
        urls.append(link.get('href'))


print(urls)