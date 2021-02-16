from bs4 import BeautifulSoup
import requests
import json
import time

# Return a Array of equity data after taking in an array of tickers
# create different lists of stock watchlist and analyze them differently according to sector
class just_scrape():
    def __init__(self, givenList):
        self.watchlist = givenList
    
    def scrape_data(self):
        datalist = []
        for ticker in self.watchlist:
            url = f'https://finance.yahoo.com/quote/{ticker}'
            print('Scraping: ', ticker)
            r = requests.get(url)
            data = BeautifulSoup(r.text, 'html.parser')
            equity = {}
            equity = {
            '$ticker' : ticker,
            'price' : data.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
            'change' : data.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
            '52 Week-range' : data.find('table', {'class': 'W(100%)'}).find_all('td')[11].text,
            'Alerts' : ''
            }
            datalist.append(equity)
        return datalist