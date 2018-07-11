from tkinter import *

root = Tk()
root.title("OCR Revision Tool")
root.geometry("800x800")
root.configure(background='white')
root.resizable(width=False, height=False)

close = Button(text="QUIT", fg="red", command=quit, height=4, width=6)
close.place(x=400, y=400) 

def new_win(): # new window definition
    about = Tk()
    about.title("About")
    about.geometry("300x500")
    about.configure(background='white')
    about.resizable(width=False, height=False)
    about_text = Text(root, height=4, width= 50)
    about_text.pack()
    about_text.insert(END, "OCR AS Level Computer Science Quiz")
    about.mainloop()
    close = Button(text="QUIT", fg="red", command=quit, height=4, width=6)
    close.place(x=400, y = 400)

window = Button(text="New Window", fg="blue", command=new_win, height=4, width=12) #command linked
window.place(x=400, y=350)
root.mainloop()
