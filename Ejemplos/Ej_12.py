import subprocess  # Importamos el módulo subprocess para ejecutar comandos del sistema operativo.

# Creamos un proceso utilizando subprocess.Popen para ejecutar el comando 'dir'.
# - 'dir' es un comando de Windows que lista el contenido del directorio actual.
# - shell=True permite que el comando se ejecute a través de la línea de comandos del sistema.
# - stdout=subprocess.PIPE redirige la salida estándar del proceso, permitiendo leerla desde el programa.
# - stderr=subprocess.PIPE redirige la salida de error estándar del proceso, permitiendo capturar errores.
p1 = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Usamos un bucle for para leer cada línea de la salida del proceso.
for line in p1.stdout:
    # Eliminamos los espacios en blanco de la derecha con rstrip() y mostramos la línea.
    line_decoded = line.decode('cp850').rstrip()
    print(line_decoded)
