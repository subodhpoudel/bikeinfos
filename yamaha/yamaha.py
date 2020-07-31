import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

site = input("Enter the url of the site that you want to scrape: ")
page = requests.get(site)
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')


specs = soup.select('tr > th')
details = soup.select('tr > td')

small = [spec.get_text() for spec in specs] 
small = ['Price'] + small    
price = soup.find(class_='woocommerce-Price-amount amount').get_text()    
para = [price] + [spec.get_text().replace('\t',' ').strip() for spec in details]


    

bike = pd.DataFrame(
    {'Specs': small,
     'Details': para,
    })

print(bike)
bike.to_csv(name +'.csv')