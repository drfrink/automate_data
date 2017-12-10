import requests
from datetime import datetime
import sys
import csv
import traceback
from config import config
import os

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

def push_coin_data_into_db(indir):
	for root, dirs, filenames in os.walk(indir):
		for f in filenames:
			#print(os.path.join(root,f))
			filename, file_extension = os.path.splitext(os.path.join(root,f))
			if file_extension != ".xz":
				with open(os.path.join(root, f), 'r') as data_file:
					reader = csv.reader(data_file)
					for line in reader:
						line_datetime = datetime.strptime(line[10], '%Y/%m/%d-%H:%M:%S')
						if PoloniexCoinPairDataRaw.objects.filter(coin_pair=line[0], created_at=line_datetime).exists():
							pass
						else:
							PoloniexCoinPairDataRaw.objects.create(coin_pair=line[0],
								last=line[1],
								lowest_ask =line[2],
								highest_bid =line[3],
								percent_change =line[4],
								base_volume =line[5],
								quote_volume =line[6],
								is_frozen =line[7],
								high_24hr =line[8],
								low_24hr =line[9],
								created_at = line_datetime)
				with open('/tmp/rm_file_list','a+') as rm_file:
					rm_file.write(os.path.join(root, f) + '\n')


indir = config.data_path
push_coin_data_into_db(indir)


#


#import time
#def follow(thefile,count):
    #thefile.seek(0,2)
#    while True:
#        line = thefile.readline()
#        if not line:
#            time.sleep(0.1)
#            continue
#        count += 1
#        yield count
#        yield line

#
#logfile = open("/mnt/DataWhore/automate_data/poloniex_20171208","r")
#count = 0
#loglines = follow(logfile,count)
#for line in loglines:
#    print(line)
#    print(count)
#
#TODO:
#Loop each file except todays
#Set up data file comparison between linobox and desktop
#datetime_object = datetime.strptime(row_date, "%Y/%m/%d-%H:%M:%S")
#Push data into DB
#Move files into archive

#IDEAS:
#Build graph with raw sql adder for other lines
#keep copies of sqls for later implementation
#Set up backtest record profit and loss indiciator values

