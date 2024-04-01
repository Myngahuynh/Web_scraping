import requests
from bs4 import BeautifulSoup
import pandas as pd


current_page=1
data=[]

for i in range(100):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    url=f'https://uk.finance.yahoo.com/most-active/?count=25&offset={i}'
    print(f'Getting page: ', i)
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
            data.append(stock)
        except:
            pass


df=pd.DataFrame(data)
df.to_csv('File_export.csv')
print('Fin.')