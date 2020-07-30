import pandas as pd
import requests
from bs4 import BeautifulSoup

site = input("Enter the url of the site that you want to scrape: ")
page = requests.get(site)
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')
specs = soup.select('.specs-detail > li')
price = ['Price']
small = price + [spec.find('small').get_text() for spec in specs] 
bike_price = soup.select('.wpb_wrapper > h2')
cost = bike_price[1].get_text()
para = [cost] + [spec.find('p').get_text() for spec in specs]
#specs = soup.select('.specs-detail')
#for i in specs:
    #print([i.text])
    

bike = pd.DataFrame(
    {'Specs': small,
     'Details': para,
    })

print(bike)
bike.to_csv(name +'.csv')