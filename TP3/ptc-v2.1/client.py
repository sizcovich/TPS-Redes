import argparse
from ptc import Socket, SHUT_WR
from socket import gethostbyname
from struct import pack

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Server hostname')
parser.add_argument('-p', '--port', type=int, help='Server port')
parser.add_argument('-s', '--size', type=int, help='Bytes to send')
parser.add_argument('-a', '--alpha', type=float, help='Alpha', default=0.125)
parser.add_argument('-b', '--beta', type=float, help='Beta', default=0.25)
parser.add_argument('-k', '--kvar', type=float, help='K', default=4)

args = parser.parse_args()

with Socket(beta=args.beta, alpha=args.alpha, k=args.kvar) as sock:
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

