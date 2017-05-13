# get real time travel time of INRIX


import xml.etree.ElementTree as ET
import requests
from datetime import datetime
import time
import numpy as np
import datetime
import os
import copy
import shutil


class Signature:
    def __init__(self):
        self.Vendor = "1346213929"
        self.Consumer = "07fdc222-32d7-4aeb-ba38-136c6dbb4626"
        self.Token = "W6L*Gnt1vKJaninIVTZgucwM7oCA1762I7QHaNuijj|"


### Define a list of TMC to request ###
# tmcstring = ""
# tmclist = open("TMC_list_sample.txt", "r")
# line = tmclist.readline()
# while line:
#     tmcstring += line.strip("\n") + ","
#     line = tmclist.readline()
# tmclist.close()
# tmcstring = tmcstring[0:-1]





################################
# Vendor = "1346213929"
# Consumer = "07fdc222-32d7-4aeb-ba38-136c6dbb4626"
# Tokenreq = "http://api.inrix.com/Traffic/Inrix.ashx?Action=GetSecurityToken&Vendorid="+Vendor+"&Consumerid="+Consumer
# Token = "W6L*Gnt1vKJaninIVTZgucwM7oCA1762I7QHaNuijj|"
#### Generate TMC request call####
# TMCreq = 'http://api.inrix.com/Traffic/Inrix.ashx?Action=GetRoadSpeedinTMCs&Token=%s&tmcs=%s' % (Token, tmcstring)
# print(TMCreq)


#  get New token  #########################
def gettoken(Tokenreq):
    response = requests.get(Tokenreq)
    root = ET.fromstring(response.content)
    AuthResponse = root.find("AuthResponse")
    Token = str(AuthResponse.find("AuthToken").text)
    print(response.content)
    timestamp = str(AuthResponse.find("AuthToken").get("expiry"))
    print(timestamp + " update token")
    return Token

def build_tmc_string(tmc_list, start_idx, num):
    if start_idx + num < len(tmc_list):
        return ",".join([str(e) for e in tmc_list[start_idx: start_idx + num]])
    else:
        return ",".join([str(e) for e in tmc_list[start_idx:]])


def get_speed(tmc_list, start_idx, num, sig):
    Vendor = sig.Vendor
    Consumer = sig.Consumer
    Token = sig.Token
    Tokenreq = "http://api.inrix.com/Traffic/Inrix.ashx?Action=GetSecurityToken&Vendorid="+Vendor+"&Consumerid="+Consumer

    #### Generate TMC request call####
    tmcstring = build_tmc_string(tmc_list, start_idx, num)
    TMCreq = 'http://api.inrix.com/Traffic/Inrix.ashx?Action=GetRoadSpeedinTMCs&Token=%s&tmcs=%s' % (Token, tmcstring)

    # Request speed data ######################
    while True:
        # read TomTom real time travel time data in XML format
        try:
            response = requests.get(TMCreq)
        except:
            continue
        try:
            ############ find data in response XML parsing xml: https://docs.python.org/2/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
            root = ET.fromstring(response.content)
            # print(response.content)
            if root.get('statusId') in ["42", "43"]:
                Token = gettoken(Tokenreq) ## update token
                sig.Token = Token
                TMCreq = 'http://api.inrix.com/Traffic/Inrix.ashx?Action=GetRoadSpeedinTMCs&Token=%s&tmcs=%s' % (Token, tmcstring)
                continue
            if root.get('statusId') == "454":
                print "Can't find!"
                time.sleep(0.1) ## No TMC found
                continue
        except:
            continue
        try:
            RoadSpeedResultSet = root.find("RoadSpeedResultSet")
            RoadSpeedResults = RoadSpeedResultSet.find("RoadSpeedResults")
            timestamp = RoadSpeedResults.get("timestamp")
            # print(timestamp)
            tmp_list = list()
            for tmc in RoadSpeedResults.findall("TMC"):
                code =  tmc.get('code')
                speed =  tmc.get('speed')
                congestionLevel = tmc.get('congestionLevel')
                travelTimeMinutes = tmc.get('travelTimeMinutes')
                score = tmc.get('score')
                        # 0 = speed is 0-31% of reference speed
                        # 1 = speed is 32-62% of reference speed
                        # 2 = speed is 63-92% of reference speed
                        # 3 = speed is 93-100% of reference speed
                # if congestionLevel != "3": # record only non-freeflow tmcs
                #     continue
                if score == "30":
                    tmp_list.append((code, speed))
            break
        except:
            continue
            # print (code, speed, score)
        # with open("non_ff_traveltimes.csv", "a") as myfile:
        #     myfile.write(result)
    return tmp_list

