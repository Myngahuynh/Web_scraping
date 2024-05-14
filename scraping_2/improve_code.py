import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
wine_list=[]

hung
def step_one(x):
    url=f'https://wanderlustwine.co.uk/buy-wine-online/page/{x}/'

    r=requests.get(url, headers=headers)

    soup=BeautifulSoup(r.content, features='lxml')
    return soup

#find all class co diem chung : li product + type product

def parse_html(soup):
    products =soup.find_all('li', class_=["product", "type-product"])


    for item in products:
        
        try:
            product= {
            'link': item.find("a").attrs['href'],
            'name': item.find('h2', class_="woocommerce-loop-product__title").text.strip(),
            'price': item.find('span', class_="woocommerce-Price-amount amount").text          
            }
            wine_list.append(product)
        except:
            pass

def out_put():
    df=pd.DataFrame(wine_list)
    df.to_csv('Book2')



for x in range(1, 3):
    print(f'Getting page {x}')
    a=step_one(x)
    print('Parsing ...')
    parse_html(a)

out_put()
print('Saved to csv')