import ccxt
import pandas as pd 
import asyncio

async def ccxt_prices():
    binance = ccxt.binanceusdm()
    ftx = ccxt.ftx()
    while True:
        binanceticker = binance.fetch_ticker('ETH/USDT')
        ftxticker = ftx.fetch_ticker('ETH/USD:USD')

        # print(binanceticker['symbol'])
        # binancebid = binanceticker['bid']
        # binanceask = binanceticker['ask']
        # print(f"{binancebid} / {binanceask}")

        print(ftxticker['symbol'])
        ftxbid = ftxticker['bid']
        ftxask = ftxticker['ask']
        print(f"{ftxbid} / {ftxask}")

        await asyncio.sleep(0.001)
    
loop = asyncio.get_event_loop()
asyncio.ensure_future(ccxt_prices())
loop.run_forever()
