import requests
from bs4 import BeautifulSoup
import pprint



r = requests.get('https://www.dcard.tw/f/job/p/238730024')
soup = BeautifulSoup(r.text, 'html.parser')
dicts = {}
name = ''
words = ''
tags = soup.find_all('div', class_='sc-e11fdd6e-0 dcxkkY')

for tag in tags:
    name = tag.find('div', class_='sc-99e20798-1 eluFgI').text

    words = tag.find('div', class_='sc-ebb1bedf-0 aiaXw').text.split()
    if name in dicts:
        dicts[name].append(words)
    else:
        dicts[name] = [words]

pprint.pprint(dicts)



# pprint.pprint(dicts)

    
    



# tags = [['a','123 4132'], ['b','123'], ['c','111 222'], ['a','999']]
# name = ''
# word = ''
# dicts = {}
# for tag in tags:
#     name = tag[0]
#     word = tag[1]
#     print(name)
#     print(word)
#     if name in dicts:
#         dicts[name].append(word)
#         print(dicts)
#     else:
#         dicts[name] = [word]



# print(dicts)

# prime_numbers = {1}
# prime_numbers.add((2,3))
# print(prime_numbers)

# a = {1: 2, 2: 2}
# b = {1: 1, 3: 3}
# b.update(a)
# b[2] = 88
# b[5] = 55
# # print(b)

# data = {}
# data['a'] = [5]
# print(data)
# print(data['a'])
# data['a'].append(6)
# print(data)

# a = [5]
# a.append(6)
# print(a)