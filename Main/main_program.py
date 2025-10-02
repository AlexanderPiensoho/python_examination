from monitor_functions import start_monitoring, show_monitoring
from menu_functions import show_main_menu, main_menu_input_choice, show_alarm_menu, set_alarm_choice, press_enter_to_continue
from alarm import show_all_active_alarms, is_alarm_monitoring

import psutil
import time
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

#pre-defined values beacuse of testing. 
alarms = {
    "cpu": [2, 10, 40],
    "memory": [2,30, 40],
    "disk": [2]
}

set_alarm_menu_is_running = False
main_menu_is_running = True
monitoring_active = False
alarm_monitoring = False

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
            if not monitoring_active:
                print("\n❌ Ingen övervakning aktiv ❌\n".upper())
            else:
                print()
                show_monitoring()
                print()
                press_enter_to_continue()

        elif menu_choice == "3":
            set_alarm_menu_is_running = True
            while set_alarm_menu_is_running:
                show_alarm_menu()
                alarm_menu_choice = set_alarm_choice()
                if alarm_menu_choice == "1":
                    set_alarm("cpu", "Ställ in CPU alarm, menllan 0-100: ")

                elif alarm_menu_choice == "2":
                    set_alarm("memory", "Ställ in ditt RAM alarm, mellan 0-100: ")
                            
                elif alarm_menu_choice == "3":
                    set_alarm("disk", "Ställ in ditt disk alarm, mellan 0-100: ")

                elif alarm_menu_choice == "4":
                    print("\nDu skickas tillbaka till huvudmenyn".upper())
                    set_alarm_menu_is_running = False
                else:
                    print("Du måste välja en siffra mellan 1-4")
            
        elif menu_choice == "4":
            show_all_active_alarms(alarms)
            press_enter_to_continue()
            
        elif menu_choice == "5":
            is_alarm_monitoring(alarm_monitoring, alarms)
            
        elif menu_choice == "6":
            pass

        elif menu_choice == "7":
            print("===============================")
            print("======AVSLUTAR PROGRAMMET======".upper())
            print("===============================")
            break
        else:
            print("\nvälj en siffra mellan 1-7\n".upper())

if __name__ == "__main__":
    main()