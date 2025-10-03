''' Basic end assignment shell to get the structure right'''

''' the basic data-structure'''
alarms = {
    "cpu": [],
    "memory":[],
    "disk":[]
}

def show_main_menu(): #this will print the main menu
    print("1. starta övervakning")
    print("2. lista över övervakning")
    print("3. skapa alarm")
    print("4. visa alarm")
    print("5. övervakningsläge")    
    print("6. ändra och ta bort alarm")
    print("7. övervakningslogg")
    print("8. avsluta programmet")

'''general functions'''
def press_enter_to_continue():
    input("Tryck enter för att fortsätta")
def get_cpu_percent_usage():# gets CPU percent
    pass
def get_memory_percent_usage(): 
    pass
def get_disk_percent_usage():
    pass
def get_all_system_percent_usage():
    pass

'''JSON specifik functions'''
def load_alarms_from_file():
    pass
def save_alarms_to_file(alarms):
    pass
def create_log_file():
    pass
def write_to_log(message):
    pass

'''
function for validating input from user aswell as a dynamic show menu
can be reused for every menu
'''
def validate_menu_input(min_value, max_value, prompt_message):
    pass

def show_dynamic_menu(title, option):
    pass

def handle_menu(title, options):
    pass

''' thoughts about menu and menu-input functions. Can i use 1 function for each that i can reuse multiply times?'''
def main_menu_input():#this function should handle the user input 1-8 for the main menu
    pass
def create_new_alarm_menu_input():#this function should handle the user input for the submenu creat new alarm
    pass
def remove_alarm_menu_input(): # this function should handle the user input for submenu "remove alarm"
    pass


'''menu specific functions'''
def start_monitoring(): # (Menu1)this will start monitoring
    pass


def list_active_monitoring():#(menu2)This will list all the monitoring, cpu, ram, disk
    pass


def create_new_alarm_menu():#(Menu3) This will show the submenu to choose what kind of alarm to set
    pass
def create_new_alarm():#(Menu3) this will create a new alarm
    pass
def store_new_alarm():#(Menu3) this will make sure that the alarm is stored prefferably in a JSON
    pass


def show_active_alarms():#(Menu4) This will show all the active alarms
    pass


def monitoringmode_active():#(Menu5) this will start active monitoring
    pass
def check_alarms(current_stats, alarms):
    pass
def trigger_alarm_warning(alarm_type, current_value, threshold):
    pass

def remove_active_alarm_menu():#(menu6) this will show a menu for the different kind of alarms cpu, ram, disk
    pass
def remove_active_alarm():#(Menu6) this will remove an active alarm
    pass

'''for menu 7 i probably want a submenu aswell so the user can choose to show logs for either cpu, ram or disk aswell as everything'''
def alarm_log():#(menu7) this will show a logg for all the alarms
    pass


