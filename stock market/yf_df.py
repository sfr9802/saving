import pandas as pd
import yfinance as yf
import csv
def to_csv(tker : str, per : str, start_date : str, end_date : str) :

    data = yf.download(tickers = tker, interval = per, start=start_date, end = end_date)
    df_stock = pd.DataFrame({'High' : data['High'], 
                                'Low' : data['Low'], 
                                'Close' : data['Close'], 
                                'Open' : data['Open'],
                                'Adj Close' : data['Adj Close']},
                                index = data.index)
    df_stock.to_csv(''+tker+'_'+start_date+'.csv', sep=',', float_format='%.64f')
    return df_stock