#! /usr/bin/env python
from scapy.all import *

if __name__ == '__main__':
	ttl_aux = 1
	ttl_max = int(sys.argv[2])
	while(ttl_aux < ttl_max):
		packet = IP(dst=sys.argv[1], ttl=ttl_aux) / ICMP()
		res = sr(packet, timeout = 5, verbose = 0)
		if(len(res[0][ICMP]) == 0 ):
			print "*\n"
		else:
			icmp_pck = res[0][ICMP][0][1]
			if(icmp_pck.type == 11):
				print "ip: " + str(icmp_pck.src) + "\n"
		print "ttl: " + str(ttl_aux)
		ttl_aux = ttl_aux+1
