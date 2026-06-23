from tkinter import *

def convert_length(event=None):
    try:
        value_in_meters = float(value_entry.get())
        
        cm = value_in_meters * 100
        inches = value_in_meters * 39.3701
        
        result_string = f"{value_in_meters} m =\n\n• {cm:.2f} cm\n• {inches:.2f} inches"
        result_label.config(text=result_string, fg="#1565c0")
        
    except ValueError:
        result_label.config(text="Error: Please enter a valid number!", fg="#d32f2f")

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#eef2f3")

header = Label(
    root, 
    text="Meters Converter", 
    font=("Arial", 16, "bold"), 
    bg="#eef2f3", 
    fg="#2c3e50"
)
header.pack(pady=20)

input_frame = Frame(root, bg="#eef2f3")
input_frame.pack(pady=10)

Label(input_frame, text="Value (Meters):", font=("Arial", 11, "bold"), bg="#eef2f3").grid(row=0, column=0, padx=5)
value_entry = Entry(input_frame, font=("Arial", 11), justify="center", width=15)
value_entry.grid(row=0, column=1, padx=5)

value_entry.bind("<Return>", convert_length)

convert_button = Button(
    root, 
    text="Convert", 
    font=("Arial", 11, "bold"),
    bg="#2c3e50",
    fg="white",
    padx=20,
    pady=5,
    relief="flat"
)
convert_button.pack(pady=20)

convert_button.bind("<Button-1>", convert_length)

result_label = Label(
    root, 
    text="Enter a value and press Convert", 
    font=("Arial", 12, "normal"), 
    bg="#ffffff", 
    width=30, 
    height=6,
    relief="solid",
    bd=1,
    fg="#7f8c8d"
)
result_label.pack(pady=15)

root.mainloop()