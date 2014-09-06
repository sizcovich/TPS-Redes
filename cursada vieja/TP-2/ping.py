from scapy.all import *

def time_elapsed(sent, received):
	return int((received.time - sent.sent_time) * 1000)
	
def ping(x):
	# Armo el paquete IP con ICMP 	
	pkt = IP(dst=x)/ICMP()
	# Seteo el timer
	# Envio el paquete por la interfaz por defecto
	res = sr(pkt, verbose=0)
	sent = res[0][0][0]
	received = res[0][0][1]
	time = time_elapsed(sent, received)
	# imprimo por consola.
	print "IP = {0} -> TYPE = {1} -> TTL = -> {2} -> RESPONSE TIME = {3} ms"\
	.format(res[0][0][1].src, received.type, received.ttl, time)

if __name__ == "__main__":
	import sys
 	#la funcion toma una IP enviada por parametro cuando se la llama.
	#Ej leoraed@ubuntu:~/Desktop/Redes$ sudo python ping.py "192.168.75.1"
	ping(sys.argv[1])
	
