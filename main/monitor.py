import psutil
import time
from log import log_event
from menu import press_enter_to_continue

convert_bytes_to_gb = lambda: 1024**3   

def get_cpu_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"CPU | {cpu_percent} %"

def get_memory_status():
    memory_percent = psutil.virtual_memory().percent
    memory_used_gb = psutil.virtual_memory().used / convert_bytes_to_gb()
    total_memory_gb = psutil.virtual_memory().total / convert_bytes_to_gb()
    return f"RAM-minne | {memory_percent} % | {memory_used_gb:.2f}GB använt utav {total_memory_gb:.2f}GB total"

def get_disk_status():
    disk_percent = psutil.disk_usage('/').percent
    disk_used_gb = psutil.disk_usage('/').used / convert_bytes_to_gb()
    total_disk_gb = psutil.disk_usage('/').total / convert_bytes_to_gb()
    return f"Disk | {disk_percent} % | {disk_used_gb:.2f}GB använta utav {total_disk_gb:.2f}GB total"
#Uses all functions above to make a prettier main program
def print_system_status(current_log):
    print(get_cpu_status())
    print(get_memory_status())
    print(get_disk_status())
    log_event("System_status_hämtad_lyckades", current_log)
    press_enter_to_continue()

def start_monitoring():
    print("\n🕵️ ÖVERVAKNING STARTAD 🕵️\n")
    return True

#Makes sure only the highest alarm is triggered
def check_and_trigger_highest_alarm(alarm_type, current_value, alarms, alarm_name, emoji, current_log):
    exceeded_alarms = [threshold_value for threshold_value in alarms[alarm_type] if current_value >= threshold_value]
    if exceeded_alarms:
        highest_alarm = max(exceeded_alarms)
        log_event(f"{alarm_name}_alarm_triggat_{highest_alarm}_%", current_log)
        print(f"{emoji}{alarm_name} ALARM | ÖVERSKRIDIT {highest_alarm}%{emoji}")

#Starts active monitoring of the system. It scans and triggers a warning for the highest alarm.
def active_monitoring (alarms, monitoring_active, current_log):

    if monitoring_active:
        try:
            while monitoring_active:
                print("\nAktiv övervakning pågår | tryck ctrl+c för att återvända till huvudmenyn\n".upper())
                current_cpu_percent = psutil.cpu_percent(interval=0.2)
                check_and_trigger_highest_alarm("cpu", current_cpu_percent, alarms, "CPU", "🚨", current_log)
    
                current_memory_percent = psutil.virtual_memory().percent
                check_and_trigger_highest_alarm("memory", current_memory_percent, alarms, "RAM-MINNE", "🚨", current_log)

                current_disk_percent = psutil.disk_usage('/').percent
                check_and_trigger_highest_alarm("disk", current_disk_percent, alarms, "DISK", "🚨", current_log)
                time.sleep(2)

        except KeyboardInterrupt:
                log_event(f"Användaren_avslutade_aktiv_övervakning", current_log)
                print("Återvänder till huvudmenyn...".upper())
    else:
        print("Övervakning är inte startat")
        press_enter_to_continue()

