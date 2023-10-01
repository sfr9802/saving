import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

local = 'C:/Users/TT/Desktop/CNMSshvol20211227.txt'

df = pd.read_csv(local, sep='|')
df.head()

print(df[df["Symbol"] == "AAPL"]) 
# Symbol로 구성된 DataFrame 에서 
# 컬럼값이 AAPL인 녀석으로 다시 DataFrame 구성 


df_row_v = df.loc[:,['Symbol', 'TotalVolume', 'Market']]

aapl = (df_row_v.Symbol == 'AAPL')
ms = (df_row_v.Symbol == 'MS')
tsla = (df_row_v.Symbol == 'TSLA')

df_join = pd.concat([df_row_v[aapl], df_row_v[ms], df_row_v[tsla]], axis=0)

print(df_join)

sns.barplot(data=df_join, x="Symbol", y="TotalVolume")
sns.set(rc = {'figure.figsize':(60,40)})

plt.rc('xtick', labelsize = 20)
plt.rc('ytick', labelsize = 20)

plt.show()
