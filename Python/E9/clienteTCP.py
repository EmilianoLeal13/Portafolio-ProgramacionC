import argparse
import socket
from cryptography.fernet import Fernet

# Descripción de ejecución impreso en pantalla
description = """ Script de conexión entre sesiones TCP y encriptador de mensaje
                Ejemplos de uso:
            + py cliente.py -msg "mensaje"
            + python cliente.py -msg "mensaje"""
# Creación de los argumentos y uso del argparse
parser = argparse.ArgumentParser(description='Comunicador de sesiones TCP',
                                 epilog=description,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-msg", metavar='msg', dest='msg', help="Mensaje a enviar",
                    required=True)
# Parsear los argumentos
params = parser.parse_args()
# Generación de la clave con Fernet
clave = Fernet.generate_key()
cifrado = Fernet(clave)
# Creación de archivo clave.key y escritura de clave
archivo_key = open('clave.key', 'wb')
archivo_key.write(clave)
archivo_key.close()
# Guardado del parámetro -msg en variable
mensaje = params.msg
# Cambiar de str a byte el mensaje argumento
byte_mensaje = mensaje.encode()
# Encriptación de mensaje de cliente
mensaje_cifrado = cifrado.encrypt(byte_mensaje)
# Impresión de mensaje en pantalla
print("Mensaje a enviar:", mensaje)
# Declaración de constantes para la conexión
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
# Creación del objeto socket para IPv4
obj_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conexión a la IP y puerto dado
obj_soc.connect((TCP_IP, TCP_PORT))
# Envío de mensaje al servidor
obj_soc.send(mensaje_cifrado)
# Decodificar la respuesta del servidor con un Buffer dado
str_respuesta = obj_soc.recv(BUFFER_SIZE).decode()
# Cierre de conexión
obj_soc.close()
# Impresión de la respuesta del servidor en pantalla
print("Respuesta de servidor:", str_respuesta)
