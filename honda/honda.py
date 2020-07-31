import pandas as pd
import requests
from bs4 import BeautifulSoup

site = input("Enter the url of the site that you want to scrape: ")
page = requests.get(site, verify=False)
name = input("Enter the bike: ")
soup = BeautifulSoup(page.content, 'html.parser')
#specs = soup.find_all(class_='tech-specs collapse-ul')
specs = soup.select('li > small')
details = soup.select('li > p')
small = [spec.get_text() for spec in specs] 
x = 0
while x < 3:
    rem = small.pop(0)
    x = x + 1
small = ['Price'] + small    
price = soup.find(id='model-price').get_text()    
para = [price] + [spec.get_text() for spec in details]
x = len(para)
rem = para.pop(x-1)
#specs = soup.select('.specs-detail')
#for i in specs:
    #print([i.text])
    

bike = pd.DataFrame(
    {'Specs': small,
     'Details': para,
    })

print(bike)
bike.to_csv(name +'.csv')