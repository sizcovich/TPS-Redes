import msvcrt as m
import ptc as ptc

def print_server(msg):
	print "PTCServer - " + msg;

def wait(msg):
	print_server(msg)
	m.getch()
	
SERVER_IP = "198.168.0.3"
SERVER_PORT = 5555

def test_server():
	print_server("Creacion del servidor!")
	server  = ptc.PTCServer(SERVER_IP, SERVER_PORT)
	#wait("Esperando pedido de conexion?")
	server.accept()
	print_server("Aceptacion de conexion!")
	#wait("Esperando arribo de datos?")
	data = server.recv(1)
	print_server("Datos recibidos! " + data)
	wait("Esperando cierre de conexion?")
	#server.close_no_wait();

if __name__ == "__main__":
	test_server()