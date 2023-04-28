import time
from winotify import Notification, audio
import yfinance as yfin
from datetime import datetime

tickers = ["AAPL", "NVDA", "GS", "WFC"]
upper_limits = [200, 400, 500, 100]
lower_limits = [100, 130, 140, 30]


def printFormat(current_prices):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    stocks_price = [f"{dt_string}:\t"]
    for i in range(len(tickers)):
        stock = (f"{tickers[i]} - ${current_prices[i]}\t")
        stocks_price.append(stock)
    print(*stocks_price)


def checkPrices():
    current_prices = []
    for i in range(len(tickers)):
        stock_info = yfin.Ticker(tickers[i]).info
        current_prices.append(stock_info['currentPrice'])
    printFormat(current_prices)
    return current_prices

def notification(current_prices):
    for i in range(len(tickers)):
        if current_prices[i] > upper_limits[i]:
            toast = Notification(app_id="Stock Bot",
                                 title="Price Alert: " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {current_prices[i]}.",
                                 duration="long")
            toast.set_audio(audio.LoopingAlarm6, loop=False)
            toast.show()
        elif current_prices[i] < lower_limits[i]:
            toast = Notification(app_id="Stock Bot",
                                 title="Price Alert: " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {current_prices[i]}.",
                                 duration="long")
            toast.set_audio(audio.LoopingAlarm8, loop=False)
            toast.show()
        time.sleep(5)

def main():
    while True:
        current_prices = checkPrices()
        time.sleep(5)
        notification(current_prices)


main()