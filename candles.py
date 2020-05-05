import pandas as pd
daily = pd.read_csv('apple.csv',index_col=0,parse_dates=True)
daily.index.name = 'Date'
daily.shape
daily.head(3)
daily.tail(3)


import mplfinance as mpf
mpf.plot(daily,type='candle')
