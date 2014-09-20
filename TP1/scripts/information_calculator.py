#! /usr/bin/env python
import sys, math, operator

if __name__ == '__main__':
	file_aux = open(sys.argv[1], 'r')
	dicc_ip_rep = {}
	dicc_ip_info = {}
	length = 0
	for line in file_aux:
		if(line in dicc_ip_rep):
			dicc_ip_rep[line] = dicc_ip_rep[line] + 1 
		else:
			dicc_ip_rep[line] = 1
		length = length + 1
	for key in dicc_ip_rep.keys():
		prob = dicc_ip_rep[key]*1.0/length
		info  = math.log(1/prob,2)
		dicc_ip_info[key] = info		
		#print key.rstrip() + " " + str(info)
	sorted_ip_info = sorted(dicc_ip_info.iteritems(), key=operator.itemgetter(1))
	for [ip , info] in sorted_ip_info:
		print ip.rstrip() + " " + str(info)
	
