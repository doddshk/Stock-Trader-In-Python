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
