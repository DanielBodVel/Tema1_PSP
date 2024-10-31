import subprocess  # Importamos el módulo subprocess para ejecutar comandos del sistema y gestionar la entrada y salida de procesos.

# Creamos un proceso utilizando subprocess.Popen para ejecutar el comando 'ftp'.
# - 'ftp' es un programa de línea de comandos para la transferencia de archivos mediante el protocolo FTP.
# - shell=True permite ejecutar el comando a través de la línea de comandos del sistema.
# - stdin=subprocess.PIPE permite enviar datos al proceso (entrada estándar).
# - stdout=subprocess.PIPE redirige la salida estándar del proceso para leerla en el programa.
# - stderr=subprocess.PIPE redirige la salida de error estándar del proceso.
p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Lista de comandos que se enviarán al programa FTP.
# Los comandos están en formato de bytes (indicados por el prefijo 'b') y terminan con '\n' para simular la pulsación de la tecla Enter.
comandos = [b"verbose\n",             # Activa el modo detallado para mostrar más información.
            b"open test.rebex.net\n", # Abre una conexión FTP al servidor 'test.rebex.net'.
            b"demo\n",                # Usuario de prueba para la autenticación.
            b"password\n",            # Contraseña de prueba para la autenticación.
            b"ls\n",                  # Lista los archivos y directorios en el servidor remoto.
            b"get readme.txt\n"]      # Descarga el archivo 'readme.txt' desde el servidor.

# Iteramos sobre cada comando en la lista y lo enviamos al proceso FTP.
for cmd in comandos:
    p1.stdin.write(cmd)  # Escribimos el comando en la entrada estándar del proceso.

# Esperamos hasta 5 segundos a que el proceso termine y capturamos la salida.
# p1.communicate() devuelve una tupla con (salida estándar, salida de error).
# [0] indica que estamos accediendo a la salida estándar.
respuesta = p1.communicate(timeout=5)[0]

# Imprimimos la respuesta del servidor FTP, decodificándola con la codificación 'cp850' (usada en consolas Windows).
# El argumento 'ignore' en la función decode() permite ignorar errores de decodificación.
print(respuesta.decode("cp850", "ignore"))
