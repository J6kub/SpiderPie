import requests
from bs4 import BeautifulSoup

# Define the URL you want to crawl

def getLinks(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the response with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the title tags
        a_tags = soup.find_all('a',itemprop='url')
        links = [a.get('href') for a in a_tags if a.get('href')]
        # Print out the titles
        return links
    else:
        return false

def getTitles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h1')
        for title in titles:
            print(title.get_text())
            print(url)
linkies = getLinks('https://vg.no')
for link in linkies:
    getTitles(link)

