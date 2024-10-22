import psutil
import os
import subprocess
import sys

def ProcesoActual():
    return psutil.Process(os.getpid())  # Obtenemos el proceso actual

def esWindows():
    try:
        sys.getwindowsversion()  # Verificamos si el sistema es Windows
    except AttributeError:
        return False
    else:
        return True

# Debug: Verificamos si el proceso actual se está obteniendo correctamente
proceso_actual = ProcesoActual()

# Intentamos imprimir el nombre y el directorio de trabajo del proceso
try:
    print("Nombre del proceso actual:", proceso_actual.name())  # nombre del proceso actual
    print("Directorio de trabajo:", proceso_actual.cwd())  # cwd() devuelve el directorio de trabajo del proceso.
except Exception as e:
    print("Error al obtener el nombre o el directorio del proceso:", e)

# Prioridad antes del cambio
print("Prioridad antes del cambio:", proceso_actual.nice())

# Cambiamos la prioridad del proceso dependiendo del sistema operativo
if esWindows():
    subprocess.check_output("wmic process where processid=\""+str(os.getpid())+"\" CALL setpriority \"below normal\"")
else:
    os.nice(1)

# Prioridad después del cambio
print("Prioridad después del cambio:", proceso_actual.nice())

# Esperamos una entrada del usuario antes de finalizar el programa
a = input("Presiona enter para salir...")
