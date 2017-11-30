import requests
from models import *
import os
import django
from datetime import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'automate.settings'
django.setup()

print("HIT INTO DB")

# Create your views here.
def get_coin_pair_historic_rates(coin_pair, start=None, end=None, period=None):
	params = {}
	params['currencyPair'] = coin_pair
	if start is not None:
	    params['start'] = start
	if end is not None:
	    params['end'] = end
	if granularity is not None:
	    params['period'] = period
	    #https://poloniex.com/public?command=returnChartData&currencyPair=BTC_XMR&start=1483228800&end=9999999999&period=300
	r = requests.get("https://api.gdax.com" + '/products/{}/candles'.format(product_id), params=params, timeout=30)
	return r.json()

print("code")