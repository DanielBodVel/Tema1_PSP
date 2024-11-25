# PARTE 3: Ejecución de Programas Síncrona y Asíncrona
# Importamos lo necesário
import asyncio
import subprocess
import time


# Creamos una función para ejecutar de manera sincronizada
def sincroNotepad():
    try:  # Intenta ejecutar el siguiente código
        subprocess.run(['Notepad.exe'])  # Ejecutamos el notepad de manera sincronizada
    except subprocess.CalledProcessError:  # Recogemos el posible error
        print("Error en la ejecución de forma síncrona")


# Creamos una función para ejecutar de manera asincronizada
async def asincroNotepad():
    try:  # Intenta ejecutar el siguiente código
        await asyncio.create_subprocess_exec('Notepad.exe')  # Ejecutamos el notepad de manera asíncrona
    except subprocess.CalledProcessError:  # Recogemos el posible error
        print("Error en la ejecución de forma asíncrona")


# Metodo main
if __name__ == '__main__':
    # Creamos una variable menu para elegir que se va a ejecutar, guardando lo que el usuario mete por terminal
    menu = int(
        input(print("Hola, selecciona como quieres ejecutar el bloc de notas: \n1- Con sincronía \n2- Sin sincronía")))

    if menu == 1:  # If con la 1 opción
        inicio_temporizador = time.time()  # Creamos una variable para ver el tiempo antes de ejecutar la función
        sincroNotepad()  # LLamamos a la función
        fin_temporizador = time.time()  # Creamos la otra variable para ver el tiempo después de la ejecución
        tiempo_ejec = fin_temporizador - inicio_temporizador  # Restamos el fin menos el principio para ver el tiempo de ejecución
        print("El tiempo de ejecución fue: ", tiempo_ejec, " seg")  # Lo mostramos
    elif menu == 2:
        inicio_temporizador = time.time()  # Creamos una variable para ver el tiempo antes de ejecutar la función
        asyncio.run(asincroNotepad())  # LLamamos a la función
        fin_temporizador = time.time()  # Creamos la otra variable para ver el tiempo después de la ejecución
        tiempo_ejec = fin_temporizador - inicio_temporizador  # Restamos el fin menos el principio para ver el tiempo de ejecución
        print("El tiempo de ejecución fue: ", tiempo_ejec, " seg")  # Lo mostramos
    else:
        print("Nº no válido")  # Si el nº que ha metido no es válido
