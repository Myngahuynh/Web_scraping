import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook


current_page=1
data =[]

proceed = True

while(proceed):
    print('Current page is: '+str(current_page))
    url ="https://books.toscrape.com/catalogue/category/books_1/page-"+str(current_page)+".html"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    if soup.title.text == "404 Not Found":
        proceed= False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item= {}

            #attrs : attribute

            item['Title']= book.find('img').attrs['alt']

            item['Link']= book.find("a").attrs['href']

            # text : chỉ lấy value
            item['Price']=book.find('p', class_='price_color').text[2:]

            # strip : loại bỏ khoảng trống
            item['Inventory']=book.find('p', class_='instock availability').text.strip()


            data.append(item)

    
    current_page +=1

df=pd.DataFrame(data)
df.to_excel("books.xlsx")
df.to_csv("books.csv")








 