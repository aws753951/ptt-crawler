import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.pttweb.cc/hot/all/today')
root_url = 'https://www.pttweb.cc'
soup = BeautifulSoup(r.text, 'html.parser')
spans = soup.find_all('div', class_="e7-right-top-container e7-no-outline-all-descendants")
# spans = soup.select('div.e7-right-top-container.e7-no-outline-all-descendants')


for span in spans:
    href = span.find('a').get('href')
    url = root_url + href
    title = span.find('a').find('span').find('span').text

    print(f'{title}\n{url}')


