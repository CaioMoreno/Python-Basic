# Write your solution here
from datetime import *

name=input("Filename: ")

info = []
total_minutes=0

with open(name, "w") as file:

    start_date=input("Starting date: ")
    h_days=int(input("How many days: "))
    day=datetime.strptime(start_date, "%d.%m.%Y")
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    s_day=day+timedelta(days=h_days-1)
    file.write(f"Time period: {day.strftime("%d.%m.%Y")}-{s_day.strftime("%d.%m.%Y")}\n")

    for i in range(h_days):

        w_day=day+timedelta(days=i)
        screen_time=input(f"Screen time {w_day.strftime("%d.%m.%Y")}: ")
        minutes=screen_time.split()
        total_minutes=int(minutes[0])+int(minutes[1])+int(minutes[2])+total_minutes
        a_minutes=total_minutes/h_days
        info.append(f"{w_day.strftime("%d.%m.%Y")}: {minutes[0]}/{minutes[1]}/{minutes[2]}")

    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {a_minutes:.1f}\n")
    for i in range(h_days):
        file.write(f"{info[i]}\n")
    print(f"Data stored in file {name}")