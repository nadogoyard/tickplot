import ccxt
import asyncio
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ftxbids = []
ftxasks = []
ftxmidprices = []
ftxcloses = []

def animated_plot(i):
    
    binance = ccxt.binanceusdm()
    ftx = ccxt.ftx()
    
    #binanceticker = binance.fetch_ticker('ETH/USDT')
    ftxticker = ftx.fetch_ticker('ETH/USD:USD')

    # print(binanceticker['symbol'])
    # binancebid = binanceticker['bid']
    # binanceask = binanceticker['ask']

    ftxbid = ftxticker['bid']
    ftxask = ftxticker['ask']
    ftxmidprice = ((ftxask + ftxbid) / 2)
    ftxclose = ftxticker['close']

    ftxbids.append(ftxbid)
    ftxasks.append(ftxask)
    ftxmidprices.append(ftxmidprice)
    ftxcloses.append(ftxclose)

    plt.cla()
    plt.plot(ftxbids, drawstyle='steps-pre',label='bid')
    plt.plot(ftxasks, drawstyle='steps-pre',label='ask')
    plt.plot(ftxcloses, drawstyle='steps-pre', label='executed', alpha=0.66)
    plt.legend(loc="upper left")
    plt.xlabel("ticks")
    plt.ylabel("price")
    plt.ticklabel_format(useOffset=False)

ani = FuncAnimation(plt.gcf(), animated_plot, interval=1)

plt.show()

