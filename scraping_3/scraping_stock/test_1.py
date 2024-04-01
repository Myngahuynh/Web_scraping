import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
stock_list=[]

url=f'https://uk.finance.yahoo.com/most-active/?count=25&offset=1'
r=requests.get(url, headers=headers)
soup=BeautifulSoup(r.content, features='lxml')

stocks= soup.find_all('tr', class_=["simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv2BgColor)","simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv1BgColor)"])


for item in stocks:
    try:
        stock= {
        'symbol': item.find('a', class_="Fw(600) C($linkColor)").text,
        'name': item.find('td', class_="Va(m) Ta(start) Px(10px) Fz(s)").text,
        'price': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('fin-streamer')[0].text,
        'change': item.find('fin-streamer', class_='Fw(600)').text,
        'volumne':item.find('td', class_='Va(m) Ta(end) Pstart(20px) Fz(s)').text
        }
        stock_list.append(stock)
    except:
        pass

print(stock_list)



# df=pd.DataFrame(wine_list)
# df.to_csv('Book1s.csv')

# change= soup.find_all('span', class_='C($positiveColor)')
# for i in change:
#     print(i.text)
        # 'change_%': soup.find('fin-streamer', class_="Fw(600)").find_all('span')[1].text
        # 'change': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('span', class_='C($positiveColor)')[0].text
        # 'change_%': soup.find('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)").find_all('fin-streamer')[2].text
        # 'change' : soup.find('div', {'class':"D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text,
        # 'change': item.find_all('span', class_="C($positiveColor)").text[1]
        # 'change_%': item.find('span', class_="C($positiveColor)").text[1]

        # 'market_cap':item.find('td', class_='Va(m) Ta(end) Pstart(20px) Fz(s)').text,
        # 'market_cap':item.find, : giống trường hợp ở trên
        # 'P/E':item.find: giống ở trên