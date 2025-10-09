
#Prints main menu, i will probably do the menu dynamic soon.
def show_main_menu():
    print("Menyval 1: Starta övervakning")
    print("Menyval 2: Lista över övervakning")
    print("Menyval 3: Skapa nya alarm")
    print("Menyval 4: Visa alarm")
    print("Menyval 5: Starta övervakningsläge")
    print("Menyval 6: Ta bort alarm")
    print("Menyval 7: Kolla alla loggar")
    print("Menyval 8: Avsluta programmet")
    print("===============================")

#Handels user input for menu choices in main menu
def main_menu_input_choice():
    while True:
        menu_choice = input("Gör ett val mellan 1-8: ")
        try:
            if 1<= int(menu_choice) <=8:
                return menu_choice
            else:
                print("välj en siffra mellan 1-8")
        except ValueError:
            print("Det måste vara en siffra")
            
#Handles the submenu for setting alarm levels
def show_alarm_menu():
        print("\nKonfigurera larm\n".upper())
        print("1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("4. Tillbaka till huvudmenyn")

#Handels user input for submenu  
def alarm_menu_input():
    while True:    
        alarm_menu_choice = input("Gör ett val mellan 1-4: ")
        try:
            choice_number = int(alarm_menu_choice)
            if 1<= choice_number <=4:
                return alarm_menu_choice
            else:
                print("välj en siffra mellan 1-4")
        except ValueError:
            print("Det måste vara en siffra")
        
def press_enter_to_continue ():
    input("Tryck enter för att fortsätta...".upper())
