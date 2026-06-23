from tkinter import *

def display():
    try:
        textbox.delete("1.0", END)
        
        p = float(principle_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())
        
        si = (p * r * t) / 100
        amount = p * ((1 + r / 100) ** t)
        ci = amount - p
        
        textbox.insert(END, f"Simple interest = {str(si)}")
        textbox.insert(END, f"\nCompound interest = {str(ci)}")
        
    except ValueError:
        textbox.delete("1.0", END)
        textbox.insert(END, "Error: Please enter valid numeric values!")

root = Tk()
root.title("Interest Calculator")
root.geometry("450x450")
root.configure(bg="#f0f4f8")

frame = Frame(root, bg="#f0f4f8")
frame.pack(pady=15)

principle_lbl = Label(frame, text="Principle", bg="#9A38D3", fg="white", width=12)
principle_lbl.grid(row=0, column=0, padx=5, pady=5)

rate_lbl = Label(frame, text="Rate(%)", bg="#9A38D3", fg="white", width=12)
rate_lbl.grid(row=1, column=0, padx=5, pady=5)

time_lbl = Label(frame, text="Time(in years)", bg="#9A38D3", fg="white", width=14)
time_lbl.grid(row=2, column=0, padx=5, pady=5)

principle_entry = Entry(frame)
principle_entry.grid(row=0, column=1, padx=5, pady=5)

rate_entry = Entry(frame)
rate_entry.grid(row=1, column=1, padx=5, pady=5)

time_entry = Entry(frame)
time_entry.grid(row=2, column=1, padx=5, pady=5)

btn = Button(root, text="Calculate", command=display, bg="green", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=10)

textbox = Text(root, width=40, height=6, bg="#F0F2F0", fg="black", font=("Arial", 10))
textbox.pack(pady=10)

root.mainloop()