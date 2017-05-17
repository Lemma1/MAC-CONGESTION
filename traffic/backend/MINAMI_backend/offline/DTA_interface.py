import numpy as np
import os
import datetime
import subprocess
import math
import copy
import shutil
import os

class Link:
	from1 = None
	to1	  = None
	ID = None
	linkType = None
	name = None
	length = np.float(0)
	FFS = np.float(0)
	cap = np.float(0)
	RHOJ = np.float(0)
	lane = None
	hasCounts = False
	hasSpeed = False
	volume = np.float()
	lambda_plus = np.float()
	lambda_minus = np.float()
	v = np.float()
	u = np.float()
	def __init__(self, re):
		words = re.split()
		self.ID = int(words[0])
		self.linkType = words[1]
		self.name = words[2]
		self.from1 = int(words[3])
		self.to1 = int(words[4])
		self.length = np.float32(words[5])
		self.FFS = np.float64(words[6])
		self.cap = np.float64(words[7])
		self.RHOJ = np.float64(words[8])
		self.lane = int(words[9])
	def isConnector(self):
		return int(self.RHOJ > 9999)

##################################################
#######				link    			##########
##################################################

def rewrite_link(request, link_name):
	if not os.path.exists(link_name + ".backup"):
		shutil.copy2(link_name, link_name + ".backup")
	os.remove(link_name)
	shutil.copy2(link_name + ".backup", link_name)
	if os.path.exists(link_name + "new"):
		os.remove(link_name + "new")
	f = file(link_name + "new", "w")
	link_modify_list = request["linkInfoUpdates"]
	link_log = file(link_name).readlines()
	f.write(link_log[0])
	MNM_link_list = list()
	for line in link_log[1:]:
		change_flag = False
		words = line.split()
		MNM_link_list.append(int(words[0]))
		for link_modify in link_modify_list:
			if link_modify["closed"]:
				continue
			link_ID = int(link_modify["ID"])
			speed_to_change = float(link_modify["speed"])
			cap_to_change = float(link_modify["capacity"])
			if int(words[0]) == link_ID:
				print "changing:", link_ID
				change_flag = True
				if speed_to_change > 0:
					words[3] = speed_to_change
				if cap_to_change > 0:
					words[4] = cap_to_change	
				f.write(" ".join([str(e) for e in words]) + "\n")
		if not change_flag:
			f.write(line)
	f.close()

	closed_dict = dict()
	for link_modify in link_modify_list:
		link_ID = link_modify["ID"]
		if link_ID in MNM_link_list:
			closed = link_modify["closed"]
			if closed:
				closed_dict[link_ID] = list()
	return closed_dict

def write_closed_file(path, closed_dict):
	closed_file_name = os.path.join(path, "MNM_input_workzone")
	if os.path.exists(closed_file_name):
		os.remove(closed_file_name)
	f = file(closed_file_name, "w")
	f.write(str(len(closed_dict)) + "\n")
	for key in closed_dict.keys():
		f.write(str(key) + "\n")
	f.close()

def replace_link(link_name):
	new_link_name = link_name + "new"
	if os.path.exists(new_link_name):
		os.remove(link_name)
	os.rename(new_link_name, link_name)


def modify_link(request, path):
	link_name = os.path.join(path, "MNM_input_link")
	print "rewrite link"
	closed_dict = rewrite_link(request, link_name)
	print "replace link"
	replace_link(link_name)
	print "write_closed_file"
	write_closed_file(path, closed_dict)

##################################################
#######				config    			##########
##################################################

def read_output(total_inverval, path):
	output = dict()
	link_id_list = list()
	f = file(os.path.join(path, "record/MNM_output_record_interval_volume"), 'r')
	line = f.readline()
	words = line.split()
	num_link = len(words)
	for str_link_id in words:
		link_id = int(str_link_id)
		output[link_id] = np.zeros(total_inverval)
		link_id_list.append(link_id)
	line = f.readline()
	counter = 0
	while line:
		words = line.split()
		for idx, str_link_volume in enumerate(words):
			output[link_id_list[idx]][counter] = np.float(str_link_volume)
		counter = counter + 1
		line = f.readline()
	if (counter != total_inverval):
		print "Potential error"
	f.close()
	return output

