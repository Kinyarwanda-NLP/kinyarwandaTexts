import argparse

from Utils.igihe_latest_links import get_latest_igihe_links

parser =  argparse.ArgumentParser(description="Kinyarwanda texts Scrapper")
parser.add_argument('site', help="Site to scrape. Choose between (igihe, inyarwanda, umuseke, umubyeyi)", choices=['igihe', 'inyarwanda', 'umuseke'])
parser.add_argument('-a', '--articles', help="Number of article to scrape", type=int, default=5)

args = parser.parse_args()



def main():
    
    #Get latest igihe links
    new_igihe_links = get_latest_igihe_links()
    
    new_links = []

    #Write them on file
    with open('DATA/igihelinks.txt', 'r+') as fr:
        links_in_the_file =  fr.readlines()
        
    new_igihe_links =  [ link.strip() for link in new_igihe_links ]
    links_in_the_file = [ link.strip() for link in links_in_the_file]

    for link in new_igihe_links:
        if link not in links_in_the_file:
            new_links.append(link)

    with open('DATA/igihelinks.txt', 'a') as fa:
        for item in new_links:
            fa.write(item+ '\n')

main()