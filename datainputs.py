import sys
import os
import random
import time
from datetime import datetime
import pytz

project_dir = "C:/Users/Z003YT8Z/Desktop/sundar_s/Automation/automatedata"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'automatedata.settings'

import django
django.setup()
from datainput.models import DataInput

while True:
	random_number = random.randint(1,9)
	date_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d-%m-%Y %H:%M:%S")
	print(random_number)
	print(date_time)
	datafeed = DataInput.objects.create()
	datafeed.number = random_number
	datafeed.time_stamp = date_time
	datafeed.save()
	time.sleep(5)
	