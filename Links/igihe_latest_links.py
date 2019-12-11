import requests
from bs4 import BeautifulSoup


def get_latest_igihe_links(url='http://m.igihe.com/'):
    ''' return a list of the latest articles links on igihe'''

    response =  requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles =  soup.find_all("div", class_='middle-news')
    
    LINKS = []

    with open("igihelinks.txt", 'a+') as f:
        for article in articles:
            link =  article.find('a', href=True)
            if link['href'].startswith('http'):
                LINKS.append(link['href'])
                #f.write(link['href'] + '\n')
            LINKS.append(url+link['href'])
            #f.write('http://m.igihe.com/' + link['href']+ '\n')
    
    return LINKS