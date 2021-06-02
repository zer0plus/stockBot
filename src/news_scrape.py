from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

    def get_news(newsPiece):
        title = newsPiece.find('h4', 's-title').text
        source = newsPiece.find('span', 's-source').text
        date_posted = newsPiece.find('span', 's-time').text.replace('·', '').strip()
        desc = newsPiece.find('p', 's-desc').text.strip()
        url_raw = newsPiece.find('a').get('href')
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


    df = pd.DataFrame(news, columns=["Title", "Source", "Date", "Desc", "URL"])
    vader = SentimentIntensityAnalyzer()
    lmbd = lambda title: vader.polarity_scores(title)['compound']
    df["Sentiment Rating"] = df["Desc"].apply(lmbd)

    print("------------------------------------" + str(ticker) + " News ------------------------------------" + "\n")

    total_compound = 0

    for article in (news[:6]):
        print(str(article[1]) + " - " + str(article[2]) + ": "+ str(article[0]))
        print("--> " + str(article[-1]))
        total_compound += df.loc[df.Title == article[0], "Sentiment Rating"].item()
        if (df.loc[df.Title == article[0], "Sentiment Rating"].item() < 0):
            print("Sentiment Rating: Negative")
        elif (df.loc[df.Title == article[0], "Sentiment Rating"].item() == 0):
            print("Sentiment Rating: Neutral")
        elif (df.loc[df.Title == article[0], "Sentiment Rating"].item() > 0):
            print("Sentiment Rating: Positive")
        print()

    if (total_compound/6 > 0 and total_compound/6 < 0.2):
        print("Overall News: Midly Positive")
    elif (total_compound/6 > 0 and total_compound/6 > 0.2):
        print("Overall News: Very Positive")
    elif (total_compound/6 < 0 and total_compound/6 > -0.2):
        print("Overall News: Very Negative")
    elif (total_compound/6 < 0 and total_compound/6 < -0.2):
        print("Overall News: Midly Negative")
    elif (total_compound/6 == 0):
        print("Overall News: Neutral")