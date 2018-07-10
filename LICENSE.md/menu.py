import tkinter                   



root = tkinter.Tk()
root.title("OCR Revision Tool")
root.geometry("800x800")
root.configure(background='white')
root.resizable(width=False, height=False)

quit = tkinter.Button(text="QUIT", fg="red", command=quit, height=4, width=6)
quit.place(x=400, y=400) 

def new_winF(): # new window definition
    new = tkinter.TK()
    new.title("New Window")
    new.geometry("800x800")
    new.configure(background='white')
    new.resizable(width=False, height=False)
    new.mainloop()
    close = tkinter.Button(text="QUIT", fg="red", command=quit, height=4, width=6)
    close.place(x=400, y=400)
    
    
button1 = tkinter.Button(text="open new window", fg="blue", command=new_winF(), height=4, width=6) #command linked
button1.place(x=400, y=425)






root.mainloop()
