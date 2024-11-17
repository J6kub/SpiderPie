import requests
from bs4 import BeautifulSoup
import random
import time
from CSVtoTable import *

if True:
    running = True
    i = 0
    pth = 'results/vg_hopper/'
    while running:
        try:
            tbl = CreateCsvTable(pth + str(i),["header","link","description"])
            running = False
            break
        except:
            i += 1

urls = []
tmr = time.time()
def hopper(url):
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headers = soup.find_all('h1')
        header = "none"
        try:
            print(headers[0].get_text())
            header = headers[0].get_text()
            txt = headers[0].find_next('p').get_text()
        except:
            print('no header')
        bottom = soup.find('aside')
        articles = bottom.find_all('article')
        articles.pop(0)

        for article in articles:
            next = article.find('a').get('href')
            if next not in urls:
                break
        if next in urls:
            raise Exception('no more articles')

        #append
        row = tbl.createRow(f'{header};{url};{txt}')
        if row not in tbl.rows:
            tbl.rows.append(row)

        urls.append(next)
        try:
            hopper(next)
        except:
            stats()
            hopper(random.choice(urls))

def stats():
    print(f'Number of links: {len(urls)}')
    print(f'Total time: {int(time.time() - tmr)} seconds')
    tbl.save()



hopper('https://www.vg.no/nyheter/i/gwrP0J/fikk-ulvesjokk-hvordan-har-den-kommet-seg-dit')