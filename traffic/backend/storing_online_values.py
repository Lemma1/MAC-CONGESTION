import numpy as np
from traffic.models import Philly_online_loading, Philly_congestion_array_online, Philly_link
import datetime
import os
from django.conf import settings
from MINAMI_backend.online.real_interface import get_realtime_feed


print "import online data"
with open("/home/hzn/project/dataproject/traffic/backend/MINAMI_backend/online/loading_time.txt"), "r") as f:
	interval_no = int(f.readline())
time = datetime.time(hour = interval_no / 4, minute = interval_no % 4 * 15)
loading_obj = Philly_online_loading(time = time)
loading_obj.save()

values = get_realtime_feed()
for col in values:
	link = Philly_link.objects.get(no__exact = col[0])
	link_values = Philly_congestion_array_online(loading = loading_obj,
						link = link,
						values = list(col[1:]))
	link_values.save()
