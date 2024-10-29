# PARTE 2: Finalizar Procesos Específicos
from typing import final

import psutil  # Importamos el módulo psutil para trabajar con procesos

if __name__ == "__main__":

    try:  # Intenta ejecutar el siguiente código
        nombre_proceso_buscado = input(
            "Ingrese el nombre del proceso a finalizar: ")  # Guarda en una variable el nombre a buscar en los procesos
        for proceso in psutil.process_iter():  # Itera sobre todos los procesos en ejecución
            nombre_proceso = proceso.name()  # Guardamos el nombre del proceso para poder comaprarlo

            if nombre_proceso == nombre_proceso_buscado:  # Comparamos el nombre del proceso por el proces que buscamos
                proceso.terminate()  # Si coincide lo terminamos

    except psutil.NoSuchProcess:  # Maneja la excepción si ocurre algún error con un proceso
        print("No se ha podido terminar correctamente")

    finally:  # Si ha ido correcto imprime el siguiente mensaje
        print("Proceso finalizado correctamente")
