# PARTE 1: Listar Procesos Activos
import psutil  # Importamos el módulo psutil para trabajar con procesos

if __name__ == '__main__':
    nombre_proceso = input(print(
        "Introduce un nombre de proceso para ver información relevante de este:"))  # Solicito al usuario el nombre del proceso a buscar

    encontrado = False  # Creo una variable booleana para indicar si se encontró el proceso

    try:  # Intenta ejecutar el siguiente código
        for proceso in psutil.process_iter():  # Itera sobre todos los procesos en ejecución
            nombre_proceso_actual = proceso.name()  # Obtengo el nombre del proceso actual
            id_proceso = proceso.pid  # Obtengo el ID del proceso actual

            if nombre_proceso_actual == nombre_proceso:  # Si el nombre coincide con el buscado
                # Obtenemos la información de memoria del proceso
                memoria_proceso = psutil.Process(id_proceso).memory_info().rss
                # Imprimimos la información formateada
                print(

                    "ID: " + id_proceso.__str__() + "\nNombre: " + nombre_proceso_actual + "\nUso de memoria (En GB): " + (

                            memoria_proceso / (1024 ** 3)).__str__())
                encontrado = True  # Marcamos que el proceso fue encontrado
                break  # Podemos salir del bucle, ya que encontramos el proceso

        if not encontrado:  # Si no se encontró el proceso
            print("El programa no se está ejecutando.")

    except PermissionError:  # Maneja la excepción si no hay permisos suficientes para ver el proceso
        print("No tienes permisos para leer el archivo.")
    except psutil.NoSuchProcess:  # Maneja la excepción si ocurre algún error con un proceso
        print("Proceso inexistente")
