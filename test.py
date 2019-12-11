import requests
from bs4 import BeautifulSoup


response =  requests.get('http://m.igihe.com/')
soup = BeautifulSoup(response.text, 'html.parser')
articles =  soup.find_all("div", class_='middle-news')

with open("igihelinks.txt", 'a+') as f:
    for article in articles:
        link =  article.find('a', href=True)
        if link['href'].startswith('http'):
            f.write(link['href'] + '\n')
        f.write('http://m.igihe.com/' + link['href']+ '\n')