from __future__ import print_function
from scapy.all import *

def sniff_arp(sniff_Count = 0, time_out = 0):
	#Formato de salida por pantalla de la captura de un paquete arp
	output = "IpSrc: %ARP.psrc%, MacSrc: %Ether.src% -> IpDst: %ARP.pdst%, MacDst: %Ether.dst%"
	#Si tiene timeout
	if (time_out > 0):
		pkts = sniff(filter="arp", prn=lambda x:x.sprintf(output), count = sniff_Count, timeout = time_out)
	else:
		pkts = sniff(filter="arp", prn=lambda x:x.sprintf(output), count = sniff_Count)
	#Si se capturaron paquetes
	if (len(pkts) > 0):
		f = open('sniff.txt','w')
		for pkt in pkts:
			#Escribe en archivo con la infromacion basica de los paquetes capturados en formato csv
			print( pkt.psrc +", "+ pkt.src +", " + pkt.pdst + ", " + pkt.dst, file = f)
		#Genera un archivo de captura de los paquetes sniffeados en formato pcap
		wrpcap("sniff.pcap", pkts)

if __name__ == "__main__":
	import sys
	if len(sys.argv)>2:
		sniff_arp(int(sys.argv[1]), int(sys.argv[2]))
	else:
		if len(sys.argv)>1:
			sniff_arp(int(sys.argv[1]))