tmc_spd = dict()
link_spd = dict()
cant_find = list()
batch_num = 150
def update_full_record(link_spd, link_to_tmc, tmc_spd, tmc_list, sig):
    cur_idx = 0
    while (cur_idx < len(tmc_list) - 1):
        tmp_list = get_speed(tmc_list, cur_idx, batch_num, sig)
        for e in tmp_list:
            tmc_spd[e[0]] = np.float(e[1])
            # time.sleep(30)
        cur_idx = cur_idx + batch_num
    for key, value in link_to_tmc.iteritems():
        try:
            link_spd[key] = tmc_spd[value]
        except:
            # print "NO key find", key, value
            cant_find.append(str(value).strip("'"))




def write_link_spd_file(link_spd, file_name):
    f = file(file_name, "w")
    f.write(str(len(link_spd)) + "\n")
    for link_id, spd in link_spd.iteritems():
        f.write(" ".join([str(e) for e in [link_id, spd]]) + "\n")
    f.close()


def read_tmc():
    TMC2LinkLog = file('TMC2LinkID.csv', 'r').readlines()

    tmc_list = list()
    link_to_tmc = dict()

    threshold = 5
    for line in TMC2LinkLog:
        words = line.split(',')
        numLink = len(words) - 1
        if numLink > threshold:
            continue
        TMCname = words[0].replace("+", "%2B")
        # TMCname = words[0]
        tmc_list.append(TMCname)
        # print words
        for i in range(numLink):
            index = i + 1
            LinkID = int(words[index])
            link_to_tmc[LinkID] = words[0]
    return tmc_list, link_to_tmc


def get_interval(hour, minute):
    return 4 * hour + minute // 15

def generate_instruction(cur_inter):
    f = file("instruction", "w")
    f2 = file("loading_time", "w")
    f.write(str(cur_inter))
    f2.write(str((cur_inter + 1) % 96))
    f.close()
    f2.close()





def rewrite_link(link_name):
    if not os.path.exists(link_name + ".backup"):
        shutil.copy2(link_name, link_name + ".backup")
    os.remove(link_name)
    shutil.copy2(link_name + ".backup", link_name)
    change_dic = get_change_dic()
    f = file(link_name + "new", "w")
    link_log = file(link_name).readlines()
    f.write(link_log[0])
    for line in link_log[1:]:
        change_flag = False
        words = line.split()
        link_ID = int(words[0])
        if link_ID in change_dic.keys():
            print "changing:", link_ID
            change_flag = True
            words[4] = float(words[4]) * (0.9 - 0.01 * change_dic[link_ID] * 0.8)    
            f.write(" ".join([str(e) for e in words]) + "\n")
        if not change_flag:
            f.write(line)
    f.close()

def get_change_dic():
    link_cap_change_name = "linkInfoUpdates.txt"
    if not os.path.exists(link_cap_change_name):
        print "No link cap drop update"
        return dict()
    else:
        change_dic = dict()
        f = file(link_cap_change_name, "r")
        for line in f:
            words = line.split()
            change_dic[int(words[0])] = float(words[1])
        f.close()
        os.remove(link_cap_change_name)
        return change_dic 

def replace_link(link_name):
    new_link_name = link_name + "new"
    if os.path.exists(new_link_name):
        os.remove(link_name)
    os.rename(new_link_name, link_name)


def modify_link(path):
    link_name = path + "MNM_input_link"
    rewrite_link(link_name)
    replace_link(link_name)


if __name__ == "__main__":
    path = ""
    sig = Signature()
    tmc_list, link_to_tmc = read_tmc()
    once = True
    while(True):
        if datetime.datetime.now().minute in [55, 10, 25 ,40] and once:
            cur_inter = get_interval(datetime.datetime.now().hour, datetime.datetime.now().minute)
            print "Current interval:", cur_inter
            update_full_record(link_spd, link_to_tmc, tmc_spd, tmc_list, sig)
            write_link_spd_file(link_spd, "MNM_input_spd")
            modify_link(path)
            generate_instruction(cur_inter)
            once = False
        else:
            print "waiting"
            time.sleep(5)
            if datetime.datetime.now().minute not in [55, 10, 25 ,40]:
                once = True
            
