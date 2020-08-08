import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

site = input("Enter the url of the site that you want to scrape: ")
page = requests.get(site)
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')

row = soup.find_all('td', {'width':'222'})
specs = [spec.get_text() for spec in row]
specs.pop()


infos = soup.find_all(lambda tag: tag.name == 'td' and not tag.attrs)
info = [spec.get_text() for spec in infos]
info.pop()


bike = pd.DataFrame (
    {'Specs': specs, 
     'Infos': info,  
    })
bike.to_csv(name +'.csv')
