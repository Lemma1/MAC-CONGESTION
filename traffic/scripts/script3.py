from traffic.models import *
from django.core import serializers
import re
import json
import pickle
# fields = ('geom', 'v0prt', 'no', 'direction', 'length', 'tsysset', 'numlanes', 'county_10', 'hwy_num', 'cap_1h')

# new_fields = 'zoom_level'

cut_offs = [30, 50, 100]

# Load data (deserialize)
with open('Philly/match_dict.pkl', 'rb') as handle:
    match_dict = pickle.load(handle)


def get_zoom_level(no):
    type_no = match_dict[int(no)]
    zoom_level = None
    for idx, cut in enumerate(cut_offs):
        if type_no <= cut:
            zoom_level = idx + 1
            return zoom_level

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