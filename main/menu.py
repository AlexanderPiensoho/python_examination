from log import log_event

def show_dynamic_menu(title: str, options: dict[int, str]) -> None:
    print(f"\n{'='*40}")
    print(title.center(40))
    print("="*40)
    for key, value in options.items():
        print(f"{key}. {value}")
    print("="*40)


def validate_input(message: str, min_value: int, max_value: int, optional_message: str = "") -> int | None:
    while True:
        try:
            input_message = input(f"{message} {min_value}-{max_value}{optional_message}: ")
            choice_number = int(input_message)
            if min_value <= choice_number <= max_value:
                return choice_number
            else:
                print(f"Välj en siffra mellan {min_value}-{max_value}!")
        except ValueError:
            print("Felaktigt värde, det måste vara en siffra")
        except KeyboardInterrupt:
            print("Avbruten av användaren...")
            return None

        
def press_enter_to_continue() -> None:
    try:
        input("\nTryck enter för att fortsätta...\n")
    except KeyboardInterrupt:
        return None

def leave_alarm_menu() -> bool:
    print("\nDu skickas tillbaka till huvudmenyn\n")
    log_event("Användaren_återvände_till_huvudmenyn")
    return False

def exit_program() -> bool:
    print("="*40)
    print("AVSLUTAR PROGRAMMET".center(40))
    print("="*40)
    log_event("Användare_avslutade_programmet")
    return False

