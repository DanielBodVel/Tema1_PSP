# Es necesario instalar la librería pywin32 para trabajar con el portapapeles en Windows:
# Ejecuta en la terminal: pip install pywin32
import win32clipboard  # Importamos el módulo win32clipboard para interactuar con el portapapeles de Windows.

# Enviar datos al portapapeles
win32clipboard.OpenClipboard()  # Abre el portapapeles para manipularlo.
win32clipboard.EmptyClipboard()  # Limpia el contenido actual del portapapeles.
win32clipboard.SetClipboardText("PSP-DAM-2425")  # Establece el texto "PSP-DAM-2425" en el portapapeles.
win32clipboard.CloseClipboard()  # Cierra el portapapeles para liberar el acceso.

# Obtener datos del portapapeles
win32clipboard.OpenClipboard()  # Abre nuevamente el portapapeles para leer su contenido.
datos = win32clipboard.GetClipboardData()  # Obtiene los datos actuales del portapapeles (en este caso, el texto).
win32clipboard.CloseClipboard()  # Cierra el portapapeles para liberar el acceso.

# Imprimir el contenido obtenido del portapapeles
print(datos)
