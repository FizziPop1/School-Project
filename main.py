import tkinter                   



root = tkinter.Tk()
root.title("OCR Revision Tool")
root.geometry("800x800")
root.configure(background='white')
root.resizable(width=False, height=False)

close=tkinter.Button(text="QUIT", fg="red", command=quit, height=4, width=6)
close.place(x=400, y=400) 

def new_win(): # new window definition
    new = tkinter.Tk()
    new.title("New Window")
    new.geometry("800x800")
    new.configure(background='white')
    new.resizable(width=False, height=False)
    new.mainloop()
    close = tkinter.Button(text="QUIT", fg="red", command=quit, height=4, width=6)
    close.place(x=400, y = 400)
    
    
window=tkinter.Button(text="New Window", fg="blue", command=new_win, height=4, width=12) #command linked
window.place(x=400, y=350)

root.mainloop()
