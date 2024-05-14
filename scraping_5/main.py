import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.accommodationforstudents.com/search-results?location=London&beds=0&occupancy=min&propertyTypes=halls&propertyTypes=house&propertyTypes=flat&propertyTypes=studio&minPrice=0&maxPrice=500&latitude=51.509865&longitude=-0.118092&geo=false&page=1'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
1111111111111

script = soup.find('script', id='__NEXT_DATA__').text.strip()
data =json.loads(script)

# print(data['props']['pageProps']['locations'])
print(data['props']['pageProps']['locations'][0])



