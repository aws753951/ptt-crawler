import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import pprint


def crawl(date):
    print('crawling', date.strftime('%Y/%m/%d'))
    year = date.year
    month = date.month
    day = date.day
    r = requests.get(f'https://www.taifex.com.tw/cht/3/futContractsDate?queryType=3&goDay=&doQuery=1&dateaddcnt=-1&queryDate={year}%2F{month}%2F{day}&commodityId=')
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
    else:
        print('connect error')

    try:
        table = soup.find('table', class_='table_f')
        trs = table.find_all('tr')
    except AttributeError:
        print('no data for ', date)
        return
    rows = trs[3:-4]

    # c = []
    all_data = {}
    for row in rows:
        ths = row.find_all('th')
        tds = row.find_all('td')
        cells = [td.text.strip() for td in tds]

        if len(ths) == 3:
            product = ths[1].text.strip()
            name = ths[2].text.strip()
        else:
            name = ths[0].text.strip()

        data = [product] + [name] + cells
        converted = [int(d.replace(',', '')) for d in data[2:]]
        data = data[:2] + converted
        # c.append(data)

        # 第二種方式: 字典 ----------
        # product > who > content

        headers = ['商品名稱', '身份別', '交易多方口數', '交易多方契約金額', '交易空方口數', '交易空方契約金額', '交易多空淨額口數', '交易多空淨額金額', '未平倉多方口數', '未平倉多方契約金額', '未平倉空方口數', '未平倉空方契約金額', '未平倉多空淨額口數', '未平倉多空淨額金額']

        product = data[0]
        who = data[1]
        contents = {headers[i]: data[i] for i in range(2, len(headers))}

        if product not in all_data:
            all_data[product] = {who: contents}  # all_data這個字典，當中的key為product，對應的value為另個字典，key為who，value為contents的字典
        else:
            all_data[product][who] = contents

    print(all_data['富櫃200期貨']['投信']['未平倉多空淨額金額'])



        # 第二種方式: 字典 ----------



    # 第一種方式: pandas ----------

    # headers = ['商品名稱', '身份別', '交易多方口數', '交易多方契約金額', '交易空方口數', '交易空方契約金額', '交易多空淨額口數', '交易多空淨額金額', '未平倉多方口數', '未平倉多方契約金額', '未平倉空方口數', '未平倉空方契約金額', '未平倉多空淨額口數', '未平倉多空淨額金額']
    # df = pd.DataFrame(c, columns=headers)
    # print(df.head())
    # df.to_excel(f'future{year}{month}{day}.xlsx', index=False)

    # 第一種方式: pandas ----------




date = datetime.today()
crawl(date)
while True:
    crawl(date)
    date = date - timedelta(days=1)
    if date < datetime.today() - timedelta(days=20): # 365*2 該網站就只能看過去兩年
        break
    
    