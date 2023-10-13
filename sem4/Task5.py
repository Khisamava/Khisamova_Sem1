import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BTC_data.csv')
Time = list(df['time'])


print(Time)