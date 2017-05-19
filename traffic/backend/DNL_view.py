from django.contrib.auth.decorators import login_required, permission_required
from multiprocessing import Pool
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
import numpy as np
from django.conf import settings
from traffic.models import Philly_link, Philly_request, Philly_congestion, Philly_congestion_array, Philly_DMS, Philly_online_loading, Philly_congestion_array_online
from datetime import datetime, timedelta
import logging
import os
import random
import json
from django.core import serializers
from MINAMI_backend.offline.DTA_interface import get_DNL_results
import xml.etree.ElementTree as ET
from dateutil import parser, tz
import pdb
import time


def query_finished(tup):

	print "call back"
	start = time.time()

	ID = tup[2]
	params = tup[1]
	link_stat = tup[0]
	link_stat = link_stat[link_stat[:,0].argsort()]
	(nrow, ncol) = link_stat.shape


	this_request = Philly_request.objects.get(taskid__exact=ID)
	# Line up, to save time searching
	links = list(Philly_link.objects.all().order_by('no'))
	link_objects = [None] * len(links)
	for row in xrange(nrow):
		link_congestion_object = Philly_congestion_array(request = this_request,
											  link = links[row],
											  values = link_stat[row, 1:].tolist())
		link_objects[row] = link_congestion_object
	Philly_congestion_array.objects.bulk_create(link_objects)


	# Update total interval according to the matrix
	parameter = this_request.parameter
	parameter['totalInterval'] = ncol-1
	this_request.parameter = parameter
	this_request.finish = 1
	this_request.save()
	# file_lock = "/home/hzn/project/dataproject/traffic/backend/offline_task_on"
	file_lock = os.path.join(os.getcwd(), "traffic/backend/offline_task_on")
	os.remove(file_lock)
	end = time.time()
	print "done callback"


def DNL_bridge(params, ID):
	params['startTime'] = parser.parse(params['startTime'].split("(")[0])
	params['endTime'] =  parser.parse(params['endTime'].split("(")[0])
	result = get_DNL_results(params)
	return (result, params, ID)


# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def submit_link_update(request):
	print "checking...: ", os.path.join(os.getcwd(), "traffic/backend/offline_task_on")
	file_lock = os.path.join(os.getcwd(), "traffic/backend/offline_task_on")
	if (os.path.isfile(file_lock)):
		return HttpResponse("Other task is going on. Wait for a while")
	with open(file_lock, "w") as f:
		f.write("on")


	taskID = str(int(random.random() * 10000000))
	parameter = request.POST.dict()

	parameter['linkInfoUpdates'] = json.loads(parameter['linkInfoUpdates'])

	requestEntry = Philly_request(user = "admin", taskid = taskID,
								taskname = request.POST['taskName'],
								parameter = parameter, finish = 0)
	requestEntry.save()

	p = pool.apply_async(DNL_bridge, args = (parameter, taskID), callback = query_finished)

	return HttpResponse("Task successfully sent " + taskID + ", please check back 15 mintues later.")

# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def submit_link_update_online(request):
	parameter = request.POST.dict()
	parameter['linkInfoUpdates'] = json.loads(parameter['linkInfoUpdates'])
	try:
		with open("/home/hzn/project/dataproject/traffic/backend/MINAMI_backend/online/linkInfoUpdates.txt", "w") as f:
			for update in parameter['linkInfoUpdates']:
				f.write(str(update['id']) + " " + str(update['drop']) + "\n")
	except Exception,e :
		pass
	return HttpResponse("Link updates successfully sent")



# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_tasks(request):
	tasks_info = list(Philly_request.objects.values_list('taskname', 'taskid'))
	json_stuff = json.dumps({"tasks_info" : tasks_info})
	return HttpResponse(json_stuff, content_type ="application/json")

def delete_task(request):
	taskID = request.GET.get("taskID")
	Philly_request.objects.get(taskid__exact = taskID).delete()
	file_lock = os.path.join(os.getcwd(), "traffic/backend/offline_task_on")
	try:
		os.remove(file_lock)
	except Exception: pass
	return HttpResponse("Task " + str(taskID) + " successfully deleted.")

# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_parameter(request):
	req = Philly_request.objects.get(taskid__exact=request.GET['taskid'])
	parameters = req.parameter
	parameters['finish'] = req.finish
	params_json = json.dumps(parameters)

	return HttpResponse(params_json, content_type ="application/json")

