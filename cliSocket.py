import socket
import sys

# Creación de un socket TCP (stream) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Como ejemplo se usará el puerto 10000
dir_server = ('localhost', 10000)
print('Conectando al servidor {} en el puerto {}'.format(*dir_server))
sock.connect(dir_server)

try:

    # Enviar la cadena
    cadena = 'Hola Servidor, soy el cliente'
    print('Enviando {!r}'.format(cadena))
    sock.sendall(cadena)

finally:
    print('Cerrando conexión...')
    sock.close()
