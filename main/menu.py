
#Show menu dynamicly, either main menu or submenu. most of the prints are only fanzy stuff.
def show_dynamic_menu(title: str, option: dict[str, str]):
    print(f"\n{'='*40}")
    print(f"{title.center(40)}")
    print(f"{'='*40}")
    for key in option.keys():
        print(f"{key}. {option[key]}")
    print(f"{"="*40}")


def validate_input(min_value, max_value):
    while True:
        input_message = input(f"Gör ett val mellan {min_value}-{max_value}: ")
        try:
            choice_number = int(input_message)
            if min_value <= choice_number <= max_value:
                return choice_number
            else:
                print(f"Välj en siffra mellan {min_value}-{max_value}!")
        except ValueError:
            print("Felaktigt värde, det måste vara en siffra")
        
def press_enter_to_continue():
    input("Tryck enter för att fortsätta...".upper())

def exit_program(log_event, current_log):
    print("="*40)
    print("AVSLUTAR PROGRAMMET".center(40))
    print("="*40)
    log_event("Användare_avslutade_programmet", current_log)
    return False
