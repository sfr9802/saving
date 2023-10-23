import numpy as np
import pandas as pd

import yfinance as yf

def to_csv(tker : str, per : str, date : str, start_date : str, end_date : str) :
    data = yf.download(tickers = tker, period = per, start=start_date, end = end_date)
    
    df_stock = pd.DataFrame({'High' : data['High'], 
                                'Low' : data['Low'], 
                                'Close' : data['Close'], 
                                'Open' : data['Open'],
                                'Adj Close' : data['Adj Close']},
                                index = data.index)
    
    df_stock.to_csv('Spx_data'+date+'.csv', sep=',', float_format='%.64f')