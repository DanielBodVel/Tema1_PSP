# Pide al usuario que ingrese el PID de un proceso que desea terminar.
# Usa el PID ingresado para finalizar el proceso. Si no se puede finalizar el proceso
# (por ejemplo, por falta de permisos), el programa debe manejar el error y mostrar un mensaje al usuario.

import psutil

if __name__ == "__main__":

    try:
        pid = int(input("Ingrese el PID del proceso a finalizar: "))
        for proc in psutil.process_iter():
            processID = proc.pid

            if processID == pid:
                proc.terminate()

    except psutil.NoSuchProcess:
        print("Error")