#! /usr/bin/env python
from scapy.all import *
import pygeoip
import numpy
import ipaddress

if __name__ == '__main__':
	ttl_aux = 1
	i = 0
	ttl_max = int(sys.argv[2])
	ip_list = []
	gic = pygeoip.GeoIP('GeoLiteCity.dat')
	while(ttl_aux < ttl_max):
		packet = IP(dst=sys.argv[1], ttl=ttl_aux) / ICMP()
		ans,unans = sr(packet, timeout = 1, verbose = 0)
		#print "ttl: " + str(ttl_aux)	
		if(len(ans[ICMP]) == 0 ):
			print str(ttl_aux) + " *"
		else:
			icmp_pck = ans[ICMP][0][1]
			if(icmp_pck.type == 11):				
				#print "ip: " + str(icmp_pck.src)
				tx_time = ans[0][0].sent_time
				rx_time = ans[0][1].time
				delta = (rx_time - tx_time)*1000
				ip_list.append(icmp_pck.src)
				#print "time: " + str(delta)				
				print str(ttl_aux) + " " + str(icmp_pck.src) + " " + str(delta) 
				iplong = int(ipaddress.IPv4Address(unicode('201.212.5.12'))) #int(ipaddress.ip_address('201.212.5.12'))
				print iplong
				print gic.record_by_addr(str(iplong))
				#print gic.record_by_addr('3386115340')
				
			else:
				print str(ttl_aux) + " " + "*"	
		ttl_aux = ttl_aux+1
	print ip_list
	ip_dicc = {}
	for ip in ip_list:
		i = 0
		time_list = []		
		while(i < 3):
			packet = IP(dst=ip) / ICMP()
			#packet.display()
			ans,unans = sr(packet, timeout = 10, verbose = 0)
			while(len(ans[ICMP]) == 0 ):
				ans,unans = sr(packet, timeout = 10, verbose = 0)
			icmp_pck = ans[ICMP][0][1]								
			tx_time = ans[0][0].sent_time
			rx_time = ans[0][1].time
			delta = (rx_time - tx_time)*1000
			time_list.append(delta)		
			i = i+1
		ip_dicc[ip] = [numpy.mean(time_list), numpy.std(time_list)]
	print ip_dicc
