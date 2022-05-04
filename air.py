import requests
from bs4 import BeautifulSoup
import pprint
import re

r = requests.get('https://airtw.epa.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2022050409.json?t=1651631749493')
if r.status_code == requests.codes.ok:
    data = r.json()

    for d in data:
        try:
            site_name = re.search(r'(.+)\(AQI=(\d+)\)', d['Name']).group(1)  # r代表裡的面\為斜線 如果沒配則會被組裝，所以前面要加r 或者雙斜線
            result = re.search(r'(.+)\(AQI=(\d+)\)', d['Name']).group(2)
            print(site_name, result)
        except AttributeError:
            continue

        # if 'AQI' not in d['Name']:
        #     continue
        # site_name = re.search(r'(.+)\(AQI=(\d+)\)', d['Name']).group(1)  # r代表裡的面\為斜線 如果沒配則會被組裝，所以前面要加r 或者雙斜線
        # result = re.search(r'(.+)\(AQI=(\d+)\)', d['Name']).group(2)
        # print(site_name, result)


    # name = [d for d in data if '永和' in d['Name']][0]['Name'] # 只拿單一的，要拿全部用for loop
    # site_name = re.search(r'(.+)\(AQI=(\d+)\)', name).group(1)  # r代表裡的面\為斜線 如果沒配則會被組裝，所以前面要加r 或者雙斜線
    # result = re.search(r'(.+)\(AQI=(\d+)\)', name).group(2)

