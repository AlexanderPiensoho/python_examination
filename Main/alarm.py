alarms = {
    "cpu": [2, 10, 40],
    "memory": [2,30, 40],
    "disk": [2]
}

def show_all_active_alarms ():
    for key in alarms.keys():
        print(f"{key} alarm".upper())
        for alarm_value in alarms[key]:
            print(f"{alarm_value}%")
    input("Tryck enter för att komma tillbaka till menyn...".upper())


