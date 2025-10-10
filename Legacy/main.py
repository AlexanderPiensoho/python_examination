import psutil
from menu import handle_menu, press_enter_to_continue
from monitoring import get_cpu_status, get_disk_status, get_memory_status
from alarms import AlarmManager

alarms_storage = {
    "cpu": [],
    "memory":[],
    "disk":[]
}
main_menu = {
        "1": "Starta övervakning",
        "2": "Lista över övervakning",
        "3": "Skapa alarm",
        "4": "Visa alarm",
        "5": "Övervakningsläge",
        "6": "Ta bort alarm",
        "7": "Visa logg",
        "8": "Avsluta programmet"
        }
alarm_menu = {
    "1": "CPU",
    "2": "RAM-Minne",
    "3": "DISK",
    "4": "Tillbaka till huvudmenyn"
}

start_up_monitoring = False
main_menu_is_running = True
alarm_manager = AlarmManager(alarms_storage)
while main_menu_is_running:
    menu_choice = handle_menu("HUVUDMENY", main_menu)

    if menu_choice == "1":
        start_up_monitoring = True
        print("Övervakning påbörjad")
        press_enter_to_continue()
        
    elif menu_choice == "2":
        if start_up_monitoring == True:
            print(get_cpu_status())
            print(get_memory_status())
            print(get_disk_status())
            press_enter_to_continue()
        else:
            print("❌Systemövervakning ej startad❌")

    elif menu_choice == "3":
        alarm_menu_choice = handle_menu("ALARM MENY", alarm_menu)
        alarm_level_choice = input("Välj larmnivå mellan 1-100: ") # felhantering/validering
        if alarm_menu_choice == "1":#CPU menu choice
            alarm_manager.add_alarm("cpu", alarm_level_choice)
        elif alarm_menu_choice == "2":# Memory menu choice
            alarm_manager.add_alarm("memory", alarm_level_choice)
        elif alarm_menu_choice == "3":# DISK menu choice
            alarm_manager.add_alarm("disk", alarm_level_choice)
        elif alarm_menu_choice == "4":# Return to main menu
            break
        press_enter_to_continue()
    elif menu_choice == "4":
        print("44")
        press_enter_to_continue()
    elif menu_choice == "5":
        print("55")
        press_enter_to_continue()
    elif menu_choice == "6":
        print("66")
        press_enter_to_continue()
    elif menu_choice == "7":
        print("77")
        press_enter_to_continue
    elif menu_choice == "8":
        print("Avslutar programmet")
        break


    




