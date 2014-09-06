from scapy.all import *
import time
import sys

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

def time_elapsed(sent, received):
	return int((received.time - sent.sent_time) * 1000)

def tracert(x, maxHosts = 30):
	pkt = IP(dst=x)/ICMP()
	res = sr(pkt, timeout = 3, verbose = 0)
	dst = x
	if len(res[0]) != 0:
		dst = res[0][0][1].src

	print "Tracing route to {0} [{1}]\nover a maximum of {2} hops:\n\n".format(x, dst, maxHosts)
	i = 1
	salir = False
	while (not salir and i <= maxHosts):
		pkt = IP(dst=x, ttl=i)/ICMP()
		# Inicializacion de variables
		j = 0
		output = "{0}\t".format(i)
		dst = ""
		arrived = False
		while (j < 3):
			t0 = time.time()
			ans = sr(pkt, filter="icmp", timeout = 3, verbose = 0)
			t1 = time.time() - t0
			if str(ans[0]) <> '[]':
				arrived = True
				sent = ans[0][0][0]
				received = ans[0][0][1]
				output += "{0} ms\t".format(time_elapsed(sent, received))
				#output += "{0} ms\t".format(int(t1*1000))
				dst = received.src
				if received.type == 0:
					salir = True
			else:
				output += "*\t"
			j += 1
		if arrived:
			print output + dst
		else:
			print output + "Request timed out."
		i += 1
	print "\nTrace complete."

if __name__ == "__main__":
 	#la funcion toma una IP enviada por parametro cuando se la llama.
	#Ej leoraed@ubuntu:~/Desktop/Redes$ sudo python ping.py "192.168.75.1"
	sys.stdout = Logger("traceroute_2.txt")
	if len(sys.argv)>2:
		tracert(sys.argv[1], int(sys.argv[2]))
	else:
		if len(sys.argv)>1:
			tracert(sys.argv[1])