import psutil  # Importamos la librería psutil para gestionar procesos del sistema operativo.

# Iteramos sobre todos los procesos que están activos en el sistema.
for proc in psutil.process_iter():
    try:
        # Obtenemos el nombre del proceso utilizando el metodo .name() de psutil.
        nombreProceso = proc.name()

        # Comprobamos si el nombre del proceso es "notepad.exe".
        # Esto sirve para buscar específicamente el proceso del Bloc de notas en Windows.
        if proc.name() == "notepad.exe":
            # Si encontramos el proceso, obtenemos su identificador PID.
            PID = proc.pid

            # Mostramos un mensaje indicando que vamos a eliminar (matar) el proceso encontrado.
            print("Eliminando el proceso: ", nombreProceso, ' ::: ', PID)

            # Utilizamos el metodo .kill() para finalizar inmediatamente el proceso.
            proc.kill()

    # Manejamos posibles excepciones que pueden ocurrir durante la iteración de procesos.
    # Estas excepciones incluyen:
    # - psutil.NoSuchProcess: El proceso puede haber terminado antes de que podamos interactuar con él.
    # - psutil.AccessDenied: Puede que no tengamos permisos para gestionar ciertos procesos.
    # - psutil.ZombieProcess: El proceso puede estar en estado zombi (ya finalizado, pero no limpiado por el sistema).
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print("error")  # Si ocurre alguno de estos errores, imprimimos un mensaje de error.