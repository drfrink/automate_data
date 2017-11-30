from django.shortcuts import render
import requests

from config import config

# Create your views here.
api_key = config.aplha_vantage_grabber_key

api_base_url = "https://www.alphavantage.co/query?"

stock_function = {
	'intraday' : 'TIME_SERIES_INTRADAY',
	'daily' : 'TIME_SERIES_DAILY',
	'weekly' : 'TIME_SERIES_WEEKLY',
	'monthly' : 'TIME_SERIES_MONTHLY',
	'forex' : 'CURRENCY_EXCHANGE_RATE',
}

stock_series_interval = ['1min','5min','15min','30min','60min']

stock_series_outputsize = ['compact','full']

def get_stock_data(api_function=None, api_symbol=None, api_interval=None, api_outputsize=None):
	global api_key
	global api_base_url
	global stock_function
	#https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=MSFT&apikey=demo
	api_function = stock_function[api_function]
	params = {}
	params['function'] = api_function
	if api_interval:
		params['interval'] = api_interval
	params['symbol'] = api_symbol
	params['apikey'] = api_key
	params['outputsize'] = api_outputsize
	r = requests.get( api_base_url, params=params, timeout=30)
	return r.json()

def get_current_currency_exchange_rate_data(api_function=None, api_from_currency=None, api_to_currency=None):
	global api_key
	global api_base_url
	global stock_function
	api_function = stock_function[api_function]
	params = {}
	params['function'] = api_function
	params['from_currency'] = api_from_currency
	params['to_currency'] = api_to_currency
	params['apikey'] = api_key
	r = requests.get( api_base_url, params=params, timeout=30)
	return r.json()

crypto_function = {
	'intraday' : 'DIGITAL_CURRENCY_INTRADAY',
	'daily' : 'DIGITAL_CURRENCY_DAILY',
	'weekly' : 'DIGITAL_CURRENCY_WEEKLY',
	'monthly' : 'DIGITAL_CURRENCY_MONTHLY',
}

def get_crypto_data(api_function=None, api_symbol=None, api_market=None):
	global api_key
	global api_base_url
	global crypto_function
	api_function = crypto_function[api_function]
	params = {}
	params['function'] = api_function
	params['symbol'] = api_symbol
	params['market'] = api_market
	params['apikey'] = api_key
	r = requests.get( api_base_url, params=params, timeout=30)
	return r.json()

#TODO: set up saving crypto data since it refreshes