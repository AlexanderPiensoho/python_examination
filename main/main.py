from monitor import start_monitoring, get_cpu_status, get_disk_status, get_memory_status, active_monitoring
from menu import validate_input, press_enter_to_continue, show_dynamic_menu
from alarm import AlarmManager, show_all_alarms_numbered, user_remove_alarm
from log import log_event, print_current_log
from datetime import datetime

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
    current_log = datetime.now().strftime("log_start_date_%d_%m_%Y_time_%H-%M-%S.log")
    log_event("Användare_startade_programmet", current_log)
    main_menu_is_running = True
    alarm_monitoring = False
    alarm_manager = AlarmManager()
    monitoring_active = False
    while main_menu_is_running:
        show_dynamic_menu("HUVUDMENY", main_menu)
        menu_choice = validate_input(1, 8)
        #Starts monitoring. No threading, so it only turns monitoring to True.
        match menu_choice:
            case 1:
                monitoring_active = True
                start_monitoring()
                log_event("Bakgrundövervakning_startad", current_log)
                press_enter_to_continue()
            #Show status for CPU, Memory and Disk
            case 2:
                if monitoring_active:
                    print(get_cpu_status())
                    print(get_memory_status())
                    print(get_disk_status())
                    print()
                    log_event("System_status_hämtad_lyckades", current_log)
                    press_enter_to_continue()
                else:
                    log_event("System_status_hämtad_misslyckades", current_log)
                    print("❌Systemövervakning ej startad❌")
                    press_enter_to_continue()
            #Shows a submenu with 4 choices. Set alarm 1.2.3 and return main menu 4. 
            case 3:
                set_alarm_menu_is_running = True
                while set_alarm_menu_is_running:
                    show_dynamic_menu("ALARM MENY", alarm_menu)
                    alarm_menu_choice = validate_input(1, 4)
                    match alarm_menu_choice:
                        case 1:
                            alarm_threshold = validate_input(1, 100)
                            alarm_manager.add_alarm("cpu", alarm_threshold) #Adds alarm to a separet JSON file
                            log_event(f"CPU_alarm_satt_på_{alarm_threshold}_%", current_log)
                            press_enter_to_continue()

                        case 2:
                            alarm_threshold = validate_input(1, 100)
                            alarm_manager.add_alarm("memory", alarm_threshold)
                            log_event(f"memory_alarm_satt_på_{alarm_threshold}_%", current_log)
                            press_enter_to_continue()
                                        
                        case 3:
                            alarm_threshold = validate_input(1, 100)
                            alarm_manager.add_alarm("disk", alarm_threshold)
                            log_event(f"disk_alarm_satt_på_{alarm_threshold}_%", current_log)
                            press_enter_to_continue()

                        case 4:
                            set_alarm_menu_is_running = False
                            print("\nDu skickas tillbaka till huvudmenyn".upper())
                            log_event("Användaren_återvände_till_huvudmenyn", current_log)
                            
            #Shows all alarms that is stored within the JSON
            case 4:
                show_all_alarms_numbered(alarm_manager.alarms)
                log_event("Visade_alla_aktiva_alarm", current_log)
                press_enter_to_continue()
            #Starts active monitoring and calls out alarms when triggered.     
            case 5:
                log_event("Startade_aktiv_övervakning", current_log)
                active_monitoring(alarm_monitoring, alarm_manager.alarms, current_log)
            #Here you will be able to remove alarms from the JSON 
            #Need to fix this to make it prettier
            case 6:
                alarm_list = show_all_alarms_numbered(alarm_manager.alarms)
                user_remove_alarm(alarm_list, alarm_manager)
                
            #Reads all logging
            case 7:
                print_current_log(current_log)
                press_enter_to_continue()
            #Exits program
            case 8:
                print("="*40)
                print("AVSLUTAR PROGRAMMET".center(40))
                print("="*40)
                log_event("Användare_avslutade_programmet", current_log)
                break


if __name__ == "__main__":
    main()