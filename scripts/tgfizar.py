#!/usr/bin/env python
import sys

if len(sys.argv) < 1:
	sys.exit("Usage: python2 tgfizar.py file_path")


ips_en_red = list()
#Lista de tuplas (Ip-Src, Ip-Dst)
messages = list()
f = open(sys.argv[1], 'r')
#Conisgo todas las IP's
for line in f:
	#Sacar ips y ponerlas en list
    line = line.replace('\r\n', '')
    line = line.replace(' ', '')
    datos = line.split('\t')
    datos.remove('')
    if datos[0] == "ip_src":
        continue
    if not (datos[0] in ips_en_red):
        ips_en_red.append(datos[0])
    if datos[1] == '':
        datos[1] == datos[2]
    if not (datos[1] in ips_en_red):
        ips_en_red.append(datos[1])
	#Guardo mensaje
    messages.append((ips_en_red.index(datos[0]),ips_en_red.index(datos[1])))

for i in range(len(ips_en_red)):
    print str(i+1) + " " + ips_en_red[i]

print "#"

writen_messages = list()
for msg in messages:
    if not (msg in writen_messages):
        print str(msg[0]+1) + " " + str(msg[1]+1)
        writen_messages.append(msg)

f.close()