# Seleccionar un proceso para finalizarlo:
from asyncio.subprocess import Process

# Pide al usuario que ingrese el PID de un proceso que desea terminar.
# Usa el PID ingresado para finalizar el proceso. Si no se puede finalizar el proceso
# (por ejemplo, por falta de permisos), el programa debe manejar el error y mostrar un mensaje al usuario.

import psutil

try:
    print("Ingresa el PID del proceso a terminar:")
    pid_del = input()

    proceso = Process(target=pid_del)
    proceso.terminate()

except:
    print("Error")