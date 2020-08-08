import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

site = input("Enter the url of the site that you want to scrape: ")
page = requests.get(site)
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')

key = soup.find_all(class_='key')
value = soup.find_all(class_='value')

specs = [spec.get_text() for spec in key]
infos = [spec.get_text() for spec in value]

bikes = pd.DataFrame (
    {'Specs': specs,
     'Infos': infos
    }
)

bikes.to_csv(name + '.csv')
