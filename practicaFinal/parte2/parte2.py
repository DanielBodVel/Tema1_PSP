# PARTE 3: Comunicación Interprocesos con Pipes
import os


def main():
    pipe = os.pipe()
    saludo_padre = "Hola hijo"
    id_padre = os.fork()

    if id_padre < 0:  # Error de creación del hijo
        print("Ha ocurrido algún error")

    elif id_padre == 0:  # Proceso hijo
        os.close(pipe[1])
        mensaje_pipe = os.read(pipe[0], 80).decode("utf-8")
        mensaje_pipe.upper()
        os.close(pipe[0])
        os.write(pipe[1], mensaje_pipe.encode("utf-8"))
        os.close(pipe[1])

    else:
        os.close(pipe[0])
        os.write(pipe[1], saludo_padre.encode("utf-8"))
        os.close(pipe[1])
        print(os.read(pipe[0], 80).decode("utf-8"))
        os.wait()


if __name__ == '__main__':
    main()
