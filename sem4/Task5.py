import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('BTC_data.csv')
dates = []
prices = []

for line in df['time']:
  dates.append(line.split('T')[0])

for line in df['close']:
    prices.append(int(line))

plt.figure(figsize=(10, 5), dpi=150)
plt.plot(dates, prices, label='BTC(time)')
plt.xticks(dates[::85], rotation=310)

d = 3
c = np.polyfit(np.arange(len(prices)), prices, d)
poly = np.poly1d(c)

x = np.arange(len(prices))
plt.plot(dates, poly(x), linestyle='--')

plt.grid()
plt.legend()

plt.show()