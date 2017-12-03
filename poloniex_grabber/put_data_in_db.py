import requests
from datetime import datetime
import sys
import csv
import traceback
from config import config

def __setup_django(root_path, settings):
    import os
    import django

    os.chdir(root_path)

    # Django settings
    sys.path.append(root_path)
    os.environ['DJANGO_SETTINGS_MODULE'] = settings

    django.setup()

PROJECT_PATH = config.project_path
PROJECT_SETTINGS = "automate.settings"

__setup_django(PROJECT_PATH,PROJECT_SETTINGS)

from poloniex_grabber.models import *


#TODO:
#Loop each file except todays
#Set up data file comparison between linobox and desktop
#datetime_object = datetime.strptime(row_date, "%Y/%m/%d-%H:%M:%S")
#Push data into DB
#Move files into archive

#IDEAS:
#Build graph with raw sql adder for other lines
#keep copies of sqls for later implementation

###
#PoloniexCoinPairDataRaw.objects.create(coin_pair=data_coin_pair,
#	last=(rows[data_coin_pair])["last"],
#	lowest_ask = (rows[data_coin_pair])["lowestAsk"],
#	highest_bid = (rows[data_coin_pair])["highestBid"],
#	percent_change = (rows[data_coin_pair])["percentChange"],
#	base_volume = (rows[data_coin_pair])["baseVolume"],
#	quote_volume = (rows[data_coin_pair])["quoteVolume"],
#	is_frozen = (rows[data_coin_pair])["isFrozen"],
#	high_24hr = (rows[data_coin_pair])["high24hr"],
#	low_24hr = (rows[data_coin_pair])["low24hr"])
###