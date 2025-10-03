from menu import handle_menu, press_enter_to_continue

alarms_storage = {
    "cpu": [],
    "memory":[],
    "disk":[]
}
main_menu = {
        "1": "Starta övervakning",
        "2": "Lista över övervakning",
        "3": "Skapa alarm",
        "4": "Visa alarm",
        "5": "Övervakningsläge",
        "6": "Ta bort alarm",
        "7": "Visa logg",
        "8": "Avsluta programmet"
        }
alarm_menu = {
    "1": "CPU",
    "2": "RAM-Minne",
    "3": "DISK",
    "4": "Tillbaka till huvudmenyn"
}

start_up_monitoring = False
main_menu_is_running = True
while main_menu_is_running:
    menu_choice = handle_menu("HUVUDMENY", main_menu)

    if menu_choice == "1":
        start_up_monitoring = True
        print("Övervakning påbörjad")
        press_enter_to_continue()
    if menu_choice == "2":
        print("då")
        press_enter_to_continue()
    if menu_choice == "3":
        print("tjabba")
        press_enter_to_continue()
    if menu_choice == "4":
        print("44")
        press_enter_to_continue()
    if menu_choice == "5":
        print("55")
        press_enter_to_continue()
    if menu_choice == "6":
        print("66")
        press_enter_to_continue()
    if menu_choice == "7":
        print("77")
        press_enter_to_continue
    if menu_choice == "8":
        print("Avslutar programmet")
        break


    




