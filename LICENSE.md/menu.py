import tkinter                   



root = tkinter.Tk()
root.title("OCR Revision Tool")
root.geometry("800x800")
root.configure(background='white')
root.resizable(width=False, height=False)

quit =tkinter.Button(text="QUIT", fg="red", command=quit, height=4, width=6)
quit.place(x=400, y=400) 

def new_win(): # new window definition
    new = tkinter.Tk()
    new.title("New Window")
    new.geometry("800x800")
    new.configure(background='white')
    new.resizable(width=False, height=False)
    new.mainloop()

close = tkinter.Button(text="QUIT", fg="red", command=quit, height=4, width=6)
close.place(x=400, y = 500)
    
    
window=tkinter.Button(text="open new window", fg="blue", command=new_win, height=4, width=6) #command linked
window.place(x=400, y=425)






root.mainloop()
