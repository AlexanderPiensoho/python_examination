import time
import psutil
from menu_functions import press_enter_to_continue


def show_all_active_alarms (alarms):
    for key in alarms.items():
        print(f"{key} alarm".upper())
        for alarm_value in alarms[key]:
            print(f"{alarm_value}%")
    

def is_alarm_monitoring (alarm_monitoring, alarms):
    alarm_monitoring = True
    try:
        while alarm_monitoring:
            print("\nAktiv övervakning pågår | tryck ctrl+c för att återvända till huvudmenyn\n".upper())
            time.sleep(2)
            for alarm in alarms["cpu"]:
                if psutil.cpu_percent(interval=1) >= (alarm):
                    print(f"🚨CPU ALARM 🚨 | ÖVERSKRIDIT {alarm}%")
            for alarm in alarms["memory"]:
                if psutil.virtual_memory().percent >= (alarm):
                    print(f"🚨RAM ALARM 🚨 | ÖVERSKRIDIT {alarm} %")
            for alarm in alarms["disk"]: 
                if psutil.disk_usage('/').percent >= (alarm):
                    print(f"🚨DISK ALARM 🚨 | ÖVERSKRIDIT {alarm}%")
    except KeyboardInterrupt:
            print("Återvänder till huvudmenyn...".upper())



