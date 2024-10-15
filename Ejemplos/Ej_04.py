import subprocess  # Importa el módulo subprocess para ejecutar comandos del sistema desde Python.

# Bloque try-except para manejar errores en la ejecución de los comandos
try:
    # Ejecuta el comando ping para comprobar la conectividad con el sitio web de educacyl.
    # -n 5: Especifica que se enviarán 5 paquetes ICMP (pings). Este argumento es específico para Windows.
    subprocess.run(["ping", "www.educa.jcyl.es", "-n", "5"])

    # En Linux o sistemas basados en Unix, la opción para especificar el número de paquetes es "-c" en lugar de "-n".
    # subprocess.run(["ping", "www.educa.jcyl.es", "-c", "5"])  # Comando equivalente en Linux

# Excepción para capturar errores relacionados con la ejecución del comando.
except subprocess.CalledProcessError as e:
    # Si ocurre un error durante la ejecución del comando ping, se imprime el contenido del error.
    print(e.output)
