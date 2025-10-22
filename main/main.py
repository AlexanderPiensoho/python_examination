from monitor import start_monitoring, print_system_status, active_monitoring, print_no_monitoring_active
from menu import validate_input, press_enter_to_continue, show_dynamic_menu, exit_program, leave_alarm_menu
from alarm import AlarmManager, user_remove_alarm, create_alarm_from_user, show_all_alarms_numbered
from log import log_event, print_current_log

main_menu ={
    1: "Starta övervakning",
    2: "Lista över övervakning",
    3: "Skapa nya alarm",
    4: "Visa alarm",
    5: "Starta övervakningsläge",
    6: "Ta bort alarm",
    7: "Kolla alla loggar",
    8: "Avsluta programmet"
}
alarm_menu = {
    1: "CPU",
    2: "RAM-Minne",
    3: "DISK",
    4: "Tillbaka till huvudmenyn"
}
alarm_type_choices = {
    1: "cpu",
    2: "memory",
    3: "disk"
    }

def main() -> None:
    '''
    This program can get system statuses, set/delete/show alarms
    and monitor the alarms against the cumputers current thresholds
    and logs everything that happens per program-run
    '''
    log_event("Användare_startade_programmet")
    main_menu_is_running = True
    monitoring_active = False
    alarm_manager = AlarmManager()
    while main_menu_is_running:
        show_dynamic_menu("HUVUDMENY", main_menu)
        main_choice = validate_input("Gör ett menyval mellan", 1, len(main_menu))

        match main_choice:
            case 1:
                monitoring_active = start_monitoring()

            case 2:
                if not monitoring_active:
                    print_no_monitoring_active()
                else:
                    print_system_status()

            case 3:
                alarm_menu_running = True
                while alarm_menu_running:
                    show_dynamic_menu("LARM MENY", alarm_menu)
                    alarm_choice = validate_input("Gör ett menyval mellan", 1, len(alarm_menu))
                    match alarm_choice:
                        case 1 | 2 | 3:
                            create_alarm_from_user(alarm_manager, alarm_type_choices[alarm_choice])

                        case 4: 
                            alarm_menu_running = leave_alarm_menu()

            case 4:
                show_all_alarms_numbered(alarm_manager.get_alarm())
                press_enter_to_continue()
    
            case 5: 
                if not monitoring_active:
                    print_no_monitoring_active()
                else:
                    active_monitoring(alarm_manager.get_alarm())

            case 6:
                alarm_list = show_all_alarms_numbered(alarm_manager.get_alarm())
                user_remove_alarm(alarm_list, alarm_manager)
                
            case 7:
                print_current_log()
                press_enter_to_continue()

            case 8:
                main_menu_is_running = exit_program()

if __name__ == "__main__":
    main()