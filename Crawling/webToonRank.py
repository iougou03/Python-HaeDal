import requests
import datetime
import csv
from bs4 import BeautifulSoup

req = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
html = req.text

soup = BeautifulSoup(html,'html.parser')

datas = soup.select(
    '.col .col_inner'
)

ranking = {}
for data in datas:
    date = data.h4['class'][0]
    if date not in ranking:
        ranking[date] = []
    for toon in data.ul.findChildren("li",recursive=False):
        ranking[date].append(toon.a.img['title'])

topN = 5
for k,v in ranking.items():
    print("date :",k)
    for i in range(1,topN+1):
        print(i,"등",v[i-1])

with open('rank_webToon.csv','w',newline='') as c:
    cp = csv.writer(c)
    for k, v in ranking.items():
        n=0
        cp.writerow(['요일','순위','제목'])
        for vv in v:
           n+=1 
           cp.writerow([k,n,vv])
    
    