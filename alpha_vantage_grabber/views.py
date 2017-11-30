import requests
from datetime import datetime
import sys

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

print("HIT DB")

from alpha_vantage_grabber.models import *
from alpha_vantage_grabber import ticker_data
from alpha_vantage_grabber import stock_technical_indicator_data

import math
import decimal

def get_daily_stock(stockname):
	data = None
	if DailyTickerData.objects.filter(symbol=stockname).exists():
		data = ticker_data.get_stock_data(api_function="daily", api_symbol=stockname, api_outputsize="compact")
	else:
		data = ticker_data.get_stock_data(api_function="daily", api_symbol=stockname, api_outputsize="full")
	data = data["Time Series (Daily)"]
	for row in data:
		if not DailyTickerData.objects.filter(symbol=stockname, quote_time=datetime.strptime(row, "%Y-%m-%d").date()).exists():
			row_data = data[row]
			DailyTickerData.objects.create(symbol=stockname,
				open_quote=row_data["1. open"],
				high_quote=row_data["2. high"],
				low_quote=row_data["3. low"],
				close_quote=row_data["4. close"],
				volume_quote=row_data["5. volume"],
				quote_time=datetime.strptime(row, "%Y-%m-%d").date())

def get_daily_roc(stockname,period):
	data = None
	data = stock_technical_indicator_data.get_analysis_data(api_function="ROC", 
		api_symbol=stockname, 
		api_interval="daily", 
		api_time_period=str(period), 
		api_series_type="open")
	data = data["Technical Analysis: ROC"]
	for row in data:
		if not DailyRocTickerData.objects.filter(symbol=stockname, time_period=period,quote_time=datetime.strptime(row, "%Y-%m-%d").date()).exists():
			row_data = data[row]
			DailyRocTickerData.objects.create(symbol=stockname,
				roc=row_data["ROC"],
				time_period=period,
				quote_time=datetime.strptime(row, "%Y-%m-%d").date())

def backtest_roc_theory(start_dollars, stockname,period_1,period_2):
	dollars=decimal.Decimal(start_dollars)
	stock_amt=0
	#stock_data = DailyTickerData.objects.filter(symbol=stockname).order_by('quote_time')
	stock_value=0
	#roc_data = DailyRocTickerData.objects.filter(symbol=stockname,quote_time__range=["2017-08-01", "2017-11-30"]).order_by('quote_time')
	roc_data = DailyRocTickerData.objects.filter(symbol=stockname,time_period=period_1,quote_time__range=["2017-01-01", "2017-11-30"]).order_by('quote_time')
	prev_roc=0
	prev_roc2=0
	check_list=[]
	buy_value=0
	buy_date=0
	for row in roc_data:
		if DailyRocTickerData.objects.filter(symbol=stockname, time_period=period_2, quote_time=row.quote_time).exists():
			row2 = DailyRocTickerData.objects.filter(symbol=stockname, time_period=period_2, quote_time=row.quote_time).get()
			stock_data = DailyTickerData.objects.filter(symbol=stockname,quote_time=row.quote_time).get()
			check_list.append(["DATE: ",stock_data.quote_time,"ROC: ",row.roc," ROC2 :",row2.roc,"PRICE: ",stock_data.open_quote])
			try:
				if ((row.roc < -5 ) and (row2.roc < -10)) and stock_amt == 0:
					stock_data = DailyTickerData.objects.filter(symbol=stockname,quote_time=row.quote_time).get()
					stock_amt = math.floor(dollars/stock_data.open_quote)
					stock_value = stock_amt*stock_data.open_quote
					dollars -= (stock_amt*stock_data.open_quote)
					buy_value=stock_value
					buy_date=stock_data.open_quote
					print("BUYING ",stock_amt," at ",stock_data.open_quote," on ", row.quote_time)
				if stock_amt > 0 and (stock_data.open_quote != buy_date) and (( 
					(prev_roc2 > 0)
					and (row2.roc < 0)
					)
					or ((prev_roc<0) and row.roc>0)
					 or ((stock_amt*stock_data.open_quote)/(stock_value) < 0.80)):
					stock_data = DailyTickerData.objects.filter(symbol=stockname,quote_time=row.quote_time).get()
					total_value = dollars
					dollars += (stock_amt*stock_data.open_quote)
					print("SELLING ",stock_amt," at ",stock_data.open_quote," on ", row.quote_time," Profit is ",(dollars-buy_value))
					if (dollars-(stock_value+total_value)) < 0:
						for x in check_list[-60:]:
							print(x)
					stock_amt = 0
					stock_value = 0
				prev_roc2 = row2.roc
				prev_roc = row.roc
			except Exception as e:
				pass
	print("stock amt: ",stock_amt)
	print("stock value: ",stock_value)
	print("dollars: $",dollars)
	print("total: $",(dollars+stock_value))
	print("\% change ",(dollars+stock_value)/decimal.Decimal(start_dollars))

get_daily_stock("UGAZ")
get_daily_stock("DGAZ")

get_daily_roc("UGAZ",1)
#get_daily_roc("UGAZ",2)
get_daily_roc("UGAZ",3)
#get_daily_roc("UGAZ",4)
#get_daily_roc("UGAZ",5)
get_daily_roc("DGAZ",1)
get_daily_roc("DGAZ",3)

print("DONE Getting Data")

#backtest_roc_theory(1000.00, "UGAZ", 1, 3)

