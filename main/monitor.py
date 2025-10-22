import psutil
import time
import platform
from log import log_event
from menu import press_enter_to_continue

BYTES_TO_GB = 1024**3
disk_path = "C:\\" if platform.system() == "Windows" else "/"  

def get_cpu_status() -> str:
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"CPU | {cpu_percent} %"

def get_memory_status() -> str:
    memory_percent = psutil.virtual_memory().percent
    memory_used_gb = psutil.virtual_memory().used / BYTES_TO_GB
    total_memory_gb = psutil.virtual_memory().total / BYTES_TO_GB
    return f"RAM-minne | {memory_percent} % | {memory_used_gb:.2f}GB använt utav {total_memory_gb:.2f}GB total"

def get_disk_status() -> str:
    disk_percent = psutil.disk_usage(disk_path).percent
    disk_used_gb = psutil.disk_usage(disk_path).used / BYTES_TO_GB
    total_disk_gb = psutil.disk_usage(disk_path).total / BYTES_TO_GB
    return f"Disk | {disk_percent} % | {disk_used_gb:.2f}GB använta utav {total_disk_gb:.2f}GB total"

def print_system_status() -> None:
    print(f"\n{get_cpu_status()}")
    print(get_memory_status())
    print(get_disk_status())
    log_event("System_status_hämtad_lyckades")
    press_enter_to_continue()

def start_monitoring() -> bool:
    print("\n🕵️ Övervakning startad 🕵️")
    log_event("Bakgrundövervakning_startad")
    press_enter_to_continue()
    return True

def print_no_monitoring_active() -> None:
    log_event("Ingen_övervakning_startad")
    print("\n❌ Övervakning är inte startad ❌")
    press_enter_to_continue()


def check_and_trigger_highest_alarm(alarm_type: str, current_value: float, alarms: dict[str, list[int]], alarm_name: str, emoji: str) -> None:
    '''
    list-comprehension used to go through all alarms and take all that are triggered and uses max() to only show the highest triggered alarm
    param: alarm_type - ie  "cpu"
    param: current_value - current value for alarm_type ie 5%
    param: alarms - all alarms in data structure dict[str, list[int]]
    alarm_name: The name that prints when alarm triggers
    emoji: just an emoji :)
    '''
    exceeded_alarms = [threshold_value for threshold_value in alarms.get(alarm_type, []) if current_value >= threshold_value]
    if exceeded_alarms:
        highest_alarm = max(exceeded_alarms)
        log_event(f"{alarm_name}_larm_triggat_{highest_alarm}_%")
        print(f"\n{emoji}{alarm_name} LARM | ÖVERSKRIDIT {highest_alarm}%{emoji}")


def active_monitoring (alarms:dict[str, list[int]]) -> None:
    log_event("Startade_aktiv_övervakning")
    try:
            while True:
                print("\nAktiv övervakning pågår | tryck ctrl+c för att återvända till huvudmenyn".upper())
                current_cpu_percent = psutil.cpu_percent(interval=0.2)
                check_and_trigger_highest_alarm("cpu", current_cpu_percent, alarms, "CPU", "🚨")

                current_memory_percent = psutil.virtual_memory().percent
                check_and_trigger_highest_alarm("memory", current_memory_percent, alarms, "RAM-MINNE", "🚨")

                current_disk_percent = psutil.disk_usage(disk_path).percent
                check_and_trigger_highest_alarm("disk", current_disk_percent, alarms, "DISK", "🚨")
                time.sleep(5)

    except KeyboardInterrupt:
            log_event(f"Användaren_avslutade_aktiv_övervakning")
            print("\nÅtervänder till huvudmenyn...\n")


