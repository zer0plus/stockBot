import pandas as pd
import pandas_datareader.data as web
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import datetime
import numpy as np

def correlate(ticker1, ticker2):
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime.now()
    plot_cr1 = web.DataReader(ticker1, 'yahoo', start, end)
    plot_cr2 = web.DataReader(ticker2, 'yahoo', start, end)
    comparison = pd.concat([plot_cr1['Close'], plot_cr2['Close']], axis = 1)
    comparison.columns = [ticker1, ticker2]
    scatter_matrix(comparison, figsize=(8, 8), hist_kwds={'bins':50})

