from traffic.models import *
from django.core import serializers
links = Philly_link.objects.all()
serializers.serialize('json', links[0:1000], fields=("geom_str"))