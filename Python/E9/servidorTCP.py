import socket
import argparse
from cryptography.fernet import Fernet
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
obj_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Crear una vinculación de una dirección al socket y puerto
print("Esperando conexión a cliente...")
obj_soc.bind((TCP_IP, TCP_PORT))
# se hace un solo intento de conexión
obj_soc.listen(1)
# Se crea la tupla donde se guarda la conexión y la dirección cliente
(conn, address) = obj_soc.accept()
# Imprimir en pantalla la dirección de la conexión
print("Dirección de conexión:", address)
# Ciclo infinito que se rompe con break
while True:
    # bvar es el mensaje del cliente
    mensaje_encryp = conn.recv(BUFFER_SIZE)
    conn.send(b"Enterado. Bye!")
    break
conn.close()
# Lectura de archivo .key
arch_key = open("clave.key", "rb")
# Guardar dato de archivo en variable
clave = arch_key.read()
# Cierre de archivo
arch_key.close()
cif_fer = Fernet(clave)
# Desencriptar el mensaje guardado previamente
mensaje_bytes = cif_fer.decrypt(mensaje_encryp, None)
# Cambiar a str variable tipo byte
mensaje_str = mensaje_bytes.decode()
# Impresión de mensaje
print("Mensaje de cliente:", mensaje_str)
