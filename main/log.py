from datetime import datetime

def log_event(message):
    timestamp = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
    log_message = f"{timestamp}_{message}"
    
    with open("monitoring.log", "a") as log_file:
        log_file.write(log_message + "\n")

#Need to add error handling if no files exists.
def print_all_logs():
    print("\n=== Loggar ===")
    with open("monitoring.log", "r") as file:
        print(file.read())