import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
stock_list=[]

url=f'https://uk.finance.yahoo.com/most-active/?count=25&offset=1'


r=requests.get(url, headers=headers)

soup=BeautifulSoup(r.content, features='lxml')


# change= soup.find_all('span', class_='C($positiveColor)')
# for i in change:
#     print(i.text)


# change_1 = soup.find('td', {'class':'Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)'}).find_all('span')[1].text
# print(change_1)

# data=[]
# stocks= soup.find_all('tr', class_=["simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv2BgColor)","simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv1BgColor)"])
# for i in stocks:
#     item={}
#     item['change']=i.find('span')[1].text
#     item['change_%']=i.find('span')[2].text

#     data.append(item)

# print(data)


stocks= soup.find_all('tr', class_=["simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv2BgColor)","simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv1BgColor)"])

for item in stocks:
    print(item)
    try:
        # print(soup.find_all('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)")[2])
        # print(item.find('span', class_='C($positiveColor)').text)
        stock= {
        'symbol': item.find('a', class_="Fw(600) C($linkColor)").text,
        'name': item.find('td', class_="Va(m) Ta(start) Px(10px) Fz(s)").text,
        'price': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('fin-streamer')[0].text,
        # 'change': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('fin-streamer')[1].text

# change= soup.find_all('span', class_='C($positiveColor)')
# for i in change:
#     print(i.text)
        'change': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('span', class_='C($positiveColor)')[0].text,

        # 'change_%': soup.find('fin-streamer', class_="Fw(600)").find_all('span')[1].text


        # 'change': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('span', class_='C($positiveColor)')[0].text
        # 'change_%': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('fin-streamer')[2].text
        # 'change' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text,
        # 'change' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text,

        # 'change': item.find_all('span', class_="C($positiveColor)").text[1]
        # 'change_%': item.find('span', class_="C($positiveColor)").text[1]

        # 'change_%':item.find,
        # 'volumne':item.find,
        # 'market_cap':item.find,
        # 'P/E':item.find
        }
        print(stock)
        stock_list.append(stock)
    except:
        print('=========1')
        pass


print(stock_list)


# products =soup.find_all('li', class_=["product", "type-product"])
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