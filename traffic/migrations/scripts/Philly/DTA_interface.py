import numpy as np

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



def get_DNL_results(params):
	total_inverval = params["total_inverval"]
	linkDic = dict()
	link_log = file("Philly.lin", "r").readlines()[1:]
	for line in link_log:
		e = Link(line)
		if e.linkType == "LWRLK":
			linkDic[e.ID] = e
	first_col = np.array(linkDic.keys())
	data = np.random.rand(len(linkDic), total_inverval) * 1.3
	results = np.column_stack((first_col, data))
	return results



# params_local = dict()
# params_local["total_inverval"] = 10
# print get_DNL_results(params_local)
	