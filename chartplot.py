import ccxt
import pandas as pd 

binance = ccxt.binance()
binancemarkets = binance.load_markets()
binance_eth = binance.markets['ETH/USDT']
print(binance_eth[2])

ftx = ccxt.ftx()
ftxmarkets = ftx.load_markets()

#print(ccxt.exchanges)