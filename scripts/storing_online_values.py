import numpy as np
from traffic.models import Philly_online_loading, Philly_congestion_array_online, Philly_link
import datetime
import os
from django.conf import settings
from traffic.backend.MINAMI_backend.online.real_interface import get_realtime_feed


print "import online data"

with open(os.path.join(os.getcwd(), "loading_time"), "r") as f:
  interval_no = int(f.readline())

time = datetime.time(hour = interval_no / 4, minute = interval_no % 4 * 15)
today = datetime.date.today()
cur_time = datetime.datetime.combine(today, time)


loading_obj = Philly_online_loading(time = cur_time)
loading_obj.save()

values = get_realtime_feed()
(nrow, ncol) = values.shape
values = values[values[:,0].argsort()]

# for col in values:
# 	link = Philly_link.objects.get(no__exact = col[0])
# 	link_values = Philly_congestion_array_online(loading = loading_obj, link = link, values = list(col[1:]))
# 	link_values.save()

links = list(Philly_link.objects.all().order_by('no'))
link_objects = [None] * len(links)
for row in xrange(nrow):
  link_congestion_object = Philly_congestion_array_online(loading = loading_obj,
                      link = links[row],
                      values = values[row, 1:].tolist())
  link_objects[row] = link_congestion_object
Philly_congestion_array_online.objects.bulk_create(link_objects)