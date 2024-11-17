import requests
from bs4 import BeautifulSoup
import random
import time
# https://www.google.com/search?q=potato+potato

urls = []
tmr = time.time()
def hopper(url):
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headers = soup.find_all('h1')
        try:
            print(headers[0].get_text())
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

        urls.append(next)
        try:
            hopper(next)
        except:
            stats()
            hopper(random.choice(urls))

def stats():
    print(f'Number of links: {len(urls)}')
    print(f'Total time: {int(time.time() - tmr)} seconds')


hopper('https://www.vg.no/nyheter/i/gwrP0J/fikk-ulvesjokk-hvordan-har-den-kommet-seg-dit')