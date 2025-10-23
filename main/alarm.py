import json
from log import log_event
from menu import press_enter_to_continue, validate_input

class AlarmManager:
    '''
    AlarmManager handles all the data for the alarms, structures, JSON load and save
    init tries to load alarms from JSON-file, if no previous alarms exist it creates a empty alarm dict.
    '''
    def __init__(self):
        loaded_alarms = self.load_from_file()
        if loaded_alarms:
            print("Laddar tidigare larm...")
            self.alarms = loaded_alarms
        else:
            self.alarms = {
                "cpu":[],
                "memory":[],
                "disk":[]
            }


    def add_alarm(self, alarm_type: str, threshold: int) -> None:
        if threshold is None:
            return None
        if threshold in self.alarms[alarm_type]:
            print("\nAlarm på den nivån finns redan\n")
            return None
        else:
            self.alarms[alarm_type].append(threshold)
            print(f"\nDitt {alarm_type} alarm är inställt på {threshold}%")
            log_event(f"{alarm_type}_alarm_satt_på_{threshold}_%")
            self.save_to_file()


    def remove_alarm(self, alarm_type: str, threshold: int) -> bool:
        if threshold in self.alarms[alarm_type]:
            self.alarms[alarm_type].remove(threshold)
            print(f"\nRaderade {alarm_type} alarm {threshold} %")
            log_event(f"Användare_tog_bort_alarm_{alarm_type}_på_{threshold}_%")
            self.save_to_file()
            return True
        else: 
            print(f"Inget {alarm_type} alarm hittades")
            return False


    def save_to_file(self, filename:str = "alarms.json") -> None:
        with open(filename, "w") as write_file:
            json.dump(self.alarms, write_file, indent=4)


    def load_from_file(self, filename:str = "alarms.json") -> dict[str, list[int]] | None:
        try:
            with open(filename, "r") as read_file:
                loaded_data = json.load(read_file)
                print("Tidigare larm har hämtats")
                return loaded_data
        except FileNotFoundError:
            return None


    def get_alarm(self) -> dict[str, list[int]]:
        return self.alarms



def show_all_alarms_numbered(alarms: dict[str, list[int]]) -> list[tuple[str, int]]:
        '''
        Converts AlarmManager data (dict[str, list[int]] to list[tuple[str, int]] to show a
        numbered list for the user. easier for user to handle removing alarms)
        '''
        counter = 1
        alarm_list = []
        for alarm_type, threshold_list in alarms.items():
            for threshold in sorted(threshold_list):
                print(f"{counter}. {alarm_type} alarm {threshold} %")
                alarm_list.append((alarm_type, threshold))
                counter += 1
        return alarm_list


def user_remove_alarm(alarm_list: list[tuple[str, int]], alarm_manager: AlarmManager) -> None:
    if not alarm_list:
        print("\nInga alarm finns att ta bort\n")
        press_enter_to_continue()
        return None
    alarm_remove_choice = validate_input("Välj ett larm att ta bort", 1, len(alarm_list), 
                                         "|ctrl+c återvänder till huvudmenyn|")
    if alarm_remove_choice is None:
        print("Återvänder till huvudmenyn...")
        return None
    else:
        alarm_type, threshold = alarm_list[alarm_remove_choice -1]
        alarm_manager.remove_alarm(alarm_type, threshold)
        press_enter_to_continue()


def create_alarm_from_user(alarm_manager: AlarmManager, alarm_type: str) -> None:
    alarm_threshold = validate_input("Sätt en larmnivå mellan", 1, 100)
    alarm_manager.add_alarm(alarm_type, alarm_threshold)
    press_enter_to_continue()





