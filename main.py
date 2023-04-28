import time
from winotify import Notification, audio
import yfinance as yfin

tickers = ["AAPL", "NVDA", "GS", "WFC"]
upper_limits = [200, 400, 500, 100]
lower_limits = [100, 130, 140, 30]


def printFormat(current_prices):
    stocks_price = []
    for i in range(len(tickers)):
        stock = (f"{tickers[i]} - ${current_prices[i]}\t")
        stocks_price.append(stock)
    print(*stocks_price)


def checkPrices():
    current_prices = []
    for i in range(len(tickers)):
        stock_info = yfin.Ticker(tickers[i]).info
        current_prices.append(stock_info['regularMarketOpen'])
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
        time.sleep(1)

def main():
    while True:
        current_prices = checkPrices()
        time.sleep(2)
        notification(current_prices)


main()