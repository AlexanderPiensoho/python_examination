import time
import psutil
import json

class AlarmManager:
    def __init__(self):
        loaded = self.load_from_file()
        if loaded:
            self.alarms = loaded
            print("Loaded from previous alarms")
        else:
            self.alarms = {
                "cpu": [],
                "memory": [],
                "disk":[]
            }

    def add_alarm(self, alarm_type, alarm_level):
        self.alarms[alarm_type].append(alarm_level)
        print(f"\nDitt {alarm_type} alarm är inställt på {alarm_level}%")
        self.save_to_file()

    def save_to_file(self, filename = "alarms.json"):
        with open(filename, "w") as write_file:
            json.dump(self.alarms, write_file)

    def load_from_file(self, filename = "alarms.json"):
        try:
            with open(filename, "r") as read_file:
                loaded_data = json.load(read_file)
                return loaded_data
        except FileNotFoundError:
            print("Filen hittas inte")
            return None


def alarm_percent_input(): #Hanterar användarens menyval för alarm menyn
    alarm_menu_choice = input("Gör ett val mellan 1-100: ")
    try:
        choice_number = int(alarm_menu_choice)
        if 1<= choice_number <=100:
            return int(alarm_menu_choice)
        else:
            print("välj en siffra mellan 1-100")
    except ValueError:
        print("Det måste vara en siffra")

def show_all_active_alarms (alarms):
    for key, values in alarms.items():
        print(f"{key} alarm".upper())
        for alarm_value in alarms[key]:
            print(f"{alarm_value}%")






