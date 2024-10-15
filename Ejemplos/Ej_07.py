# Instalar el módulo psutil con: pip install psutil
# psutil es una librería que permite acceder a información sobre los procesos y recursos del sistema.

import psutil  # Importamos el módulo psutil, que nos permite interactuar con los procesos del sistema operativo.

try:
    # Iteramos sobre todos los procesos del sistema utilizando psutil.process_iter(), que devuelve un iterador de procesos.
    for proc in psutil.process_iter():
        # Obtenemos el nombre del proceso usando proc.name() y su identificador PID con proc.pid.
        processName = proc.name()
        processID = proc.pid

        # Imprimimos el nombre del proceso seguido de su PID.
        print(processName, ' ::: ', processID)

# Capturamos cualquier excepción que pueda ocurrir durante la iteración de procesos.
# Por ejemplo, pueden surgir excepciones si un proceso termina mientras se está obteniendo información,
# si no tenemos permisos suficientes para acceder a la información del proceso, o si el proceso está en estado zombi.
# except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
except:
    # Si ocurre cualquier error, imprimimos un mensaje de error.
    print("error")
