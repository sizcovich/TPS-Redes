import argparse
from ptc import Socket
from struct import unpack

#inicializo parser
parser = argparse.ArgumentParser()
#Agrego el parametro de delay de ACK
parser.add_argument('-d', '--delay', type=float, default=0.0, help='ACK packet delay in seconds (default 0)')
#Agrego el parametro de perdida de ACK
parser.add_argument('-l', '--loss', type=float, default=0.0, help='probability of losing an ACK packet (default 0)')
#Agrego el parametro de puerto
parser.add_argument('-p', '--port', type=int, default=6677, help='PTC port')
args = parser.parse_args()
 
with Socket(ack_delay=args.delay, ack_loss_probability=args.loss) as sock:
        sock.bind(('0.0.0.0', args.port))
        sock.listen()
        print '[PTC server] Waiting for a client...'
        sock.accept()
        print '[PTC server] Connection established.'
        size = unpack('I', sock.recv(4))[0]
        print '[PTC server] Receiving %d bytes...' % size
        received = str()
        #Un while que solo reciba los datos y los lea del buffer
        #Guarda los datos recibidos en received (print para verlo)
        while len(received) < size:
            received += sock.recv(size - len(received))
            print '[PTC server] Received %d bytes.' % len(received)
 
        sock.close()
        print '[PTC server] Received %d bytes. Connection closed.' % size