def get_link_dic(path):
	linkDic = dict()
	link_log = file(os.path.join(path, "Philly.lin"), "r").readlines()[1:]
	for line in link_log:
		e = Link(line)
		if e.linkType == "LWRLK":
			linkDic[e.ID] = e
	return linkDic

def get_matrix(link_dict, output_dict, total_inverval):
	output_matrix = np.zeros((len(link_dict), total_inverval + 1))
	for idx, link_id in enumerate(link_dict.keys()):
		output_matrix[idx][0] = link_id
		output_matrix[idx, 1:total_inverval+1] = output_dict[link_id] / (link_dict[link_id].RHOJ * np.float(link_dict[link_id].lane) * link_dict[link_id].length)
	return output_matrix


def read_results(total_inverval, path):
	print "read result1"
	link_dict = get_link_dic(path)
	print "read result2"
	output_dict = read_output(total_inverval, path)
	print "read result3"
	results = get_matrix(link_dict, output_dict, total_inverval)
	return results

def rewrite_conf(request, conf_name):
	f = file(conf_name + "new", "w")
	conf_log = file(conf_name).readlines()
	for line in conf_log:
		change_flag = False
		for trigger, value in request.iteritems():
			if line.startswith(trigger):
				print "changing:", trigger
				change_flag = True
				f.write(str(trigger) + " = " + str(value).strip("\n\t") + "\n")
		if not change_flag:
			f.write(line)

def replace_conf(conf_name):
	new_conf_name = conf_name + "new"
	if os.path.exists(new_conf_name):
		os.remove(conf_name)
	os.rename(new_conf_name, conf_name)


def modify_conf(request, path):
	conf_name = os.path.join(path, "config.conf")
	rewrite_conf(request, conf_name)
	replace_conf(conf_name)


def run_MNM(path):
	args = os.path.join(path, "dta_response")
	args = args + " " + path
	print "Excuting: ", args
	os.system(args)
	# p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# stdout, stderr = p.communicate()
	# print "Errors are:"
	# print stderr
	# print "Stdout are:"
	# print stdout
	print "Finish Excuting"
	# popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	# for line in popen.stdout:
	# 	print ">>> " + str(line.rstrip())
	# popen.wait()
	
	# output = popen.stdout.read()
	# print output


def get_interval(hour, minute):
    return 4 * hour + minute // 15
##################################################
#######				main    			##########
##################################################

def get_DNL_results(params):
	path = os.path.join(os.getcwd(), "traffic/backend/MINAMI_backend/offline")
	print "Enter get_DNL_results ", path
	# total_interval = params["total_interval"]
	# total_interval = 60
	resolution = int(params["resolution"])
	unit_time = 5
	minute_in_interval = 15
	start_time = params["startTime"]
	end_time = params["endTime"]
	veh_scalar = int(params["vehicleScalar"])

	start_interval = get_interval(start_time.hour, start_time.minute)
	print "start interval is ", start_interval
	end_interval = get_interval(end_time.hour, end_time.minute)
	print "end interval is ", end_interval
	total_interval = end_interval - start_interval
	print "total assign interval is ", total_interval
	request = dict()

	print "start modify link"
	modify_link(params, path)
	print "end modify link"

	request["max_interval"] = 24 * 60 / minute_in_interval
	request["start_assign_interval"] = start_interval
	request["rec_mode_para"] = resolution / unit_time
	request["flow_scalar"] = veh_scalar
	request["total_interval"] = total_interval * minute_in_interval * 60 / unit_time

	print "start modify conf"
	modify_conf(request, path)
	print "end modify conf"

	run_MNM(path)
	record_interval = total_interval * minute_in_interval * 60 / resolution
	results = read_results(record_interval, path)
	return results
