import psutil

def start_monitoring():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return cpu_percent, memory, disk


def show_monitoring():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    memory_used_gb = memory.used / (1024**3)
    memory_total_gb = memory.total / (1024**3)
    disk_used_gb = disk.used / (1024**3)
    disk_total_gb = disk.total / (1024**3)
    print(f"CPU användnig: {cpu_percent}%")
    print(f"Ramminne använt: {memory.percent}% | {memory_used_gb:.2f}GB av {memory_total_gb:.2f}GB Använt")
    print(f"Diskminne använt: {disk.percent}% | {disk_used_gb:.2f}GB av {disk_total_gb:.2f}GB Använt")