# import libs
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://movies.yahoo.com.tw/chart.html'

r = requests.get(url)
if r.status_code == requests.codes.ok:
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='tr')
    colname = list(rows.pop(0).stripped_strings)
    contents = []
    for row in rows:
        thisweek_rank = row.find_next('div', class_='td')
        updown = thisweek_rank.find_next('div')
        lastweek_rank = updown.find_next('div')
        if thisweek_rank.string == str(1):
            movie_title = lastweek_rank.find_next('h2')
        else:
            movie_title = lastweek_rank.find_next(class_='rank_txt')
        released_day = movie_title.find_next('div')
        trailer = released_day.find_next('a')
        star = trailer.find_next('h6')
        c = [thisweek_rank.string, lastweek_rank.string, movie_title.string, released_day.string, trailer.get('href'), star.string]
        contents.append(c)


df = pd.DataFrame(contents, columns=colname)
print(df.head())

