from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
import time

def set_time():
    time = datetime.now().strftime("%H:%M:%S")
    ms = (datetime.now().strftime("%f"))[0:3]   # we need to separate milliseconds from microseconds
    return time+":"+str(ms)

def set_date():
    return datetime.now().strftime("%d/%m")

def weekday():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[datetime.now().weekday()]

current_date = set_date()
current_time = set_time()
date_now = str(weekday())+", "+str(set_date())

window = Tk()
window.title("Anxiety Inducing Clock")

window.geometry("400x300")

def update_all():
    lbl_time.configure(text=set_time())
    lbl_date.configure(text=date_now)
    lbl_meal.configure(text=meal_message)
    lbl_time.after(1, update_all)

def meal():
    hours = int(datetime.now().strftime("%H"))
    if hours == 9:
        return "Good morning!"
    elif hours == 8:
        return "Nice and early!"
    elif hours == 10:
        return "Cuppa?"
    elif hours == 11:
        return "Lunch soon..."
    elif hours == 12:
        return "Lunch is allowed"
    elif hours == 13:
        return "Lunch break!"
    elif hours == 14:
        return "How was lunch?"
    elif hours == 15:
        return "Cuppa?"
    elif hours == 16:
        return "Home soon, I hope!"
    elif hours == 17:
        return "Go home!"
    else:
        return "Life is fleeting"
    
meal_message = meal()

lbl_time = Label(window, text=current_time, font=("Arial Black", 40), bg = "black", fg = "yellow", width = 400, height = 1)

lbl_time.pack(anchor = "n")

lbl_date = Label(window, text=date_now, font = ("Arial Black", 30), bg = "black", fg = "yellow", width = 400, height = 2)
lbl_date.pack(anchor = "center")
lbl_meal = Label(window, text=meal_message, font = ("Arial Black", 20), bg = "black", fg = "yellow", width = 400, height = 3)
lbl_meal.pack(anchor = "s")

update_all()    
window.mainloop()



