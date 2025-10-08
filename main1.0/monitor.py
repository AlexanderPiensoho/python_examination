import psutil
import time

def start_monitoring():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    print("\n🕵️ ÖVERVAKNING STARTAD 🕵️\n")
    return cpu_percent, memory, disk
        
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

def is_alarm_monitoring (alarm_monitoring, alarms):
    alarm_monitoring = True
    try:
        while alarm_monitoring:
            print("\nAktiv övervakning pågår | tryck ctrl+c för att återvända till huvudmenyn\n".upper())
            time.sleep(2)
            for alarm in alarms["cpu"]:
                if psutil.cpu_percent(interval=0.3) >= (alarm):
                    print(f"🚨CPU ALARM 🚨 | ÖVERSKRIDIT {alarm}%")
            for alarm in alarms["memory"]:
                if psutil.virtual_memory().percent >= (alarm):
                    print(f"🚨RAM ALARM 🚨 | ÖVERSKRIDIT {alarm} %")
            for alarm in alarms["disk"]: 
                if psutil.disk_usage('/').percent >= (alarm):
                    print(f"🚨DISK ALARM 🚨 | ÖVERSKRIDIT {alarm}%")
    except KeyboardInterrupt:
            print("Återvänder till huvudmenyn...".upper())

