import alpaca_trade_api as tradeapi 

SEC_KEY = ''
PUB_KEY = ''
BASE_URL = ''
api = tradeapi.REST(key_id=PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL) #base url only used in paper trading


def buy(ticker,amount): #buy stock   
    api.submit_order(
        symbol= ticker #stock ticker
        qty=amount
        side='buy'
        type='market'
        time_in_force='gtc' #good til canceled
    )
def sell(ticker,amount): #sell stock
    api.submit_order(
        symbol=ticker
        qty=amount
        side='sell'
        type='market'
        time_in_force='gtc'
    )

def main():
    #Following code gets and displays market data for stock symb.
    symb = 'SPY' #ticker 
    while True:
        print("")
        print("Checking Market Price")
        market_data = api.get_barset(symb, 'minute', limit=5) #bar data for past 5 minutes
        close_list = []
        for bar in marketData[symb]:
            close_list.append(bar.c) #bar.c is the bars closing price at time interval 

    close_list = np.array(close_list, dtype=np.float64)
    moving_average = np.mean(close_list)
    last_price = close_list[4] 
    print("Moving Average: " + str(moving_average))
    print("Last Price: " + str(last_price))
    time.sleep(60)
