import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

mystocks=['BOIL.L', 'DGI.L', 'CLON.L', 'AMGO.L', 'IAG.L']

stockdata=[]

def getData(symbol):

    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

    url=f"https://uk.finance.yahoo.com/quote/{symbol}"

    r=requests.get(url, headers=headers)

    soup= BeautifulSoup(r.text, 'html.parser')

    stock ={
    'symbol': symbol,
    'price' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text,
    'change' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text,
    'change_' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ', item)

# price = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
# change=soup.find_all('fin-streamer', {'class':'Fw(500) Pstart(8px) Fz(24px)'})
# change_ = []
# for i in change:
#     i.text,
#     change_.append(i.text)
# print(price, change_)


# headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
# url="https://uk.finance.yahoo.com/quote/CLON.L"

# r=requests.get(url, headers=headers)

# soup= BeautifulSoup(r.text, 'html.parser')

# stock ={
#     'price' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text,
#     'change' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text,
#     'change_' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
#     }

# print(stock)


# with open('stockdata.json', 'w') as f:
#     json.dump(stockdata, f)
# print('Fin.')
    
df=pd.DataFrame(stockdata)
df.to_csv('stock_data.csv')