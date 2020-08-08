import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

site = input("Enter the url of the site that you want to scrape: ")
page = requests.get(site)
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')

specs = soup.find_all('th')
infos = soup.find_all('td')

spec = [spec.text for spec in specs]
info = [info.text.replace('\n', '') for info in infos]

bike = pd.DataFrame (
    {'Specs': spec, 
     'Infos': info,  
    })
bike.to_csv(name +'.csv')
