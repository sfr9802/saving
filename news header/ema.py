import numpy as np
import pandas as pd

def ema(length : int, data, columns : str) :
    data = data
    
    len_index = len(data.index)
    sma_data = data[columns]
    sum = 0 
    for i in sma_data :
        sum = sum + i
        
    sma = sum / len_index

    c_price = data[columns]
    c_price = c_price[1:-1]
    
    k = 2/(length+1)
    ema_f = c_price[0]*k + sma*(1-k)
    ema_f_list = []
    cnt = 0
    for i in c_price :
        if cnt == 0 :
            ema = i*k + ema_f*(1-k)
        else :
            ema = i*k + ema*(1-k)
        cnt = cnt + 1
        ema_f_list.append(ema)
    cnt = 0
    return ema_f_list