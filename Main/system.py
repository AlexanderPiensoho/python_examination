from monitor import start_monitoring, show_monitoring
import psutil
import time
alarms = {
    "cpu": [],
    "memory": [],
    "disk": []
}

main_menu_is_running = True
set_alarm_menu_is_running = False
monitoring_active = False
alarm_monitoring = False

print("==Välkommen till huvudmenyn==".upper())

while main_menu_is_running:
    print("Menyval 1: Starta övervakning")
    print("Menyval 2: Lista över övervakning")
    print("Menyval 3: Skapa nya alarm")
    print("Menyval 4: Visa alarm")
    print("Menyval 5: Starta övervakningsläge")
    print("Menyval 6: Ta bort alarm")
    print("Menyval 7: Avsluta programmet")
    menu_choice = input("Gör ett menyval mellan 1-7: ")

    if menu_choice == "1":
        monitoring_active = True
        start_monitoring()
        print("\n🕵️ Övervakning startad 🕵️\n".upper())
        input("Tryck enter för att komma tillbaka till menyn...")

    elif menu_choice == "2":
        if not monitoring_active:
            print("\n❌ Ingen övervakning aktiv ❌\n".upper())
        else:
            print()
            show_monitoring()
            print()
            input("Tryck enter för att komma tillbaka till menyn...")
    elif menu_choice == "3":
        set_alarm_menu_is_running = True
        print("\n Konfigurera larm\n".upper())
        print("1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("4. Tillbaka till huvudmenyn")
        alarm_menu_choice = input("Välj ett alternativ mellan 1-4: ")

        if alarm_menu_choice == "1":
            cpu_alarm = int(input("Ställ in en nivå för CPU alarm, mellan 0-100%: "))
            alarms["cpu"].append(cpu_alarm)
            print(f"Ditt CPU alarm är inställt på {cpu_alarm}%\n")
        elif alarm_menu_choice == "2":
            memory_alarm = int(input("Ställ in en nivå för ditt RAM-minne alarm, mellan 0-100%: "))
            alarms["memory"].append(memory_alarm)
            print(f"Ditt RAM-minne alarm är inställt på {memory_alarm}%\n")
        elif alarm_menu_choice == "3":
            disk_alarm = int(input("Ställ in en nivå för ditt Disk-minne alarm, mellan 0-100%: "))
            alarms["disk"].append(disk_alarm)
            print(f"Ditt disk-minne alarm är inställt på {disk_alarm}%\n")
        elif alarm_menu_choice == "4":
            print("\nDu skickas tillbaka till huvudmenyn\n".upper())
            set_alarm_menu_is_running = False
        else:
            print("Du måste välja en siffra mellan 1-4")
      

    elif menu_choice == "4":  
        print(f"\nCPU alarm: {alarms["cpu"]}%".upper())
        print(f"RAM-minne alarm: {alarms["memory"]}%".upper())
        print(f"Disk-minne alarm: {alarms["disk"]}%\n".upper())
        input("Tryck enter för att komma tillbaka till menyn...")
    elif menu_choice == "5":
        alarm_monitoring = True
        while alarm_monitoring:
            print("Aktiv övervakning pågår")
            time.sleep(0.5)
            for alarm in alarms["cpu"]:
                if int(psutil.cpu_percent(interval=1)) >= int(alarm):
                    print("Varning")
            for alarm in alarms["memory"]:
                if int(psutil.virtual_memory()) >= int(alarm):
                    print("Varning")
            for alarm in alarms["disk"]:
                if int(psutil.disk_usage()) >= int(alarm):
                    print("Varning")

            '''
            if alarms["cpu"] == []:
                print("VARNING!! CPU")
                time.sleep(1)
            elif alarms["memory"] == []:
                print("VARNING!! RAM-MINNE")
                time.sleep(1)
            elif alarms["disk"] == []:
                print("VARNING!! DISK-MINNE")
                time.sleep(1)
            else:
                continue
                '''
    elif menu_choice == "6":
        pass
    elif menu_choice == "7":
        print("\n===AVSLUTAR PROGRAMMET===\n".upper())
        break
    else:
        print("\nvälj en siffra mellan 1-7\n".upper())