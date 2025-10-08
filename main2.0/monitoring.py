import psutil

def bytes_to_gb(): 
    return 1024**3

def get_cpu_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"CPU | {cpu_percent} %"

def get_memory_status():
    memory_percent = psutil.virtual_memory().percent
    memory_used_gb = psutil.virtual_memory().used / bytes_to_gb()
    total_memory_gb = psutil.virtual_memory().total / bytes_to_gb()
    return f"Memory | {memory_percent} % | {memory_used_gb:.2f} out of {total_memory_gb:.2f} total"

def get_disk_status():
    disk_percent = psutil.disk_usage('/').percent
    disk_used_gb = psutil.disk_usage('/').used / bytes_to_gb()
    total_disk_gb = psutil.disk_usage('/').total / bytes_to_gb()
    return f"Disk | {disk_percent} % | {disk_used_gb:.2f} out of {total_disk_gb:.2f} total"

