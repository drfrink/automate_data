import requests
from datetime import datetime
import sys
import csv
import traceback
from config import config

def grab_ticker_data():
	try:
		r = requests.get('https://poloniex.com/public?command=returnTicker')
		rows = r.json()
		row_date = time.strftime("%Y/%m/%d-%H:%M:%S")
		timestr = time.strftime("%Y%m%d%H%M")
		with open((config.data_storage + timestr),'a+') as datafile:
			datawriter = csv.writer(datafile)
			for data_coin_pair in rows:
				datawriter.writerow([data_coin_pair,
					(rows[data_coin_pair])["last"],
					(rows[data_coin_pair])["lowestAsk"],
					(rows[data_coin_pair])["highestBid"],
					(rows[data_coin_pair])["percentChange"],
					(rows[data_coin_pair])["baseVolume"],
					(rows[data_coin_pair])["quoteVolume"],
					(rows[data_coin_pair])["isFrozen"],
					(rows[data_coin_pair])["high24hr"],
					(rows[data_coin_pair])["low24hr"],
					row_date])
	except Exception as e:
		print(type(e))
		print(e.args)
		print(e)
		print((datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ": " + traceback.format_exc())

import os
import time
starttime=time.time()
while True:
	grab_ticker_data()
	time.sleep(1.0 - ((time.time() - starttime) % 1.0))


