import requests
import json
import pandas as pd

url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2024014?includeBenchmarks=false"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'if-none-match': 'W/"e2409ce1664b23f3668d156308a568e7"',
  'origin': 'https://www.afl.com.au',
  'referer': 'https://www.afl.com.au/',
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
  'x-media-mis-token': 'a8b86ad5e200218fc42d9f5fc07572b9',
  'Cookie': 'ak_bmsc=1D1CF5B1E3A1BA679DDB97A3C462F5A9~000000000000000000000000000000~YAAQzfbVF6fup5uOAQAAQP9BnBcq0FKHxdSK4yxAuGNtAfYgFbdQYupteHY4Ct1W7lEq08DQHDo29XDk+lD6lZyQIlr/UX/bs3zHsXVU35Tgfh5XmIJr+HBhV7jt3p0/0032aytPZuTac1p0QTRQS60bwEOtPXKkdRsUmuzFHtFvTWem+zxyubgdIwL9YQ5S+WVRtpR4vdpeS91yBL2TR9c9ufP+Og0K2n6dH6R7RZNhYcLlefNkQsBIPnsxERD4mgeuV405SsxvOvrD74xXPMuFmpckYs6B7eBp/WHNiJtj5eFKa7OkIR5EgVdY2Lr433PxcARPb8VOrr9TsalFe0nwijgmikALSbdjA6Xdyn5Rfa+k5yqlAkA+gg==; bm_sv=70B89A0960B0E9FEBC43CBBE638E5CBA~YAAQCw80F1WrWpeOAQAAFeCjnBc8w+6iqi+lyerSQcQ4v1+xnV+mpkb6OZ9NyDi3wYCImADg72QS0t0o5TMoKrmkC2qAC/838t5/tzX7a4eb9BgXZMdaknud9KXZLKUHL+3YdvspSuOAW79RmsnX7RMqRi9xFwwZ0HBTkMg5+Y2WTRvPF8YtUFJ7L11AxgeAokTpyyPo1rn0CRH4NOvP5h0gpwsJwfNGIoE+RhIDSMalvCAXg1n/TuXJLbsEzFZ1~1'
}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

r= requests.get(url, headers=headers)

player_data=r.json()


# print(player_data.keys())
# print(player_data['players'][0])


df=pd.json_normalize(player_data['players'])
df.to_csv('Playerdata.csv', index=False)