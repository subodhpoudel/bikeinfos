from bs4 import BeautifulSoup
import pandas as pd
import re
import requests



site = input("Enter the url of the site that you want to scrape: ")
page = requests.get(site)
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')

specs = soup.select('h5', {'class':'clearfix services__title'})
title = ['Price'] + [spec.get_text() for spec in specs]

price = soup.select_one('h4[style="color: white;"]').text
infos = soup.select('.services__text')
spec =  [price] + [info.get_text() for info in infos]

bike = pd.DataFrame (
    {'Specs': title,
     'Infos': spec, 
    })
bike.to_csv(name + '.csv')
