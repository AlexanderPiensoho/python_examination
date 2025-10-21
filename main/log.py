from datetime import datetime
current_log = datetime.now().strftime("log_start_date_%d_%m_%Y_time_%H-%M-%S.log")

def log_event(message: str) -> None:
    timestamp = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
    log_message = f"{timestamp}_{message}"
    
    with open(current_log, "a") as log_file:
        log_file.write(log_message + "\n")


def print_current_log() -> None:
    try:
        print(f"\n{'='*40}")
        print("Loggar".center(40))
        print(f"{'='*40}")
        with open(current_log, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Det finns inga loggar sparade")