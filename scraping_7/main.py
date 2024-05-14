
# Không get API web products whiskey, render google new kh đc, kh hiểu logic về shopify?
from requests_html import HTMLSession

session= HTMLSession()

url='https://news.google.com/home?hl=en-US&gl=US&ceid=US:en'

r=session.get(url)

r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('article')

print(articles)