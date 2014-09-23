#! /usr/bin/env python
from scapy.all import *
def monitor_callback(pkt):
	if ARP in pkt:
		if (pkt[ARP].op == 1) and (pkt[ARP].psrc != pkt[ARP].pdst):			
			print pkt[ARP].psrc + " " + pkt[ARP].pdst

if __name__ == '__main__':
	sniff(prn=monitor_callback, filter = "arp", store = 0)
