import tkinter                   



root = tkinter.Tk()
root.title("OCR Revision Tool")
root.geometry("800x800")
root.configure(background='white')
root.resizable(width=False, height=False)

quit = tkinter.Button(text="QUIT", fg="red", command=quit, height = 4, width = 6)
quit.place(x=400, y=400) 

def new_winF(): # new window definition
    display = Label(Toplevel(root), text="Title")
    new = tkinter.TK()
    new.title("New Window")
    new.geometry("800x800")
    new.configure(background='white')
    new.resizable(width=False, height=False)
    new.mainloop()

button1 = tkinter.Button(root, text ="open new window", command =new_winF) #command linked
button1.pack()










root.mainloop()
