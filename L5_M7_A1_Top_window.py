from tkinter import*
root=Tk()
root.geometry("400x300")
root.title("main")

def topwind():
    top=Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    
    L2=Label(top,text="This is toplevel window")
    L2.pack()
    top.mainloop()
l=Label(root,text="This is root window")
btn=Button(root,text="click here to open another window",command=topwind)

l.pack()
btn.pack()

root.mainloop()
