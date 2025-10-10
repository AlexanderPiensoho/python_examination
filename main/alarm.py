import time
import psutil
import json
from log import log_event

class AlarmManager:
    '''
    init tries to load alarms from JSON-file, if no previous alarms exist it creates a empty alarm dict.
    '''
    def __init__(self):
        print("Laddar tidigare larm...")
        loaded = self.load_from_file()
        if loaded:
            self.alarms = loaded
        else:
            self.alarms = {
                "cpu": [],
                "memory": [],
                "disk":[]
            }

    #Adds alarm to dict and calls save_to_file method to store it in JSON
    def add_alarm(self, alarm_type, alarm_level):
        self.alarms[alarm_type].append(alarm_level)
        print(f"\nDitt {alarm_type} alarm är inställt på {alarm_level}%")
        self.save_to_file()

    #Should delete an alarm
    def remove_alarm(self, alarm_type, threshold):
        if threshold in self.alarms[alarm_type]:
            self.alarms[alarm_type].remove(threshold)
            print(f"Raderade {alarm_type} alarm {threshold} %")
            log_event(f"Användare_tog_bort_alarm_{alarm_type}_på_{threshold}_%")
            self.save_to_file()
            return True
        else:
            print(f"Inget {alarm_type} alarm hittades")
            return False

    #Saves alarm in JSON
    def save_to_file(self, filename = "alarms.json"):
        with open(filename, "w") as write_file:
            json.dump(self.alarms, write_file)

    #Loads file from JSON into the programs dict
    def load_from_file(self, filename = "alarms.json"):
        try:
            with open(filename, "r") as read_file:
                loaded_data = json.load(read_file)
                print("Tidigare larm har hämtats")
                return loaded_data
        except FileNotFoundError:
            return None

'''
Shows all alarms in the lists within the dict
def show_all_active_alarms (alarms):
    for key, values in alarms.items():
        print(f"{key} alarm".upper())
        for values in alarms[key]:
            print(f"{values}%")
'''

#Shows all alarms with a number before 1. cpu alarm 40% 2. cpu alarm 50% etc.
def show_all_alarms(alarms):
    counter = 1
    alarm_list = []
    for alarm_type, threshold_list in alarms.items():
        for threshold in threshold_list:
            print(f"{counter}. {alarm_type} alarm {threshold} %")
            alarm_list.append((alarm_type, threshold))
            counter +=1
    return alarm_list





