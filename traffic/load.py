import os
from django.contrib.gis.utils import LayerMapping
from traffic.models import Philly_link

link_mapping = {
    'no' : 'NO',
    'fromnodeno' : 'FROMNODENO',
    'tonodeno' : 'TONODENO',
    'typeno' : 'TYPENO',
    'tsysset' : 'TSYSSET',
    'length' : 'LENGTH',
    'numlanes' : 'NUMLANES',
    'capprt' : 'CAPPRT',
    'v0prt' : 'V0PRT',
    'r_v0prt': 'R_V0PRT',
    'geom' : 'LINESTRING',
}

link_consolidate_mapping = {
    'no' : 'ID',
    'v0prt' : 'V0PRT',
    'length' : 'LENGTH',
    'geom' : 'LINESTRING',
}


link_with_attr_mapping = {
    'no' : 'ID',
    'v0prt' : 'V0PRT',
    'tsysset' : 'TSYSSET',
    'numlanes' : 'NUMLANES',
    'county_10' : 'COUNTY__10',
    'hwy_num' : 'HWY_NUM',
    'cap_1h' : 'CAP_1H',
    'length' : 'LENGTH',
    'geom' : 'LINESTRING',
}

philly_link_mapping = {
    'no' : 'ID',
    'v0prt' : 'V0PRT',
    'tsysset' : 'TSYSSET',
    'numlanes' : 'NUMLANES',
    'county_10' : 'COUNTY__10',
    'hwy_num' : 'HWY_NUM',
    'cap_1h' : 'CAP_1H',
    'direction' : 'DIRECTION',
    'length' : 'LENGTH',
    'geom' : 'LINESTRING',
}

link_shp = os.path.abspath("/home/hzn/projects/data_max/philly_link/with_direction/link_with_direction_4326.shp")

def run(verbose=True):
    lm = LayerMapping(Philly_link, link_shp, philly_link_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)
