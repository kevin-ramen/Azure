import socket
import sys

# Creación de un socket TCP (stream) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Como ejemplo se usará el puerto 10000
dir_server = ('localhost', 10000)
print('Inicializando servidor {} en el puerto {}'.format(*dir_server))

sock.bind(dir_server)
sock.listen(1)

while True:
    # Esperamos una conexión
    print('Esperando conexión...')
    conexion, dir_cliente = sock.accept()

    try:
        print('Conexión acpetada del cliente', dir_cliente)
      
        while True:
            data = conexion.recv(16)
            print('Recibido {!r}'.format(data))
            if data:
                print('Datos recibidos...')                
            else:
                print('No se recibieron datos del cliente')
                break
    finally:
        # Cerrar la conexión
        conexion.close()
