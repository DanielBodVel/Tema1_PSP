# PARTE 4: Transferencia de Datos y Manipulación del Portapapeles
import subprocess

import win32clipboard

# Creo un método para la conexión con el servidor ftp del ejemplo
def descargaDatos():
    ftp = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    comandos_ftp = [b"verbose\n", b"open test.rebex.net\n", b"demo\n", b"password\n", b"get readme.txt\n"]

    for cmd in comandos_ftp:
        ftp.stdin.write(cmd)

    readme = ftp.communicate(timeout=5)[0]
    return readme

# Creo un método para pasar el archivo descargado al portapapeles
def portapapeles(readme):
    win32clipboard.OpenClipboard()

    ppAntes = win32clipboard.GetClipboardData()

    win32clipboard.SetClipboardText(readme)

    ppDespues = win32clipboard.GetClipboardData()

    if ppAntes is not ppDespues:
        print("¡El contenido ha cambiado!\n")
    else:
        print("No ha pasado nada\n")

    win32clipboard.CloseClipboard()

# Invoco el main y los 2 métodos
if __name__ == '__main__':
    portapapeles(descargaDatos())
