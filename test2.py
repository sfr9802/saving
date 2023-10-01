import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('^VIX.csv')

df_vix_high = df[df["High"] > 25]
df_vix_low = df[df["Low"] < 20]

print(len(df_vix_high))
print(len(df_vix_low))


vix_high_op = df_vix_high["Open"].tolist()
vix_high_cs = df_vix_high["Close"].tolist()
vix_low_op = df_vix_low["Open"].tolist()
vix_low_cs = df_vix_low["Close"].tolist()

open_value = vix_high_op + vix_low_op
close_value = vix_high_cs + vix_low_cs

op_cs_data = [[o, c] for o, c in zip(open_value, close_value)]

vix_lable_data = [0]*209 + [1]*217

x_train, x_test, y_train, y_test = train_test_split(op_cs_data, vix_lable_data, shuffle=True , test_size=0.2 , random_state=5)

kn = KNeighborsClassifier()

kn.fit(x_train,y_train)



test_vix_day_open = 17.30
test_vix_day_close = 16.95

test_vix = kn.predict([[test_vix_day_open, test_vix_day_close]])

plt.scatter(vix_high_op, vix_high_cs)
plt.scatter(vix_low_op, vix_low_cs)
plt.scatter(test_vix_day_open, test_vix_day_close, marker='s')

plt.xlabel('open')
plt.ylabel('close')
print(op_cs_data)
plt.show()
if test_vix == 0 :
    print("high day")
else :
    print("low day")