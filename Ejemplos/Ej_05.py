import subprocess  # Importamos el módulo subprocess que permite ejecutar otros programas del sistema operativo.


def iniciaPrograma():
    try:
        SW_SHOWMAXIMIZED = 3  # Definimos una constante que indica que la ventana del programa debe abrirse maximizada.

        info = subprocess.STARTUPINFO()  # Creamos un objeto de tipo STARTUPINFO que contiene información sobre cómo iniciar el nuevo proceso.
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW  # Modificamos el campo dwFlags para usar la configuración de la ventana.
        info.wShowWindow = SW_SHOWMAXIMIZED  # Especificamos que la ventana debe mostrarse maximizada al iniciar el proceso.

        # Usamos subprocess.Popen para iniciar el programa Notepad.exe con la configuración de ventana especificada.
        subprocess.Popen('Notepad.exe', startupinfo=info)

    except subprocess.CalledProcessError as e:  # Si ocurre un error en la ejecución del proceso, se captura aquí.
        print(e.output)  # Se imprime el mensaje de error en caso de fallo.


# Llamamos a la función para iniciar el programa.
iniciaPrograma()

# Esperamos a que el usuario pulse una tecla antes de finalizar el programa.
input("Pulsa una tecla para terminar la ejecución")
