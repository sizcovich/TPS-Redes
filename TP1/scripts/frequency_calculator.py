#! /usr/bin/env python
import sys

if __name__ == '__main__':
	file_aux = open(sys.argv[1], 'r')
	dicc_ip_rep = {}
	
	for line in file_aux:
		if(line in dicc_ip_rep):
			dicc_ip_rep[line] = dicc_ip_rep[line] + 1 
		else:
			dicc_ip_rep[line] = 1

	for key in dicc_ip_rep.keys():
		print key.rstrip() + " " + str(dicc_ip_rep[key])
