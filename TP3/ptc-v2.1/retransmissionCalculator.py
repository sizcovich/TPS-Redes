import argparse
import time
from ptc import Socket, SHUT_WR
from socket import gethostbyname
from struct import pack

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Server hostname')
parser.add_argument('-a', '--alpha', type=int, help='Start Alpha')
parser.add_argument('-b', '--beta', type=int, help='Start Beta')
parser.add_argument('-p', '--port', type=int, help='Server port')
parser.add_argument('-l', '--loss', type=float, default=0.0, help='probability of losing a packet (default 0)')
parser.add_argument('-s', '--size', type=int, help='Bytes to send')
parser.add_argument('--fpath')
args = parser.parse_args()

alphaStart = args.alpha
betaStart = args.beta
for alpha in range(alphaStart,11,1):
	for beta in range(betaStart,11,1):
		filepath = args.fpath		
		with Socket(beta=beta/10.0, alpha=alpha/10.0, k=4, filepath = filepath, packet_loss_probability=args.loss) as sock:
		    print 'Connecting...'
		    print gethostbyname(args.host)
		    print args.port
		    sock.connect((gethostbyname(args.host), args.port), timeout=10)
		    print 'Connection established.'
		    print 'Sending file size...'
		    sock.send(pack('I', args.size)) #da la representacion en bytes de size
		    print 'Uploading %d bytes...' % args.size
		    sock.send('a' * args.size) #crea un string con 50 a's
		    sock.shutdown(SHUT_WR)
		time.sleep(1)
	betaStart = 0
print 'Connection closed.'

