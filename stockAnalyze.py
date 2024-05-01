import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def moving_avg(input, window_size):
    result = [np.nan] * (window_size - 1) 
    moving_sum = sum(input[:window_size])
    result.append(moving_sum / window_size)
    for i in range(len(input) - window_size):
        moving_sum += (input[i + window_size] - input[i])
        result.append(moving_sum / window_size)
    return result

df = pd.read_csv("PLTR.csv")
df['Date'] = pd.to_datetime(df['Date'])

sma = moving_avg(df['Close'], 20)

fig, ax1 = plt.subplots()
ax1.plot(df['Date'], df['Close'], color='b', label='Close Price')
ax1.plot(df['Date'], sma, color='r', alpha=0.5, label='20-Day SMA') 
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price and SMA', color='b')
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
