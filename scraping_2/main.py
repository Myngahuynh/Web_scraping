import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
wine_list=[]


url='https://wanderlustwine.co.uk/buy-wine-online/'

r=requests.get(url, headers=headers)

soup=BeautifulSoup(r.content, features='lxml')

# #find all class co diem chung : li product + type product
products =soup.find_all('li', class_=["product", "type-product"])

print(products)
# for item in products:
#     try:
#         product= {
#         'name': item.find('h2', class_="woocommerce-loop-product__title").text.strip(),
#         'price': item.find('span', class_="woocommerce-Price-amount amount").text            
#         }
#         wine_list.append(product)
#     except:
#         pass

# df=pd.DataFrame(wine_list)
# df.to_csv('Book1s.csv')

