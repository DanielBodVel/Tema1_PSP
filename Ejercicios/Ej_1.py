# Listar todos los procesos activos:
# El programa debe imprimir el nombre del proceso y su identificador (PID).
# Si el proceso es el Bloc de notas (Notepad.exe), debe imprimir un mensaje especial indicando que el Bloc de notas está en ejecución.

import psutil

try:
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid

        print(processName, ' --> ', processID)
        if processName == "Notepad.exe":
            print("Bloc de notas está en ejecución")

except psutil.NoSuchProcess:
    print("Error")
