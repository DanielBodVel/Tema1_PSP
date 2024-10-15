import psutil

try:
    print("")
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
