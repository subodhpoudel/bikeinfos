import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


#site = input("Enter the url of the site that you want to scrape: ")
page = requests.get('https://nepal.globalbajaj.com/en/brands/dominar/dominar-d400')
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')
 


specs = soup.find_all('div', {'class':'col-md-6 specification'})
info =  [[item.text.replace('\t', '').replace('\n', '').replace('\r', '') for item in spec.find_all('li')] for spec in specs]
  
print(info)


bike = pd.DataFrame (
    {'Specs': info   
    })
bike.to_csv(name +'.csv')
