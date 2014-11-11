import argparse
import math

from rtoCalculator import RtoCalculator
#from constants import CLOCK_TICK

parser = argparse.ArgumentParser()
parser.add_argument('--fpathIn')
parser.add_argument('--fpathOutRTTvsRTO')
#parser.add_argument('--fpathOutRTO')
args = parser.parse_args()

CLOCK_TICK = 0.01
filepathIn = args.fpathIn
filepathOutRTTvsRTO = args.fpathOutRTTvsRTO
#filepathOutRTO = args.fpathOutRTO
for alpha in range(0,11,1):
	for beta in range(0,11,1):
		rtoCalculator = RtoCalculator(filepath = filepathIn, alpha = alpha/10.0, beta = beta/10.0, k = 4)	
		print rtoCalculator.rtt_rto
		with open(filepathOutRTTvsRTO, 'a') as f:
			norma = 0
			for (rtt, rto) in rtoCalculator.rtt_rto:
				dif_rto_rtt = rto*CLOCK_TICK - rtt*CLOCK_TICK
				norma = norma + math.pow(dif_rto_rtt, 2)
			norma = math.sqrt(norma)
			f.write(str(alpha/10.0) + ' ' + str(beta/10.0) + ' ' + str(norma))
			f.write('\n')

