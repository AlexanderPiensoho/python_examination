from datetime import datetime

def log_event(message, current_log):
    timestamp = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
    log_message = f"{timestamp}_{message}"
    
    with open(current_log, "a") as log_file:
        log_file.write(log_message + "\n")

#Need to add error handling if no files exists.
def print_current_log(current_log):
    try:
        print("\n=== Loggar ===")
        with open(current_log, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Det finns inga loggar sparade")