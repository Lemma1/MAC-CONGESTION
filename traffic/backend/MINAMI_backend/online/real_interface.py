import numpy as np
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
	link_dict = get_link_dic(path)
	output_dict = read_output(total_inverval, path)
	results = get_matrix(link_dict, output_dict, total_inverval)
	return results

##################################################
#######				main    			##########
##################################################

def get_realtime_feed():
	record_freq = 6
	path = os.path.join(os.getcwd(), "traffic/backend/MINAMI_backend/online")
	total_inverval = 60 * 60 / 5 / record_freq
	results = read_results(total_inverval, path)
	return results


# print get_realtime_feed()
# linkDic = dict()
# match_file = file("match_file", "w")
# link_log = file("Philly.lin", "r").readlines()[1:]
# for line in link_log:
# 	e = Link(line)
# 	if e.linkType == "LWRLK":
# 		linkDic[e.ID] = e
# for link in linkDic.itervalues():
# 	print link.ID
# 	match_file.write(" ".join([str(e) for e in [link.ID, link.name]]) + "\n") 



