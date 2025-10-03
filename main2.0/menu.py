''' this file is for all menu related functions'''

#This is the main function for our menus in the program
def handle_menu(title, options):
    show_dynamic_menu(title, options)
    max_choice = max([int(key) for key in options.keys()])
    return validate_menu_input(1, max_choice, f"Välj 1-{max_choice}: ")

#Handles input, used within handle_menu function
def validate_menu_input(min_value, max_value, prompt_message):
    while True:
        try:
            choice = int(input(prompt_message))
            if min_value <= choice <=max_value:
                return str(choice)
            else:
                print(f"Välj en siffra mellan {min_value}-{max_value}")
        except ValueError:
            print("Det måste vara en siffra")

#Show a menu that is called upon - used within handle_menu function
def show_dynamic_menu(title, option):
    print(f"\n{'='*40}")
    print(f"{title.center(40)}")
    print(f"{'='*40}")
    for key in sorted(option.keys()):
        print(f"{key}. {option[key]}")
    print(f"{"="*40}")

def press_enter_to_continue():
    input("Tryck enter för att fortsätta")



        
    