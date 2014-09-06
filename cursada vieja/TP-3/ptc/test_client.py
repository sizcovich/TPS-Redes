import msvcrt as m
import ptc as ptc

from packet_data import DataPacket

def print_client(msg):
	print "PTCClient - " + msg

def wait(msg):
	print_client(msg)
	m.getch()

SERVER_IP = "198.168.0.3"
SERVER_PORT = 5555
CLIENT_IP = "198.168.0.2"
CLIENT_PORT = 12345

def test_client():
	print_client("Creacion del cliente!")
	client = ptc.PTCClient(CLIENT_IP, CLIENT_PORT)
	#wait("Creacion del servidor?")
	print_client("Pedido de conexion!")
	client.connect(SERVER_IP, SERVER_PORT)
	#wait("Aceptacion de conexion?")
	print_client("Enviando datos!")
	#client.send('hola!') 
	client.send_file(DataPacket(1))
	#wait("Acuse de recivo de datos enviados?")
	print_client("Cierre de conexion!")
	#client.close()

if __name__ == "__main__":
	test_client()