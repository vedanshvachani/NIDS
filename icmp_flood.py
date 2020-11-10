#!/bin/python
import subprocess as sub
from collections import Counter
import time, sys, os, signal, datetime, threading
from time import strftime,gmtime
def bruteforce(ip_addr, flag):
	try:
		attacker_list = dict()
		logs = []
		DEVNULL = open(os.devnull,'w')
		p = sub.Popen(("sudo","tcpdump","-nn","-l", str(flag) +" and dst "+ str(ip_addr)),stdout=sub.PIPE)
		sec = time.time()
		end_sec = time.time() + 60
		no_attacker_ip = 0
		no_attacker_port = 0
		res = ""
		file = open("dos.txt","a")
		check = dict()
		for row in iter(p.stdout.readline, b''):
			attacker_ip = row.rstrip().split(" ")[2]
			if(attacker_ip not in attacker_list):
				attacker_list[attacker_ip] = []
			if(attacker_ip in attacker_list):
				attacker_list[attacker_ip].append(1)
			for i in attacker_list:
				if(sec < end_sec):
                        		if(len(attacker_list[i]) > 10):
						res = "TIME: "+str(strftime('%Y-%m-%d %H:%M',gmtime()))+", "+i+" is trying ICMP Flood on "+str(ip_addr)
                                        	if res not in logs:
                                        		logs.append(res)
                                                	file.write(res+"  \n")
	except OSError as e:
    		print("ok")

bruteforce("192.168.2.110","icmp")
