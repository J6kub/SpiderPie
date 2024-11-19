import requests
from bs4 import BeautifulSoup

def getPrice(crypt):
    url = f'https://www.binance.com/en/price/{crypt}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('div', class_='css-1bwgsh3')
        price = price.get_text();
        return price

while True:
    try:
        pc = getPrice(input('What coin do you want? '))

    except:
        print("Crypto not found")
    if pc == None:
        print("Crypto not found")
    else:
        print(pc)