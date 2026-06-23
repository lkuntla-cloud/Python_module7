from tkinter import *

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")
root.configure(bg="#f0f4f8")


desc_label = Label(
    root, 
    text="This application calculates the product of two numbers.", 
    font=("Arial", 10, "italic"),
    bg="#f0f4f8",
    fg="#333333"
)
desc_label.pack(pady=10)

# Input Elements
label1 = Label(root, text="Enter First Number:", font=("Arial", 10), bg="#f0f4f8")
label1.pack()
entry1 = Entry(root, font=("Arial", 10), justify="center")
entry1.pack(pady=2)

label2 = Label(root, text="Enter Second Number:", font=("Arial", 10), bg="#f0f4f8")
label2.pack()
entry2 = Entry(root, font=("Arial", 10), justify="center")
entry2.pack(pady=2)

result_text = Text(root, width=35, height=2, font=("Arial", 10), bg="#ffffff")


calc_button = Button(
    root, 
    text="Calculate Product", 
    command=lambda: [
        result_text.delete("1.0", END),
        result_text.insert(END, f"The product is: {float(entry1.get()) * float(entry2.get())}")
    ],
    font=("Arial", 10, "bold"),
    bg="#4caf50", 
    fg="white",
    padx=10,
    pady=5
)
calc_button.pack(pady=15)
result_text.pack(pady=5)

root.mainloop()