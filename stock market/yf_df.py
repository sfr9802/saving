import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots

def yf_to_df(tker : str, per : str, start_date : str, end_date : str) :
    data = yf.download(tickers = tker, interval = per, start=start_date, end = end_date)
    df_stock = pd.DataFrame({'High' : data['High'], 
                                'Low' : data['Low'], 
                                'Close' : data['Close'], 
                                'Open' : data['Open'],
                                'Adj Close' : data['Adj Close']},
                                index = data.index)
    return df_stock