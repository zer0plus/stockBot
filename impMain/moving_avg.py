import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import numpy as np

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime.now()

def move_avg(ticker):
    plot_avg = web.DataReader(ticker, 'yahoo', start, end)
    plot_avg['MA50'] = plot_avg['Close'].rolling(50).mean()
    plot_avg['Close'].plot(figsize=(15,7))
    plot_avg['MA50'].plot(label = 'MA50')
    plot_avg['MA200'] = plot_avg['Close'].rolling(200).mean()
    plot_avg['MA200'].plot(label = 'MA200')
    plt.title(ticker)
    plt.legend()
    plt.show()

# move_avg("TSLA")