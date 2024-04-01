import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
stock_list=[]


def step_one(x):
    url=f'https://uk.finance.yahoo.com/most-active/?count=25&offset={x}'

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
