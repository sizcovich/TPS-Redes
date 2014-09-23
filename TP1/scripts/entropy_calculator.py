#! /usr/bin/env python
import sys, math

if __name__ == '__main__':
	file_aux = open(sys.argv[1], 'r')
	dicc_ip_rep = {}
	length = 0

	for line in file_aux:
		if(line in dicc_ip_rep):
			dicc_ip_rep[line] = dicc_ip_rep[line] + 1 
		else:
			dicc_ip_rep[line] = 1
		length = length + 1
	entropy = 0
	for key in dicc_ip_rep.keys():
		prob = dicc_ip_rep[key]*1.0/length
		print "prob " + str(prob )
		info  = math.log(1/prob,2)
		print "info " + str(info)
		entropy = entropy + prob*info
	cantidad_ips = len(dicc_ip_rep.keys())
	max_entropy = math.log(cantidad_ips,2)
	print "Entropia: " + str(entropy)
	print "Maxima entropia: " + str(max_entropy)
	print "Cantidad de IPs: "  + str(cantidad_ips)
