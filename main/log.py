from datetime import datetime
'''
log-testing right now before i put it in the program.
'''
def log_event(message):
    timestamp = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
    log_message = f"{timestamp}_{message}"
    
    with open("monitoring.log", "a") as log_file:
        log_file.write(log_message + "\n")
