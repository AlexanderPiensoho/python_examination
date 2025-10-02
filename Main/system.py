from monitor_functions import start_monitoring, show_monitoring
from menu_functions import show_main_menu, main_menu_input_choice, show_set_alarm_menu, set_alarm_choice

import psutil
import time

alarms = {
    "cpu": [2, 10, 40],
    "memory": [2,30, 40],
    "disk": [2]
}
set_alarm_menu_is_running = False
main_menu_is_running = True
monitoring_active = False
alarm_monitoring = False
bytes_to_gb = 1024**3

print("=================================")
print("====Välkommen till huvudmenyn====".upper())
print("=================================")

while main_menu_is_running:
    show_main_menu()
    menu_choice = main_menu_input_choice()

    if menu_choice == "1":
        monitoring_active = True
        start_monitoring()
        print("\n🕵️ Övervakning startad 🕵️\n".upper())
        input("Tryck enter för att komma tillbaka till menyn...".upper())

    elif menu_choice == "2":
        if not monitoring_active:
            print("\n❌ Ingen övervakning aktiv ❌\n".upper())
        else:
            print()
            show_monitoring()
            print()
            input("Tryck enter för att komma tillbaka till menyn...".upper())

    elif menu_choice == "3":
        set_alarm_menu_is_running = True
        while set_alarm_menu_is_running:
            show_set_alarm_menu()
            alarm_menu_choice = set_alarm_choice()
            if alarm_menu_choice == "1":
                cpu_alarm = int(input("Ställ in en nivå för CPU alarm, mellan 0-100%: "))
                alarms["cpu"].append(cpu_alarm)
                print(f"Ditt CPU alarm är inställt på {cpu_alarm}%\n")
            elif alarm_menu_choice == "2":
                memory_alarm = int(input("Ställ in en nivå för ditt RAM-minne alarm, mellan 0-100%: "))
                alarms["memory"].append(memory_alarm)
                print(f"Ditt RAM-minne alarm är inställt på {memory_alarm}%\n")
            elif alarm_menu_choice == "3":
                disk_alarm = int(input("Ställ in en nivå för ditt Disk-minne alarm, mellan 0-100%: "))
                alarms["disk"].append(disk_alarm)
                print(f"Ditt disk-minne alarm är inställt på {disk_alarm}%\n")
            elif alarm_menu_choice == "4":
                print("\nDu skickas tillbaka till huvudmenyn\n".upper())
                set_alarm_menu_is_running = False
            else:
                print("Du måste välja en siffra mellan 1-4")
        

    elif menu_choice == "4":
        for key, value in alarms.items():
            print(f"{key} alarm".upper())
            for alarm_value in alarms[key]:
                print(f"{alarm_value}%")
        input("Tryck enter för att komma tillbaka till menyn...".upper())

    elif menu_choice == "5":
        alarm_monitoring = True
        try:
            while alarm_monitoring:
                print("\nAktiv övervakning pågår | tryck ctrl+c för att återvända till huvudmenyn\n".upper())
                time.sleep(2)
                for alarm in alarms["cpu"]:
                    if psutil.cpu_percent(interval=1) >= (alarm):
                        print(f"🚨CPU ALARM🚨 | ÖVERSKRIDIT {alarm}%")
                for alarm in alarms["memory"]:
                    if psutil.virtual_memory().percent >= (alarm):
                        print(f"🚨RAM ALARM🚨 | ÖVERSKRIDIT {alarm} %")
                for alarm in alarms["disk"]: 
                    if psutil.disk_usage('/').percent >= (alarm):
                        print(f"🚨DISK ALARM🚨 | ÖVERSKRIDIT {alarm}%")
        except KeyboardInterrupt:
            print("Återvänder till huvudmenyn...".upper())

            

    elif menu_choice == "6":
        pass

    elif menu_choice == "7":
        print("===============================")
        print("======AVSLUTAR PROGRAMMET======".upper())
        print("===============================")
        break
    else:
        print("\nvälj en siffra mellan 1-7\n".upper())