from bs4 import BeautifulSoup
import requests
import json
import time
import re

def scrape_news(ticker):
    url = f'https://news.search.yahoo.com/search?p={ticker}'
    print("Fetching news for " + str(ticker) + "\n")

    news = []
    links = set()
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.google.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44'
    }
    r = requests.get(url, headers=headers)
    data = BeautifulSoup(r.text, 'html.parser')
    articles = data.find_all('div', 'NewsArticle')
    card = articles[0]

    def get_news(newsPiece):
        title = newsPiece.find('h4', 's-title').text
        source = newstitle = newsPiece.find('span', 's-source').text
        date_posted = newstitle = newsPiece.find('span', 's-time').text.replace('·', '').strip()
        desc = newstitle = newsPiece.find('p', 's-desc').text.strip()
        url_raw = newstitle = newsPiece.find('a').get('href')
        url_raw_u = requests.utils.unquote(url_raw)
        reg = re.compile(r'RU=(.+)\/RK')
        url_final = re.search(reg, url_raw_u).group(1)

        return (title, source, date_posted, desc, url_final)
    

    for article in articles:
        art1 = get_news(article)
        link = art1[-1]
        if not link in links:
            links.add(link)
            news.append(art1)

    print("------------------------------------" + str(ticker) + " News ------------------------------------" + "\n")
    for article in news[:5]:
        print(str(article[1]) + " - " + str(article[2]) + ": "+ str(article[0]))
        print("--> " + str(article[-1]))
        print()
