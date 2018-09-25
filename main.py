

from CoinBaseExchangeAuth import CoinbaseExchangeAuth
import requests
from Ticker import Ticker
from threading import Timer
from AuthenticatedClient import AuthenticatedClient
from Algorithm import Algorithm
from UserSocket import UserSocket
from MarketData import MarketData
import time


class main:

	"This Program is used to to runb our various algorithms to buy and sell"
	"cryptocurrency (LTC)"


	global acceptable_loss,  total_loss, clock, market, coinbase_terminal, setPrice, dollar_buy

	#User Input information for keys


	#dollar_buy = float(input("How much do you want to spend?: "))
	#setPrice = float(input("What is the price you want to buy at? :"))
	
	"Open Terminal to begin purchasin"
	#coinbase_terminal = CoinbaseExchangeAuth(User_API_Key,User_Secret, User_Passphrase)


	#market = MarketSocket.MarketSocket(coinbase_terminal, 'https://api.gdax.com/products/ltc-usd/ticker')
	#auth_client = AuthenticatedClient(coinbase_terminal, market, api_url)
	"Run Algorithms from market data"
	#algo = Algorithm("dummy", auth_client, market, "10.00", "LTC-USD")


	#UserSocket = UserSocket(coinbase_terminal)
	#channels = ["ticker"]
	#UserSocket.subscribe(["LTC-USD"], channels)

	#sleep(100)
	#print(market.getPriceTable())
	#market.stopPriceTable()




main()
