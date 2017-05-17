from traffic.models import *
from django.core import serializers
import re
import json

fields = ('geom', 'v0prt', 'no', 'direction', 'length', 'tsysset', 'numlanes', 'county_10', 'hwy_num', 'cap_1h')

links = Philly_link.objects.all()
def redo(link):
    s = serializers.serialize('geojson', [link], fields=fields)
    j = json.loads(s)
    link.geom_str = json.dumps(j['features'])
    link.save()

def redo_all_links():
    i = 0
    for link in links: 
        redo(link)
        i += 1
        if i % 100 == 0: print i
    print "Done!"

task = '''
import traffic.script2
'''