import requests
from bs4 import BeautifulSoup

def get_igihe_article_content(url):
    '''
    This function get igihe article content and save the content on the txt file
    '''

    response =  requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    article =  soup.find_all('div', class_="inkuru-title-2")[0]
    paragraphs = article.find_all('p')
    filename = url.rsplit('/', 1)[-1]

    with open(filename + '.txt', 'w+') as f:
        for para in paragraphs:
            f.write(para.getText()+ '\n \n')