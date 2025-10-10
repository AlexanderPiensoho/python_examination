from monitor import start_monitoring, get_cpu_status, get_disk_status, get_memory_status, is_alarm_monitoring
from menu import validate_menu_input, press_enter_to_continue, show_dynamic_menu
from alarm import show_all_active_alarms, AlarmManager, alarm_percent_input, show_all_alarms_numbered
from log import log_event
#Main_menu var used for show_dynamic_menu function
main_menu ={
    "Menyval 1": "Starta övervakning",
    "Menyval 2": "Lista över övervakning",
    "Menyval 3": "Skapa nya alarm",
    "Menyval 4": "Visa alarm",
    "Menyval 5": "Starta övervakningsläge",
    "Menyval 6": "Ta bort alarm",
    "Menyval 7": "Kolla alla loggar",
    "Menyval 8": "Avsluta programmet"
}
#alarm_menu var used for show_dynamic_menu function
alarm_menu = {
    "1": "CPU",
    "2": "RAM-Minne",
    "3": "DISK",
    "4": "Tillbaka till huvudmenyn"
}

#Main program starts here
def main():
    log_event("Användare_startade_programmet")
    main_menu_is_running = True
    alarm_monitoring = False
    alarm_manager = AlarmManager()
    monitoring_active = False
    while main_menu_is_running:
        show_dynamic_menu("HUVUDMENY", main_menu)
        menu_choice = validate_menu_input(1, 8)
        #Starts monitoring. No threading, so it only turns monitoring to True.
        if menu_choice == "1":
            monitoring_active = True
            start_monitoring()
            log_event("Bakgrundövervakning_startad")
            press_enter_to_continue()
        #Show status for CPU, Memory and Disk
        elif menu_choice == "2":
            if monitoring_active:
                print(get_cpu_status())
                print(get_memory_status())
                print(get_disk_status())
                log_event("System_status_hämtad_lyckades")
                press_enter_to_continue()
            else:
                log_event("System_status_hämtad_misslyckades")
                print("❌Systemövervakning ej startad❌")
        #Shows a submenu with 4 choices. Set alarm 1.2.3 and return main menu 4. 
        elif menu_choice == "3":
            set_alarm_menu_is_running = True
            while set_alarm_menu_is_running:
                show_dynamic_menu("ALARM MENY", alarm_menu)
                alarm_menu_choice = validate_menu_input(1, 4)
                if alarm_menu_choice == "1":
                    alarm_threshold = alarm_percent_input()
                    alarm_manager.add_alarm("cpu", alarm_threshold) #Adds alarm to a separet JSON file
                    log_event(f"CPU_alarm_satt_på_{alarm_threshold}_%")

                elif alarm_menu_choice == "2":
                    alarm_threshold = alarm_percent_input()
                    alarm_manager.add_alarm("memory", alarm_threshold)
                    log_event(f"memory_alarm_satt_på_{alarm_threshold}_%")
                                
                elif alarm_menu_choice == "3":
                    alarm_threshold = alarm_percent_input()
                    alarm_manager.add_alarm("disk", alarm_threshold)
                    log_event(f"disk_alarm_satt_på_{alarm_threshold}_%")

                elif alarm_menu_choice == "4":
                    set_alarm_menu_is_running = False
                    print("\nDu skickas tillbaka till huvudmenyn".upper())
                    log_event("Användaren_återvände_till_huvudmenyn")
                    
        #Shows all alarms that is stored within the JSON
        elif menu_choice == "4":
            show_all_active_alarms(alarm_manager.alarms)
            log_event("Visade_alla_aktiva_alarm")
            press_enter_to_continue()
        #Starts active monitoring and calls out alarms when triggered.      
        elif menu_choice == "5":
            log_event("Startade_aktiv_övervakning")
            is_alarm_monitoring(alarm_monitoring, alarm_manager.alarms)
        #Here you will be able to remove alarms from the JSON 
        elif menu_choice == "6":
            alarm_list = show_all_alarms_numbered(alarm_manager.alarms)
            alarm_remove_choice = int(input("Vilket alarm vill du ta bort?: "))#Needs error handling
            idx = alarm_remove_choice -1
            alarm_type, threshold = alarm_list[idx]
            alarm_manager.remove_alarm(alarm_type, threshold)
            press_enter_to_continue()
        #Reads all logging
        elif menu_choice == "7":
            print("\n=== Loggar ===")
            with open("monitoring.log", "r") as f:
                print(f.read())
            press_enter_to_continue()
        #Exits program
        elif menu_choice == "8":
            print("===============================")
            print("======AVSLUTAR PROGRAMMET======".upper())
            print("===============================")
            log_event("Användare_avslutade_programmet")
            break


if __name__ == "__main__":
    main()