from traffic.models import *
from django.core import serializers
import re
import json
import pickle
# fields = ('geom', 'v0prt', 'no', 'direction', 'length', 'tsysset', 'numlanes', 'county_10', 'hwy_num', 'cap_1h')

# new_fields = 'zoom_level'

cut_offs = [40, 50, 100]

cut_dict = {1: [41, 42, 43, 51, 52, 61, 62, 72, 81, 82, 83, 85, 86, 92], 2: [31, 32, 33], 3:[5, 11, 12, 13, 21, 22, 23]}

# Load data (deserialize)
with open('Philly/match_dict.pkl', 'rb') as handle:
    match_dict = pickle.load(handle)


def get_zoom_level(no):
    type_no = match_dict[int(no)]
    for key, cut in cut_dict.iteritems():
        if type_no in cut:
            return key
    print "ERROR!!!!"

links = Philly_link.objects.all()

def redo(link):
    link.zoom_level = get_zoom_level(link.no)
    link.save()

def redo_all_links():
    i = 0
    for link in links: 
        redo(link)
        i += 1
        if i % 100 == 0: print i
    print "Done!"

# task = '''
# import traffic.script2
# '''