#Det här är slutprojektet för min pythonkurs
import psutil
import time

print("==TESTAR SYSTEMÖVERVAKNING==")

print("CPU Time")
cpu_time = psutil.cpu_times(percpu=True)
print(cpu_time)

print("CPU användning")
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU: {cpu_percent}%")

print("minnesanvändning")
memory = psutil.virtual_memory()
print(f"    Totalt: {memory.total / (1024**3):.2f} GB")
print(f"    Använt: {memory.used / (1024**3):.2f} GB")
print(f"    Procent: {memory.percent}%\n")

print("Diskanvändning:")
disk = psutil.disk_usage('/')
print(f"    Totalt: {disk.total / (1024**3):.2f} GB")
print(f"    Använt: {disk.used / (1024**3):.2f} GB")
print(f"    Procent: {disk.percent}%")

cpu_threads = psutil.cpu_count(True)
print("Antalet kärnar i CPU")
print(cpu_threads)

cpu_max_hz = psutil.cpu_freq(True)
print("Max hertz")
print(cpu_max_hz)