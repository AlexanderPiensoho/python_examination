from monitor import start_monitoring, get_cpu_status, get_disk_status, get_memory_status, is_alarm_monitoring
from menu import show_main_menu, main_menu_input_choice, show_alarm_menu, alarm_menu_input, press_enter_to_continue
from alarm import show_all_active_alarms, AlarmManager, alarm_percent_input
import json
#import psutil
#import time
# Set_alarm funktion, för jag får den inte att fungera i annan fil pga alarms dict ligger här
def set_alarm(alarm_type, input_message):
    while True:
        try:
            alarm_value = int(input(input_message))
            if 0<= alarm_value <=100:
                alarms[alarm_type].append(alarm_value)
                print(f"\nDitt {alarm_type} alarm är inställt på {alarm_value}%".upper())
                press_enter_to_continue()
                break
            else:
                print("Siffran måste vara mellan 0-100")
        except ValueError: 
            print("Felaktigt värde, det måste vara en siffra mellan 0-100")

'''pre-defined values beacuse of testing. 
alarms = {
    "cpu": [2, 10, 40],
    "memory": [2,30, 40],
    "disk": [2]
}
'''

set_alarm_menu_is_running = False
main_menu_is_running = True
monitoring_active = False
alarm_monitoring = False
alarm_manager = AlarmManager()
saved_alarms = alarm_manager.load_from_file()


print("=================================")
print("====Välkommen till huvudmenyn====".upper())
print("=================================")

def main():
    while main_menu_is_running:
        show_main_menu()
        menu_choice = main_menu_input_choice()

        if menu_choice == "1":
            monitoring_active = True
            start_monitoring()
            press_enter_to_continue()

        elif menu_choice == "2":
            if monitoring_active:
                print(get_cpu_status())
                print(get_memory_status())
                print(get_disk_status())
                press_enter_to_continue()
            else:
                print("❌Systemövervakning ej startad❌")

        elif menu_choice == "3":
            set_alarm_menu_is_running = True
            while set_alarm_menu_is_running:
                show_alarm_menu()
                alarm_menu_choice = alarm_menu_input()
                if alarm_menu_choice == "1":
                    alarm_threshold = alarm_percent_input()
                    alarm_manager.add_alarm("cpu", alarm_threshold)

                elif alarm_menu_choice == "2":
                    alarm_threshold = alarm_percent_input()
                    print(f"DEBUG: alarm_threshold = {alarm_threshold}, type = {type(alarm_threshold)}")
                    alarm_manager.add_alarm("memory", alarm_threshold)
                                
                elif alarm_menu_choice == "3":
                    alarm_threshold = alarm_percent_input()
                    alarm_manager.add_alarm("disk", alarm_threshold)

                elif alarm_menu_choice == "4":
                    set_alarm_menu_is_running = False
                    print("\nDu skickas tillbaka till huvudmenyn".upper())
                    

        elif menu_choice == "4":
            show_all_active_alarms(alarm_manager.alarms)
            press_enter_to_continue()
            
        elif menu_choice == "5":
            is_alarm_monitoring(alarm_monitoring, alarm_manager.alarms)
            
        elif menu_choice == "6":
            pass

        elif menu_choice == "7":
            print("===============================")
            print("======AVSLUTAR PROGRAMMET======".upper())
            print("===============================")
            break


if __name__ == "__main__":
    main()