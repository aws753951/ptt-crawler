import requests
from bs4 import BeautifulSoup

r = requests.get('https://tw.stock.yahoo.com/quote/2498.TW')
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    close_price = soup.find_all(class_='C(#232a31) Fz(16px)--mobile Fz(14px)')[0].find_next_siblings('span')[0]
    open_price = soup.find_all(class_='C(#232a31) Fz(16px)--mobile Fz(14px)')[0].find_next(class_='C(#232a31) Fz(16px)--mobile Fz(14px)').find_next_siblings('span')[0]
    last_price = soup.find_all(class_='C(#232a31) Fz(16px)--mobile Fz(14px)')[6].find_next_siblings('span')[0]


    print(f'收盤價: {close_price.text} 開盤價: {open_price.text} 前日收盤價{last_price.text}')


