# Enumeración de procesos alternativos en Windows
import \
    subprocess  # Importamos el módulo subprocess, que nos permite ejecutar comandos del sistema y capturar su salida.

# Obtención de los procesos del sistema
# Usamos subprocess.check_output para ejecutar el comando 'wmic process list brief', que lista los procesos del sistema.
# 'wmic' es una herramienta de línea de comandos de Windows que permite acceder a información sobre procesos y otros recursos del sistema.
Datos = subprocess.check_output(['wmic', 'process', 'list', 'brief'])

# Convertimos la salida obtenida (Datos) en una cadena de texto (string), ya que inicialmente está en formato de bytes.
a = str(Datos)

try:
    # Iteramos a través de la longitud de la cadena 'a' que contiene la información de los procesos.
    for i in range(len(a)):
        # Usamos split() para dividir la cadena en partes separadas por el delimitador '\\r\\r\\n', que es el salto de línea
        # en la salida de la consola de Windows, y mostramos cada línea (i) de la información obtenida.
        print(a.split("\\r\\r\\n")[i])

# Si el índice 'i' intenta acceder a una posición fuera del rango (es decir, cuando ya no hay más líneas en la salida),
# se lanza una excepción IndexError, y el programa la maneja mostrando un mensaje de finalización.
except IndexError as e:
    print("Finalizado")
