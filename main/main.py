from monitor import start_monitoring, print_system_status, active_monitoring
from menu import validate_input, press_enter_to_continue, show_dynamic_menu, exit_program
from alarm import AlarmManager, user_remove_alarm, create_alarm_from_user, show_all_alarms_numbered
from log import log_event, print_current_log
from datetime import datetime

main_menu ={
    "1": "Starta övervakning",
    "2": "Lista över övervakning",
    "3": "Skapa nya alarm",
    "4": "Visa alarm",
    "5": "Starta övervakningsläge",
    "6": "Ta bort alarm",
    "7": "Kolla alla loggar",
    "8": "Avsluta programmet"
}

alarm_menu = {
    "1": "CPU",
    "2": "RAM-Minne",
    "3": "DISK",
    "4": "Tillbaka till huvudmenyn"
}


def main():
    current_log = datetime.now().strftime("log_start_date_%d_%m_%Y_time_%H-%M-%S.log")
    log_event("Användare_startade_programmet", current_log)
    main_menu_is_running = True
    monitoring_active = False
    alarm_manager = AlarmManager()
    while main_menu_is_running:
        show_dynamic_menu("HUVUDMENY", main_menu)
        main_choice = validate_input(1, 8)

        match main_choice:
            case 1:
                monitoring_active = start_monitoring()
                log_event("Bakgrundövervakning_startad", current_log)
                press_enter_to_continue()

            case 2:
                #Checks if monitoring is started before listing system status
                if monitoring_active:
                    print_system_status(current_log)
                else:
                    log_event("System_status_hämtad_misslyckades", current_log)
                    print("❌Systemövervakning ej startad❌")
                    press_enter_to_continue()

            case 3:
                alarm_menu_running = True
                while alarm_menu_running:
                    show_dynamic_menu("ALARM MENY", alarm_menu)
                    alarm_choice = validate_input(1, 4)
                    match alarm_choice:
                        case 1 | 2 | 3:
                            alarm_type = {1: "cpu", 2: "memory", 3: "disk"}
                            create_alarm_from_user(alarm_manager, alarm_type[alarm_choice], current_log)

                        case 4: 
                            alarm_menu_running = False
                            print("\nDu skickas tillbaka till huvudmenyn".upper())
                            log_event("Användaren_återvände_till_huvudmenyn", current_log)

            case 4:
                show_all_alarms_numbered(alarm_manager.get_alarm())
                log_event("Visade_alla_aktiva_alarm", current_log)
                press_enter_to_continue()
    
            case 5:
                #Enter active monitoring mode that check current status against the set alarms, only trigger the highest.
                log_event("Startade_aktiv_övervakning", current_log)
                active_monitoring(alarm_manager.alarms, monitoring_active, current_log)

            case 6:
                alarm_list = show_all_alarms_numbered(alarm_manager.get_alarm())
                user_remove_alarm(alarm_list, alarm_manager, current_log)
                
            case 7:
                print_current_log(current_log)
                press_enter_to_continue()

            case 8:
                main_menu_is_running = exit_program(log_event, current_log)

if __name__ == "__main__":
    main()