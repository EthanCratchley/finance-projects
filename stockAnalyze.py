import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PLTR.csv")
df['Date'] = pd.to_datetime(df['Date'])

fig, ax1 = plt.subplots() 

ax1.plot(df['Date'], df['Close'], color='b', label='Close Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()  
ax2.bar(df['Date'], df['Volume'], color='g', alpha=0.3, label='Volume')
ax2.set_ylabel('Volume', color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax2.legend(loc='upper right')

fig.autofmt_xdate()

plt.title('PLTR Stock Price and Volume')
plt.show()
