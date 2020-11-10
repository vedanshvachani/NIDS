#!/bin/python
import subprocess as sub
from collections import Counter
import time, sys, os, signal, datetime, threading
import re
from time import strftime,gmtime
def bruteforce():
	try:
		logs = []
		p = sub.Popen(("sudo","tcpdump","-A","-nn","-l","port 21"),stdout=sub.PIPE)
		res = ""
		file = open("dos.txt","a")
		check = dict()
		#user = "USER "+username
		cn = 0
		for row in iter(p.stdout.readline, b''):
			if "530" in row:
				ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}$",row.split(" ")[2])
				if(ip):
					source_ip = ip.group()
					s_ip = source_ip.replace("."+ip.group().split(".")[-1],"")
					elements = row.split(" ")
					for i in elements:
						if(i[-1] == ":"):
							g = i.replace(":","")
							rega = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,5}$",str(g))
							if(rega):
								if(rega.group() != s_ip):
									attacker_ip = rega.group().replace("."+rega.group().split(".")[-1],"")
									res = "TIME: "+str(strftime('%Y-%m-%d %H:%M',gmtime()))+", "+attacker_ip+" is trying to login on FTP Server ("+str(s_ip)+")"
									if(res not in logs):
										logs.append(res)
										file.write(res+" \n")


	except OSError as e:
    		print("ok")

bruteforce()
