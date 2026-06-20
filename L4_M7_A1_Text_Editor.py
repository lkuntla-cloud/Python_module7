from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window=Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def open_file():
    """Open a file for editing"""
    filepath=askopenfilename(filetype=[("Text Files","*.txt"),("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath, "r") as input_file:
        text=input_file.read()
def save_file():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")]) 
    if not filepath:
        return
    with open(filepath,"w")as output_files:
        text=txt_edit.get(1.0,END)
        output_files.write(text)
    window.title(f"Codingals Text Editor-{filepath}")
txt_edit=Text(window)
fr_button=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_button,text="Save As...",command=save_file) 

btn_open
        