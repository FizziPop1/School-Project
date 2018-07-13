from tkinter import *
import time
import random

def destroy(): 

    random_question = Label()

    close_button.destroy()
    about_button.destroy()
    start_button.destroy()
    version.destroy()
    conf.destroy()
    root.title("Computer Science Quiz")
    root_win2()

    


def root_win2():  # THIS FUNCTION IS WHERE THE QUESTION ASKING HAPPENS
  
    
  
    questions = {
        q1: "Describe what the instruction 'BRP' does.",
        a1: ,
        q2: "Describe what is meant by the term 'Open Source Software'.",
        a2: ,
        q3: "What is meant by the term 'Lossy Compression'?",
        a3: ,
        q4: "What is the number '55' as an 8-bit unsigned integer?",
        a4: ,
        q5: "What might a printer use RAM for?",
        a5: ,
        q6: "Describe the term 'firewall'.",
        a6: ,
        q7: "Describe the Rapid Application Development process."
        a7 ,
    }
    
    Qavailability = {
        q1: "True"
        q2: "True"
        q3: "True"
        q4: "True"
        q5: "True"
        q6: "True"
        q7: "True"
    }
     ANS = randint(1,7) #Python will pick a "random" number, in this case, first must be 1 and second the amount of questions
     Q='q'+ANS
     A='a'+ANS
     if Qavailability[Q] - "TRUE":
            print(questions[Q])
            response=input()
            Qavailability[Q]="False"
            if response==questions[A]:
                print("correct")
            elif response!=questions[A]:
                print("incorrect")
                
            


def root_win1():
    global root, close_button, about_button, start_button, version, root

    root = Tk()
    root.title("Start Menu")
    root.geometry("800x800")
    root.configure(background='white')
    root.resizable(width=False, height=False)

    close_button = Button(text="Quit", fg="red", command=quit, height=3, width=12)  
    close_button.place(x=370, y = 420)

    about_button = Button(text="About", fg="blue", command=new_win, height=3, width=12) 
    about_button.place(x=370, y=360)

    start_button = Button(text="Begin", fg="green", command=confirmation, height=3, width=12)
    start_button.place(x=370, y=300)

    version = Label(root, bg="white", text="v0.48")
    version.place(x=767, y=0)




def callback(event):
    webbrowser.open_new(r"http://www.ocr.org.uk/Images/170845-specification-accredited-as-level-gce-computer-science-h046.pdf")



def new_win(): 

    about = Toplevel()
    about.title("About")
    about.geometry("370x300")
    about.configure(background='white')
    about.resizable(width=False, height=False)

    about_text = Label(about, bg="white", anchor=W, justify=LEFT, text = "OCR AS Level Computer Science Quiz \n\n"
                                                             "This app quizzes you on 25 random questions related to computing, \n"
                                                             "in accordance with the OCR AS Computer Science specification \n\n"
                                                             "You are given 10 minutes to answer 25 questions \n\n"
                                                             "Version 0.48 \n\n"
                                                             "Firas Hafiz - 2018 \n\n"
                                                             "You can visit the subject specification from the link below: \n")
                                                             
    about_text.pack()

    back_button1 = Button(about, text="Understood", command=about.destroy, height=2, width=10)
    back_button1.place(x=145, y=240)
    
    link = Label(about, bg="white", justify=LEFT, anchor=W, text="OCR AS Level Computer Science Specification", fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", callback)

    about.focus_set()
    about.grab_set()
    
    about.mainloop()


def confirmation():
    global conf

    conf = Toplevel()
    conf.title("Begin?")
    conf.geometry("250x100")
    conf.configure(background='white')
    conf.resizable(width=False, height=False)
    
    conf_label = Label(conf, bg="white", justify=LEFT, anchor=W, text="Are you sure you want to continue?")
    conf_label.pack()
    
    continue_button = Button(conf, text="Continue", command=destroy, height=2, width=10)
    continue_button.place(x=30, y=30)

    back_button2 = Button(conf, text="Go back", command=conf.destroy, height=2, width=10)
    back_button2.place(x=136, y=30)

    conf.focus_set()
    conf.grab_set()


    conf.mainloop()

root_win1()
root.mainloop()
