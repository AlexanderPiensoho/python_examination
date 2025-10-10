import psutil
import time
from log import log_event

def start_monitoring():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    print("\n🕵️ ÖVERVAKNING STARTAD 🕵️\n")
    return cpu_percent, memory, disk
#Converts data from psutil from bytes to gigabyte.        
def bytes_to_gb(): 
    return 1024**3
#Gets current CPU usage from computers CPU
def get_cpu_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"CPU | {cpu_percent} %"
#Gets memory(RAM) precent used, currently used GB and total GB
def get_memory_status():
    memory_percent = psutil.virtual_memory().percent
    memory_used_gb = psutil.virtual_memory().used / bytes_to_gb()
    total_memory_gb = psutil.virtual_memory().total / bytes_to_gb()
    return f"Memory | {memory_percent} % | {memory_used_gb:.2f} utav {total_memory_gb:.2f} total"
#Gets Disk percent used, currently used GB and totalt GB
def get_disk_status():
    disk_percent = psutil.disk_usage('/').percent
    disk_used_gb = psutil.disk_usage('/').used / bytes_to_gb()
    total_disk_gb = psutil.disk_usage('/').total / bytes_to_gb()
    return f"Disk | {disk_percent} % | {disk_used_gb:.2f} utav {total_disk_gb:.2f} total"

#Starts active monitoring of the system. It scans all the alarms an messaure it to the current system levels
def active_monitoring (alarm_monitoring, alarms):
    alarm_monitoring = True
    try:
        while alarm_monitoring:
            print("\nAktiv övervakning pågår | tryck ctrl+c för att återvända till huvudmenyn\n".upper())
            time.sleep(2)
            for alarm in alarms["cpu"]:
                if psutil.cpu_percent(interval=0.3) >= (alarm):
                    log_event(f"CPU_alarm_triggat_{alarm}_%")
                    print(f"🚨CPU ALARM 🚨 | ÖVERSKRIDIT {alarm}%")
            for alarm in alarms["memory"]:
                if psutil.virtual_memory().percent >= (alarm):
                    log_event(f"memory_alarm_triggat_{alarm}_%")
                    print(f"🚨RAM ALARM 🚨 | ÖVERSKRIDIT {alarm} %")
            for alarm in alarms["disk"]: 
                log_event(f"disk_alarm_triggat_{alarm}_%")
                if psutil.disk_usage('/').percent >= (alarm):
                    print(f"🚨DISK ALARM 🚨 | ÖVERSKRIDIT {alarm}%")
    except KeyboardInterrupt:
            log_event(f"Användaren_avslutade_aktiv_övervakning")
            print("Återvänder till huvudmenyn...".upper())

