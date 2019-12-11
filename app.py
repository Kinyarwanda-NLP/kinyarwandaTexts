import argparse

parser =  argparse.ArgumentParser(description="Kinyarwanda texts Scrapper")
parser.add_argument('site', help="Site to scrape. Choose between (igihe, inyarwanda, umuseke, umubyeyi)", choices=['igihe', 'inyarwanda', 'umuseke'])
parser.add_argument('-a', '--articles', help="Number of article to scrape", type=int, default=5)

args = parser.parse_args()



def main():
    pass