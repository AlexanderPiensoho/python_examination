import psutil
import json
#Create alarm, delete alarms, 
class AlarmManager:
    def __init__(self, alarms):
        self.alarms = alarms

    def add_alarm(self, alarm_type, alarm_level):
        self.alarms[alarm_type].append(alarm_level)
        print(f"\nDitt {alarm_type} alarm är inställt på {alarm_level}%")

    def save_to_file(self):
        pass

#et_cpu_alarm = AlarmManager()
#int(input(set_cpu_alarm.add_alarm("cpu", "set alarm: ")))
#type_of_alarm_input = input("Vilket typ av larm vill du ställa in? ")
#new_alarm_level_input = input("Ställ in en procentsats mellan 0-100: ")

    
    
    

