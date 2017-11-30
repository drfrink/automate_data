from django.shortcuts import render
import requests

from config import config

# Create your views here.
api_key = config.aplha_vantage_grabber_key

api_base_url = "https://www.alphavantage.co/query?"

intervals = [
	'1min',
	'5min',
	'15min',
	'30min',
	'60min',
	'daily',
	'weekly',
	'monthly'
]

time_period = ['Positive integer']

series_type = [
	'close',
	'open',
	'high',
	'low'
]

indicators = {
	'SMA' : 'Simple Moving Average',
	'EMA' : 'Exponential Moving Average',
	'WMA' : 'Weighted Moving Average',
	'DEMA' : 'Double Exponential Moving Average',
	'TEMA' : 'Triple Exponential Moving Average',
	'TRIMA' : 'Triangular Moving Average',
	'KAMA' : 'Kaufman Adaptive Moving Average',
	'MAMA' : ['MESA Adaptive Moving Average', 'fastlimit=+INT','slowlimit=+INT'],
	'T3' : 'Triple Exponential Moving Average',
	'MACD' : ['Moving Average Convergence/Divergence', 'fastperiod=+INT','slowperiod=+INT','signalperiod=+INT'],
	'MACDEXT' : ['Moving Average Convergence/Divergence with controllable moving average type', 'fastperiod=+INT','slowperiod=+INT','signalperiod=+INT','fastmatype=0-8','slowmatype=0-8','signalmatype=0-8'],
	'STOCH' : ['Stochastic Oscillator', 'fastkperiod=+INT','slowkperiod=+INT','fastmatype=0-8','slowmatype=0-8'],
	'STOCHF' : ['Stochastic Fast', 'fastkperiod=+INT','fastdperiod=+INT','fastdmatype=0-8'],
	'RSI' : 'Relative Strength Index',
	'STOCHRSI' : ['Stochastic Relative Strength Index', 'fastkperiod=+INT','fastdperiod=+INT','fastdmatype=0-8'],
	'WILLR' : 'Williams R values',
	'ADX' : 'Average Directional Movement Index',
	'ADXR' : 'Average Directional Movement Index Rating',
	'APO' : ['Absolute Price Oscillator', 'fastperiod=+INT','slowperiod=+INT','matype=0-8'],
	'PPO' : ['Percentage Price Oscillator', 'fastperiod=+INT','slowperiod=+INT','matype=0-8'],
	'MOM' : 'Momentum Values',
	'BOP' : 'Balance of Power',
	'CCI' : 'Commodity Channel Index',
	'CMO' : 'Chande Momentum Oscillator',
	'ROC' : 'Rate of Change',
	'ROCR' : 'Rate of Change Ratio',
	'AROON' : 'Aroon (AROON) values',
	'AROONOSC' : 'Aroon Oscillator',
	'MFI' : 'Money Flow Index',
	'TRIX' : 'Triple Smooth Exponential Moving Average',
	'ULTOSC' : ['Ultimate Oscillator','timeperiod1=+INT','timeperiod2=+INT','timeperiod3=+INT'],
	'DX' : 'Directional Movement Index',
	'MINUS_DI' : 'Minus Directional Indicator',
	'PLUS_DI' : 'Plus Directional Indicator',
	'MINUS_DM' : 'Minus Directional Movement',


}

matypes = {
	0 : 'Simple Moving Average (SMA)', 
	1 : 'Exponential Moving Average (EMA)',
	2 : 'Weighted Moving Average (WMA)', 
	3 : 'Double Exponential Moving Average (DEMA)',
	4 : 'Triple Exponential Moving Average (TEMA)', 
	5 : 'Triangular Moving Average (TRIMA)', 
	6 : 'T3 Moving Average', 
	7 : 'Kaufman Adaptive Moving Average (KAMA)', 
	8 : 'MESA Adaptive Moving Average (MAMA)'
}

def get_analysis_data(api_function=None, 
	api_symbol=None, 
	api_interval=None, 
	api_time_period=None, 
	api_series_type=None):
	global api_key
	global api_base_url
	params = {}
	params['function'] = api_function
	if api_symbol:
		params['symbol'] = api_symbol
	if api_interval:
		params['interval'] = api_interval
	if api_time_period:
		params['time_period'] = api_time_period
	if api_series_type:
		params['series_type'] = api_series_type
	params['apikey'] = api_key
	r = requests.get( api_base_url, params=params, timeout=30)
	return r.json()