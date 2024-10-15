import subprocess  # Importamos el módulo subprocess para crear y controlar procesos del sistema operativo.
import time  # Importamos el módulo time para poder hacer pausas temporales durante la ejecución del programa.


def CrearProceso():
    try:
        SW_SHOWMAXIMIZED = 3  # Definimos una constante que indica que la ventana debe abrirse maximizada.

        info = subprocess.STARTUPINFO()  # Creamos un objeto STARTUPINFO para configurar el proceso que vamos a iniciar.
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW  # Configuramos los flags para usar la ventana de inicio especificada.
        info.wShowWindow = SW_SHOWMAXIMIZED  # Indicamos que la ventana del proceso debe abrirse maximizada.

        # Creamos un proceso que ejecuta 'notepad.exe' (el Bloc de notas) usando la configuración startupinfo.
        proc = subprocess.Popen('notepad.exe', startupinfo=info)
        return proc  # Devolvemos el objeto proceso creado.

    except subprocess.CalledProcessError as e:  # Si ocurre un error al crear el proceso, lo capturamos aquí.
        print(e.output)  # Imprimimos el mensaje de error si se produce un fallo.


# Llamamos a la función CrearProceso y almacenamos el proceso devuelto en la variable 'p'.
p = CrearProceso()

# Imprimimos el ID del proceso (PID), que es un identificador único del proceso en el sistema operativo.
print("El PID de este proceso es: " + str(p.pid))

# Hacemos una pausa de 5 segundos antes de que el programa continúe.
time.sleep(5)
