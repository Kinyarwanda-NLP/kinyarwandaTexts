import os
import requests
from bs4 import BeautifulSoup

def get_igihe_article_content(url, folder_to_write_to):
    '''
    This function get igihe article content and save the content on the txt file
    '''

    response =  requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    try :
        article =  soup.find_all('div', class_="inkuru-title-2")[0]
    except IndexError as e:
        print('Another IndexError: ', e)
        return 
    paragraphs = article.find_all('p')
    filename = url.rsplit('/', 1)[-1] + '.txt'

    with open(os.path.join(folder_to_write_to, filename), 'w+') as f:
        for para in paragraphs:
            f.write(para.getText()+ '\n \n')