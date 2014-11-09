# -*- coding: utf-8 -*-

##########################################################
#                 Trabajo Práctico 3                     #
#         Programación de protocolos end-to-end          #
#                                                        # 
#              Teoría de las Comunicaciones              #
#                       FCEN - UBA                       #
#              Segundo cuatrimestre de 2014              #
##########################################################

class RtoCalculator(object):
     
    def __init__(self, filepath, alpha, beta, k):
	print 'init rtoCalculator'
	self.filepath = filepath
	self.alpha = alpha
	self.beta = beta
	self.k = k
        self.rtt = []
	self.srtt = 0
        self.rttvar = 0
        self.rto = 100 #INITIAL_RTO
	self.rtt_rto = []
	
	self.count = 0
	self.fileRead()
	self.calculateRTT_RTO()
        
    def fileRead(self):
	with open(self.filepath, 'r') as f:
		for line in f:
	       		(acknumber, rtt) = line.split(' ')
			#print acknumber
			#print rtt 
			#print self.rtt
			self.rtt.append(float(rtt)/0.01)
			#print self.rtt
	
    def update_rtt_estimation_with(self, sampled_rtt):
	#print 'sample_rtt: ' + str(sampled_rtt)
        if self.srtt == 0:
	    print 'primera muestra'
            # Primera muestra. Actualizar los valores de acuerdo al paso 2.1
            # del RFC.
            self.srtt = sampled_rtt
            self.rttvar = sampled_rtt / 2
        else:
            # Tenemos por lo menos una muestra, por lo que actualizamos los
            # valores según el paso 2.2 del RFC.
            deviation = abs(self.srtt - sampled_rtt)
            self.rttvar = (1 - self.beta) * self.rttvar + self.beta * deviation
            self.srtt = (1 - self.alpha) * self.srtt + self.alpha * sampled_rtt
	print '-------'	+ str(self.count) + '-------'
	print 'alpha: ' +str(self.alpha)
	print 'beta: ' + str(self.beta)
	print 'rtt: ' + str(sampled_rtt)    	
	print 'rttvar: ' + str(self.rttvar)
	print 'srtt: ' + str(self.srtt)
	self.count = self.count +1
    def update_rto(self):
        self.rto = self.srtt + max(1, self.k * self.rttvar)
    	print 'rto: ' + str(self.rto)
	
    def calculateRTT_RTO(self):
        for rtt in self.rtt:
		self.update_rtt_estimation_with(rtt)
		self.update_rto()
		self.rtt_rto.append((rtt, self.rto))
        #print self.rtt_rto
