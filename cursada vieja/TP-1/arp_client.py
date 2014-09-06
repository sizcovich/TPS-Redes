from scapy.all import *

def dime_su_mac(x):
	# Armo el paquete: Primero uno Ethernet con destino broadcast 	
	pkt = Ether(dst="ff:ff:ff:ff:ff:ff")
	# luego le monto un paquete ARP del tipo op=1 (Who is) con la Ip enviada por parametro
	pkt = pkt/ARP(pdst=x,op=1)
	# Envio el paquete por la interfaz por defecto
	res = srp(pkt)
	# imprimo por consola la Ip y la Mac address.
	res[0].summary(lambda(s,r):r.sprintf("IP = %ARP.psrc% -> MAC = %Ether.src%"))

if __name__ == "__main__":
	import sys
 	#la funcion toma una IP enviada por parametro cuando se la llama.
	#Ej leoraed@ubuntu:~/Desktop/Redes$ sudo python arp_client.py "192.168.75.1"
	dime_su_mac(sys.argv[1])
