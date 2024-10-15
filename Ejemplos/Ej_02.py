from multiprocessing import Process  # Importa la clase Process para manejar procesos
import os  # Importa el módulo os para interactuar con el sistema operativo

# Función que será ejecutada por el proceso hijo
def hijo():
   # Imprime el ID del proceso padre (getppid) y el ID del proceso hijo (getpid)
   print("Padre: %d, Hijo: %d\n" % (os.getppid(), os.getpid()))
   # Termina el proceso hijo de forma segura
   os._exit(0)

# Función que actúa como el proceso padre
def padre():
  while True:  # Bucle infinito hasta que el usuario decida salir
    # Crea un nuevo proceso hijo usando la función 'hijo' como target
    p = Process(target=hijo)
    # Inicia la ejecución del proceso hijo
    p.start()
    # Imprime el ID del nuevo proceso hijo creado
    print("\nNuevo hijo creado ", p.pid)
    # Espera a que el proceso hijo termine (bloquea hasta que p finaliza)
    p.join()
    # Solicita al usuario si desea crear un nuevo proceso o detenerse
    reply = input("Pulsa 's' si quieres crear un nuevo proceso\n")
    # Si el usuario no introduce 's', el bucle se rompe y termina el programa
    if reply != 's':
      break

# Punto de entrada del programa, llama a la función padre
if __name__ == '__main__':
  padre()
