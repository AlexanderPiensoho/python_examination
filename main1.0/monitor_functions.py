import psutil

def start_monitoring():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    print("\n🕵️ ÖVERVAKNING STARTAD 🕵️\n")
    return cpu_percent, memory, disk
        


def show_monitoring():
    bytes_to_gb = 1024**3
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    memory_used_gb = memory.used / bytes_to_gb
    memory_total_gb = memory.total / bytes_to_gb
    disk_used_gb = disk.used / bytes_to_gb
    disk_total_gb = disk.total / bytes_to_gb
    print(f"CPU användnig: {cpu_percent}%")
    print(f"Ramminne använt: {memory.percent}% | {memory_used_gb:.2f}GB av {memory_total_gb:.2f}GB Använt")
    print(f"Diskminne använt: {disk.percent}% | {disk_used_gb:.2f}GB av {disk_total_gb:.2f}GB Använt")

