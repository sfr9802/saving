import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

df = pd.read_csv('^IXIC.csv')
df_close = df["Close"]
df_close_list = df_close.tolist()

df_close_target = []
n = 0
for i in df_close_list :
    
    if i <= df_close_list[n-1] :
        df_close_target.append(0)
    else :
        df_close_target.append(1)
    n = n+1

df['Target'] = df_close_target


df_ixic_train = df

print(df_ixic_train)

df_ixic_train.to_csv('^IXIC - 복사본.csv', sep=',', float_format='%.64f', columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Target'], index = False)
