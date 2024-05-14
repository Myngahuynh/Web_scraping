from requests_html import HTMLSession

url='https://www.beerwulf.com/en-gb/c?q=beer&type=0'

s=HTMLSession()

r=s.get(url)

r.html.render(sleep=1)

print(r.status_code)
