from matplotlib import pylab as plt
import pandas as pd

df1 = pd.read_csv('C:\\Users\\User\\Downloads\\JNJ.csv')
df2 = pd.read_csv('C:\\Users\\User\\Downloads\\PFEa.csv')
print(df1)
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)
df2['Date'] = pd.to_datetime(df2.Date)


plt.figure("JNJ Stock")
plt.plot("Date", "Close", 'r-', linewidth=0.6, label="JNJ Stock price, mean=", data=df1)
plt.plot("Date", "Close", 'r-', linewidth=0.6, color= 'blue',label="Pfizer Stock price, mean=", data=df2)
plt.title('StockPrices Over Time')
plt.ylabel('StockPrice')
plt.xlabel("Dates")
plt.show()

