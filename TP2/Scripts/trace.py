#! /usr/bin/env python
from scapy.all import *
import pygeoip
import numpy
import ipaddress
import time
import ast
from mpl_toolkits.basemap import Basemap
import  matplotlib.pyplot as pl
from PIL import *


if __name__ == '__main__':
	ttl_aux = 1
	i = 0
	ttl_max = int(sys.argv[2])
	ip_list = []
	gic = pygeoip.GeoIP('GeoLiteCity.dat')
	ip_rtt_dicc = {}
	latitudes = []
	longitudes = []
	while(ttl_aux < ttl_max):
		packet = IP(dst=sys.argv[1], ttl=ttl_aux) / ICMP()
		time.sleep(0.5)
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
				ip_rtt_dicc[icmp_pck.src] = [delta]
				#print "time: " + str(delta)				
				print str(ttl_aux) + " " + str(icmp_pck.src) + " " + str(delta) 
				iplong = int(ipaddress.IPv4Address(unicode(str(icmp_pck.src))))
				ipdata = gic.record_by_addr(str(iplong))
				tipo = type(ipdata)
				#me guardo las coordenadas para el mapa
				if(tipo == dict):
					latitudes.append(ipdata['latitude'])
					longitudes.append(ipdata['longitude'])
			else:
				print str(ttl_aux) + " " + "*"	
		ttl_aux = ttl_aux+1

	#creacion de mapa y trazado de recorrido
	fig = pl.figure(figsize=(12,12))
	ax = fig.add_axes([0.1,0.1,0.8,0.8])
	mapa = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c', area_thresh=1000.)
	mapa.bluemarble()
	mapa.drawcoastlines(linewidth=0.5)
	mapa.drawcountries(linewidth=0.5)
	mapa.drawstates(linewidth=0.5)
	mapa.drawparallels(numpy.arange(-180.,180.,20.),labels=[1,0,0,1])
	mapa.drawmeridians(numpy.arange(-180.,180.,20.),labels=[1,0,0,1])
	mapa.drawmapboundary(fill_color='aqua')
	x,y = mapa(longitudes, latitudes)
	pl.plot(x,y,'y-',linewidth=2 )
	pl.show()

	ip_dicc = {}
	for ip in ip_list:
		i = 0
		time_list = []		
		while(i < 10):
			packet = IP(dst=ip) / ICMP()
			#packet.display()
			time.sleep(0.5)
			ans,unans = sr(packet, timeout = 2, verbose = 0)
			if(len(ans[ICMP]) != 0 ):
				icmp_pck = ans[ICMP][0][1]								
				tx_time = ans[0][0].sent_time
				rx_time = ans[0][1].time
				delta = (rx_time - tx_time)*1000
				ip_rtt_dicc[ip].append(delta)
				time_list.append(delta)		
			i = i+1
		ip_dicc[ip] = [numpy.mean(ip_rtt_dicc[ip]), numpy.std(ip_rtt_dicc[ip])]
	print ip_rtt_dicc
	print ""
	print ip_dicc
