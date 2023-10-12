import tkinter as tk
import json

def add_subject(day, subject, time):
    schedule[time][day] = subject
    update_schedule_display()

def update_schedule_display():
    for day in days_of_week:
        for time_slot in time_slots:
            subject = schedule[time_slot][day]
            subject_entries[(day, time_slot)].delete(0, tk.END)
            subject_entries[(day, time_slot)].insert(0, subject)

def update_schedule_from_json():
    with open("schedule.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    for day in days_of_week:
        for time_slot in time_slots:
            subject = data.get(day, {}).get(time_slot, "")
            add_subject(day, subject, time_slot)
    update_schedule_display()

# Create the main window
root = tk.Tk()
root.geometry("1200x800+100+100")
root.title("Thời Khóa Biểu Học Tập")

# Create a table for the schedule
days_of_week = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
time_slots = ["7h-8h", "8h-9h", "9h-10h", "10h-11h", "11h-12h", "12h-13h", "13h-14h", "14h-15h", "15h-16h", "16h-17h", "17h-18h"]

schedule = {time: {day: "" for day in days_of_week} for time in time_slots}
subject_entries = {(day, time_slot): None for day in days_of_week for time_slot in time_slots}

for i, day in enumerate(days_of_week):
    tk.Label(root, text=day).grid(row=0, column=i+1)
    for j, time_slot in enumerate(time_slots):
        entry = tk.Entry(root, width=20)
        entry.grid(row=j+1, column=i+1)
        subject_entries[(day, time_slot)] = entry

for j, time_slot in enumerate(time_slots):
    tk.Label(root, text=time_slot).grid(row=j+1, column=0)

# Create a button to update the schedule from a JSON file
update_button = tk.Button(root, text="Cập nhật Thời Khóa Biểu", command=update_schedule_from_json)
update_button.grid(row=len(time_slots) + 1, column=1, columnspan=5)

frame = tk.Frame(root)
frame.grid(row=len(time_slots) + 2, column=1, columnspan=5)

subject_label = tk.Label(frame, text="Môn học:")
subject_label.grid(row=0, column=0, padx=10, pady=10)

subject_entry = tk.Entry(frame)
subject_entry.grid(row=0, column=1, padx=10, pady=10)

time_label = tk.Label(frame, text="Thời gian:")
time_label.grid(row=0, column=2, padx=10, pady=10)

time_combobox = tk.StringVar(value=time_slots[0])
time_combobox_widget = tk.OptionMenu(frame, time_combobox, *time_slots)
time_combobox_widget.grid(row=0, column=3, padx=10, pady=10)

day_label = tk.Label(frame, text="Thứ:")
day_label.grid(row=0, column=4, padx=10, pady=10)

day_combobox = tk.StringVar(value=days_of_week[0])
day_combobox_widget = tk.OptionMenu(frame, day_combobox, *days_of_week)
day_combobox_widget.grid(row=0, column=5, padx=10, pady=10)

add_button = tk.Button(frame, text="Thêm Môn Học", command=lambda: add_subject(day_combobox.get(), subject_entry.get(), time_combobox.get()))
add_button.grid(row=0, column=6, padx=10, pady=10)

# Open the window
root.mainloop()
