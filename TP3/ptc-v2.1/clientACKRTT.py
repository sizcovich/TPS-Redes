import argparse
import time
from ptc import Socket, SHUT_WR
from socket import gethostbyname
from struct import pack

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Server hostname')
parser.add_argument('-a', '--alpha', type=float, help='Start Alpha')
parser.add_argument('-b', '--beta', type=float, help='Start Beta')
parser.add_argument('-p', '--port', type=int, help='Server port')
parser.add_argument('-s', '--size', type=int, help='Bytes to send')
parser.add_argument('--fpath')
args = parser.parse_args()

alpha = args.alpha
beta = args.beta
filepath = args.fpath		
with Socket(beta=beta, alpha=alpha, k=4, filepath = filepath) as sock:
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

print 'Connection closed.'
