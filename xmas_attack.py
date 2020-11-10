#!/bin/python
import subprocess as sub
from collections import Counter
import time, sys, os, signal, datetime, threading
from time import strftime,gmtime
def bruteforce(ip_addr, flag, attack_name):
	try:
		attacker_list = dict()
		logs = []
		DEVNULL = open(os.devnull,'w')
		p = sub.Popen(("sudo","tcpdump","-nn","-l",str(flag)+" and dst "+ str(ip_addr)),stdout=sub.PIPE)
		sec = time.time()
		end_sec = time.time() + 60
		no_attacker_ip = 0
		no_attacker_port = 0
		res = ""
		file = open("dos.txt","a")
		check = dict()
		for row in iter(p.stdout.readline, b''):
			ip = row.rstrip().split(" ")[2]
			po = ip.split(".")
			port = po[-1]
			attacker_ip = ip.replace(port,"").rstrip(".")
			if(attacker_ip not in attacker_list):
				attacker_list[attacker_ip] = []
			if(attacker_ip in attacker_list):
				attacker_list[attacker_ip].append(1)
			for i in attacker_list:
				if(sec < end_sec):
                        		if(len(attacker_list[i]) > 10):
						res = "TIME: "+str(strftime('%Y-%m-%d %H:%M',gmtime()))+", "+i+" is trying "+attack_name+" on "+str(ip_addr)
                                        	if res not in logs:
                                        		logs.append(res)
							print(res)
                                                	file.write(res +"  \n")
	except OSError as e:
    		print("ok")


try:
 	if __name__ == "__main__":
 		flags = {"xmas scan":'tcp[tcpflags] & tcp-fin == tcp-fin and tcp[tcpflags] & tcp-push == tcp-push and tcp[tcpflags] & tcp-urg == tcp-urg', "FIN Scan": "tcp[tcpflags] & tcp-fin == tcp-fin", "ACK Scan": "tcp[tcpflags] & tcp-ack == tcp-ack"}
 		ip = " 192.168.2.110 "
 		thread_list = []
 		for i in flags:
 			thrd = threading.Thread(target=bruteforce,args=(ip,flags[i],i,))
 			thrd.start()
 			thread_list.append(thrd)
 		for t in thread_list:
 			t.join()
#except (Exception, KeyboardInterrupt, IndexError):
#	thr.join()
except IndexError:
 	print("ok")
