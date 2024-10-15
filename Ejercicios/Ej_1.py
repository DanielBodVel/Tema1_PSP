import psutil

try:
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid

        print(processName, ' --> ', processID)
        if processName == "notepad.exe":
            print("Bloc de notas está en ejecución")

except psutil.NoSuchProcess:
    print("Error")
