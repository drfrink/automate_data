import requests
from datetime import datetime
import sys
import traceback

def __setup_django(root_path, settings):
    import os
    import django

    os.chdir(root_path)

    # Django settings
    sys.path.append(root_path)
    os.environ['DJANGO_SETTINGS_MODULE'] = settings

    django.setup()

PROJECT_PATH = "/home/drfrink/Documents/devProjects/automate_data"
PROJECT_SETTINGS = "automate.settings"

__setup_django(PROJECT_PATH,PROJECT_SETTINGS)

from poloniex_grabber.models import *

def grab_ticker_data():
	try:
		r = requests.get('https://poloniex.com/public?command=returnTicker')
		rows = r.json()
		for data_coin_pair in rows:
			PoloniexCoinPairDataRaw.objects.create(coin_pair=data_coin_pair,
				last=(rows[data_coin_pair])["last"],
				lowest_ask = (rows[data_coin_pair])["lowestAsk"],
				highest_bid = (rows[data_coin_pair])["highestBid"],
				percent_change = (rows[data_coin_pair])["percentChange"],
				base_volume = (rows[data_coin_pair])["baseVolume"],
				quote_volume = (rows[data_coin_pair])["quoteVolume"],
				is_frozen = (rows[data_coin_pair])["isFrozen"],
				high_24hr = (rows[data_coin_pair])["high24hr"],
				low_24hr = (rows[data_coin_pair])["low24hr"])
	except Exception as e:
		logfile = (os.getcwd() + '/poloniex_grabber/poloniex_grabber_log')
		logsize = os.path.getsize(logfile)
		if logsize > 1000000:
			print("KILLING SCRIPT")
			sys.exit()
		else:
			with open(logfile, "a") as file:
				file.write((datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ": " + traceback.format_exc())

import os
import time
starttime=time.time()
while True:
	grab_ticker_data()
	time.sleep(1.0 - ((time.time() - starttime) % 1.0))




'''
for row in rows:
	if CryptoCoinPair.objects.filter(coin_pair=row).exists():
		pass
	else:
		coin_created = CryptoCoinPair.objects.create(coin_pair=row,
			last=(rows[row])["last"],
			lowest_ask=(rows[row])["lowestAsk"],
			highest_bid=(rows[row])["highestBid"],
			percent_change=(rows[row])["percentChange"],
			base_volume=(rows[row])["baseVolume"],
			quote_volume=(rows[row])["quoteVolume"],
			is_frozen=(rows[row])["isFrozen"],
			high_24hr=(rows[row])["high24hr"],
			low_24hr=(rows[row])["low24hr"]
		)
		coin_created.save()
'''
#Set up saving coins to db if not in db,
#Set up updating table
#Set up normalize data in another app
#Set up math db

