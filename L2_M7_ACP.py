from tkinter import *
from datetime import datetime


def calculate_age():
    try:
        user_name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        
        current_year = 2026
        current_month = datetime.now().month
        current_day = datetime.now().day
        
        
        age = current_year - year
        
        
        if (current_month, current_day) < (month, day):
            age -= 1
            
        
        result_label.config(text=f"Hello {user_name}!\nYou are {age} years old.", fg="#2e7d32")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers for dates!", fg="#d32f2f")


root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f4f4f9")


title_label = Label(root, text="Age Calculator", font=("Arial", 16, "bold"), bg="#f4f4f9", fg="#333333")
title_label.pack(pady=15)

grid_frame = Frame(root, bg="#f4f4f9")
grid_frame.pack(pady=10)


Label(grid_frame, text="Name:", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=0, column=0, sticky=E, padx=5, pady=5)
name_entry = Entry(grid_frame, font=("Arial", 10))
name_entry.grid(row=0, column=1, padx=5, pady=5)


Label(grid_frame, text="Birth Day (DD):", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=1, column=0, sticky=E, padx=5, pady=5)
day_entry = Entry(grid_frame, font=("Arial", 10))
day_entry.grid(row=1, column=1, padx=5, pady=5)

Label(grid_frame, text="Birth Month (MM):", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=2, column=0, sticky=E, padx=5, pady=5)
month_entry = Entry(grid_frame, font=("Arial", 10))
month_entry.grid(row=2, column=1, padx=5, pady=5)

Label(grid_frame, text="Birth Year (YYYY):", font=("Arial", 10, "bold"), bg="#f4f4f9").grid(row=3, column=0, sticky=E, padx=5, pady=5)
year_entry = Entry(grid_frame, font=("Arial", 10))
year_entry.grid(row=3, column=1, padx=5, pady=5)

calc_button = Button(
    root, 
    text="Calculate Age", 
    command=calculate_age,
    font=("Arial", 11, "bold"),
    bg="#1e88e5",
    fg="white",
    padx=15,
    pady=5
)
calc_button.pack(pady=20)


result_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f9", justify="center")
result_label.pack(pady=10)

root.mainloop()