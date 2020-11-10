#!/bin/python
import subprocess as sub
from collections import Counter
import time, sys, os, signal, datetime, threading
from time import strftime,gmtime
def bruteforce(port_num,ip_addr,attack_name):
	try:
		attacker_list = []
		logs = []
		p = sub.Popen(("sudo","tcpdump","-nn","-l",str(port_num)+" and dst "+ str(ip_addr)),stdout=sub.PIPE)
		sec = time.time()
		end_sec = time.time() + 60
		res = ""
		file = open("dos.txt","a")
		check = dict()
		for row in iter(p.stdout.readline, b''):
			attacker_ip = row.rstrip().split(" ")[2]
			if(attacker_ip not in attacker_list):
				attacker_list.append(attacker_ip)
				po = attacker_ip.split(".")
				port = po[-1]
				ip = attacker_ip.replace(port,"").rstrip(".")
				if(ip not in check):
					check[ip] = []
				if(port not in check[ip]):
					check[ip].append(port)
				for i in check:
					if(sec < end_sec):
						if(len(check[i]) > 10):
							res = "TIME: "+str(strftime('%Y-%m-%d %H:%M',gmtime()))+", "+i+" is trying "+attack_name+" flood attack on "+str(ip_addr)
                        				if res not in logs:
                        					logs.append(res)
								print(res)
                            					file.write(res+"  \n")

	except OSError as e:
    		print("ok")

try:
 	if __name__ == "__main__":
 		ports = {"SYN": "tcp[13] & 2 != 0", "FIN": "tcp[13] & 1 != 0", "PSH": "tcp[13] & 8 != 0", "RST": "tcp[13] & 4 != 0", "ACK": "tcp[13] & 16 != 0", "URG": "tcp[13] & 32 != 0"}
 		ip = " 192.168.2.110 "
 		thread_list = []
 		for i in ports:
 			thrd = threading.Thread(target=bruteforce,args=(ports[i],ip,i,))
 			thrd.start()
 			thread_list.append(thrd)
 		for t in thread_list:
 			t.join()
except IndexError:
 	print("ok")
