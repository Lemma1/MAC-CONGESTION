import pickle
import os
import datetime
import time
import sys
import json

def convert():
	print "updating!!!"
	dataFileList = []
	newtweets = []
	for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
		if file.startswith('updatetweet'):
			dataFileList.append(file)
	for file in dataFileList:
		try:
			tweetsTemp = pickle.load(open(file,"rb"))
			newtweets.append(tweetsTemp)
		except Exception:
			print "error in reading file:::"+file
			pass
	tweets = newtweets
	for tt in tweets:
		print tt


	dpfile = '/tweetSource/twitterDBDic.p'
	oldtweets = pickle.load(open(dpfile,"rb"))
	print len(oldtweets)
	for tweet in tweets:
		for oldtweet in oldtweets:
			if oldtweet['tid']==tweet['tid']:
				print "get one !!!!!!!"
				oldtweet['category'] = tweet['category']


	pickle.dump(oldtweets,open(dpfile,'wb'))



	for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
		if file.startswith('updatetweet'):
			os.remove(file)






if __name__ == '__main__':



	while(True):
		try:
			print "updating DB"
			convert()
		except Exception:
			print "Exception!!!"
			continue



		print 'sleeping~~~~'
		time.sleep(60)





