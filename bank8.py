import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('http://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'lxml')
    tables = soup.find_all('table', attrs={'cellpadding': '2'})
    content = []
    title = ''
    for table in tables:
        details = table.find_all('tr')
        title = list(details.pop(0).stripped_strings)
        for detail in details:
            c = list(detail.stripped_strings)
            content.append(c)


df = pd.DataFrame(content, columns=title)
print(df.head())
# df.to_csv('big888.csv', index=False)



# data = []
# r = requests.get('http://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')

# if r.status_code == requests.codes.ok:
#     r.encoding = 'utf-8'
#     soup = BeautifulSoup(r.text, 'lxml')
#     tables = soup.find_all('table', attrs={'cellpadding': '2'})

#     for table in tables:
#         details = table.find_all('tr')
#         for detail in details:
#             date, value, price = [trs.text for trs in detail.find_all('td')]
#             if date == '日期':
#                 continue

#             data.append([date, value, price])


# df = pd.DataFrame(data, columns=['日期', '買賣超金額', '台指期'])
# df.to_csv('big8.csv', index=False)
# df.to_excel('big8.xlsx', index=False)
# df.to_html('big8.html', index=False)