from django.db.models import F
# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_congestion(request):
	# print request.POST
	taskid = int(request.POST['taskid'])
	length = int(request.POST['length'])
	time = parser.parse(request.POST['time'])
	request_object = Philly_request.objects.get(taskid__exact=taskid)
	startTime = parser.parse(request_object.parameter['startTime'].split("(")[0])
	time_delta = time.replace(tzinfo=None) - startTime.replace(tzinfo=None)

	index = int(time_delta.total_seconds() / int(request_object.parameter['resolution'])) - 1
	link_id = request.POST.getlist('link_id[]')
	link_id = [int(s) for s in link_id]
	print "get link ids: ", len(link_id)
	links = Philly_link.objects.filter(no__in=link_id)

	values = Philly_congestion_array.objects.filter(request__taskid=taskid).filter(link__in=links).annotate(link_id = F('link__no'))
	values = values.values_list("link_id", "values")
	# values = [
	# 			dict([
	# 				(obj.link_id, obj.values[index+offset])
	# 				for obj in values
	# 			])
	# 			for offset in xrange(min(length, len(values[0].values)-index))
	# 		]
	values = [
				dict([
					(val[0], val[1][index+offset])
					for val in values
				])
				for offset in xrange(min(length, len(values[0][1])-index))
			]
	# values = (values)
	return HttpResponse(json.dumps(values), content_type ="application/json")

# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_congestion_for_link(request):
	taskid = int(request.GET['taskid'])
	request_object = Philly_request.objects.get(taskid__exact=taskid)
	link_id = int(request.GET['link_id'])
	values = Philly_congestion_array.objects.get(request__exact=request_object, link__no=link_id)
	startTime = parser.parse(request_object.parameter['startTime'].split("(")[0])
	unitTime = int(request_object.parameter['resolution'])
	time_value = [
		[str(startTime + timedelta(seconds=unitTime*(i+1))), values.values[i]]
		for i in xrange(len(values.values))
	]
	return HttpResponse(json.dumps(time_value), content_type ="application/json")


# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_DMS(request):
	dms = Philly_DMS.objects.all()
	response = serializers.serialize('geojson', dms, geometry_field = 'geom')
	return HttpResponse(response, content_type='application/json')

# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def congestion_online(request):
	return render(request, 'traffic/congestion_online.html')

# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_online_congestion(request):
	start_time = Philly_online_loading.objects.all().order_by('-time')[0].time
	# start_time = request.POST['start_time']
	# if (start_time != None):
	# start_time = parser.parse(start_time).replace(tzinfo=None)

	print 'get_online_congestion:start_time', start_time

	loading = Philly_online_loading.objects.get(time__exact = start_time)
	print "get_online_time:", loading.id

	length = int(request.POST['length'])
	index = int(request.POST['index'])
	link_id = request.POST.getlist('link_id[]')
	link_id = [int(s) for s in link_id]

	links = Philly_link.objects.filter(no__in=link_id)

	values = loading.philly_congestion_array_online_set.filter(link__in=links).annotate(link_id = F('link__no'))
	values = values.values_list("link_id", "values")

	# values = [
	# 			dict([
	# 				(obj.link_id, obj.values[index+offset])
	# 				for obj in values
	# 			])
	# 			for offset in xrange(min(length, len(values[0].values)-index))
	# 		]

	values = [
				dict([
					(val[0], val[1][index+offset])
					for val in values
				])
				for offset in xrange(min(length, len(values[0][1])-index))
			]

	return HttpResponse(json.dumps(values), content_type ="application/json")

# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_latest_online_time(request):
	all_loading = Philly_online_loading.objects.all().order_by('-time')
	loading = all_loading[0]
	# loading = Philly_online_loading.objects.latest('time')
	# other_loading = all_loading[1:]
	# # print other_loading
	# print "delete ", other_loading
	# Philly_congestion_array_online.objects.filter(loading__in = other_loading).delete()
		# ol.delete()
	print "get_latest_online_time:", loading.id
	return HttpResponse(json.dumps(loading.time.isoformat()), content_type ="application/json")

# @permission_required(perm= 'traffic.congestion', raise_exception= True)
def get_real_time_VMS(request):
	vms_dict = dict(list(Philly_DMS.objects.values_list('name', 'display')))
	# field1 = "VMS_name"
	# root = ET.Element("Real-time DTA generated DMS messages")
	# doc = ET.SubElement(root, "DMS")
	# for name, message in vms_dict.iteritems():
	#     ET.SubElement(doc, field1, name=name).text = message
	return HttpResponse(json.dumps(vms_dict), content_type ="application/json")

pool = Pool(processes=1)
