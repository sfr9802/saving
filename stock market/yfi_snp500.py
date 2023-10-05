import numpy as np
import pandas as pd

import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots

def yfi_snp500_chart(start_date : str, end_date : str) :
    snp_data = yf.download(tickers='^GSPC', period = '4h', start=start_date, end = end_date)

    fig = go.Figure()
    fig2 = go.Figure()

    #Candlestick

    fig.add_trace(go.Candlestick(x=snp_data.index,
                            open=snp_data['Open'],
                            high=snp_data['High'],
                            low=snp_data['Low'],
                            close=snp_data['Close'],
                            name = 'market data'))
    fig.update_layout(
        title='S&P500 live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')
    
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="minute", stepmode="backward"),
                dict(count=3, label="3m", step="minute", stepmode="backward"),
                dict(count=5, label="5m", step="minute", stepmode="backward"),
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    
    fig.show()

def to_csv(tker : str, per : str, date : str, start_date : str, end_date : str) :
    data = yf.download(tickers = tker, interval = per, start=start_date, end = end_date)
    
    df_stock = pd.DataFrame({'High' : data['High'], 
                                'Low' : data['Low'], 
                                'Close' : data['Close'], 
                                'Open' : data['Open'],
                                'Adj Close' : data['Adj Close']},
                                index = data.index)
    
    df_stock.to_csv('SPY data'+date+'.csv', sep=',', float_format='%.64f')

def yfi_to_df(tker : str, per : str, date : str, start_date : str, end_date : str) :
    data = yf.download(tickers = tker, interval = per, start=start_date, end = end_date)
    df_stock = pd.DataFrame({'High' : data['High'], 
                                'Low' : data['Low'], 
                                'Close' : data['Close'], 
                                'Open' : data['Open'],
                                'Adj Close' : data['Adj Close']},
                                index = data.index)
    return df_stock