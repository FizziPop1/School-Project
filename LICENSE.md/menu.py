from tkinter import *
import time
import random


questions = {}
random_list = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(random_list)
current_question = 1








def destroy():

    close_button.place(x=970, y = 420)
    about_button.place(x=970, y=360)
    start_button.place(x=970, y=300)
    quit_info.place(x=970, y=300)
    version['fg'] = "white"
    conf.destroy()
    root.title("Computer Science Quiz")
    root_win2()


def clear_text():
    global clear

    clear = Label(root, bg="white", 
                 fg="White",
                 font = ("Segoe UI", 14),
                 text="                                                                                                      "
                 )


    clear.place(x=23, y=20)

    root_win2()


def confirmation2():
    global conf2, continue_button1

    def conf2_sub():
        conf2.destroy()
        undestroy()


    conf2 = Toplevel()
    conf2.title("Return?")
    conf2.geometry("230x105")
    conf2.configure(background='white')
    conf2.resizable(width=False, height=False)
    
    conf2_label = Label(conf2, bg="white", justify=LEFT, anchor=W, text="Are you sure you want to return to \n"
                                                                        "the start menu?")
    conf2_label.pack()
    
    continue_button1 = Button(conf2, text="Continue", command=conf2_sub, height=2, width=10)
    continue_button1.place(x=23, y=45)

    back_button3 = Button(conf2, text="Go back", command=conf2.destroy, height=2, width=10)
    back_button3.place(x=123, y=44)

    conf2.focus_set()
    conf2.grab_set()


    conf.mainloop()





def undestroy():
    
    question.place(x=920, y=20)
    current.place(x=900, y=20)
    next_button.place(x=970, y=300)
    home_button.place(x=940, y=740)
    quit_info.place(x=180, y=480)
    
    
    close_button.place(x=370, y = 420)
    about_button.place(x=370, y=360)
    start_button.place(x=370, y=300)
    version['fg'] = "Black"                 
   

def back():
    question_variable = str(questions[temp_list[0]])
    question = Label(root, bg="white", text=question_variable, font = ("Segoe UI", 14))
    question.place(x=20, y=20)
    del(temp_list[0])
    current_question -= 1
    root_win2()

def root_win2():                                                                                                                         
    global current_question, current, question_variable, questions, next_button, home_button, question, back_button4, temp_var, back                                             

    temp_var = 0


    questions = {
    1: "Describe what the instruction 'BRP' does.",
    2: "Describe what is meant by the term 'Open Source Software'.",
    3: "What is meant by the term 'Lossy Compression'?",
    4: "What is the number '55' as an 8-bit unsigned integer?",
    5: "What might a printer use RAM for?",
    6: "Describe the term 'firewall'.",
    7: "Describe the Rapid Application Development process."
    }


    question_variable = str(questions[random_list[0]])

    question = Label(root, bg="white", text=question_variable, font = ("Segoe UI", 14))
    question.place(x=20, y=20)

    print (random_list)
    print (question_variable)

    temp_var = random_list[0]
    print(temp_var)

   
    del(random_list[0])



    current = Label(root, fg="red", bg="white", text=(str(current_question) + " / 7"), font  = ("Segoe UI Light", 20))
    current.place(x=700, y=20)

    current_question += 1

    next_button = Button(text="Next", command=clear_text, height=3, width=12)
    next_button.place(x=430, y=350)
    
    back_button4 = Button(text="Back", height=3, width=12)
    back_button4.place(x=310, y=350)

    home_button = Button(text="Home", fg="Red", command=confirmation2,  height=3, width=12)
    home_button.place(x=4, y=740)

    
    

def root_win1(): 
    global root, close_button, about_button, start_button, version, quit_info
    root = Tk()
    root.title("Start Menu")
    root.geometry("800x800")
    root.configure(background='white')
    root.resizable(width=False, height=False)


    close_button = Button(text="Quit", fg="red", command=quit, height=3, width=12)  
    close_button.place(x=370, y = 420)

    about_button = Button(text="About", fg="blue", command=new_win, height=3, width=12) 
    about_button.place(x=370, y=360)

    start_button = Button(text="Begin", fg="green", command=confirmation1, height=3, width=12)
    start_button.place(x=370, y=300)

    version = Label(root, bg="white", text="v0.54")
    version.place(x=767, y=0)
    
    quit_info = Label(root, bg="white", text="(If you quit the application, you'll lose any progress you've made on the quiz)", font = ("Segoe UI", 10))
    quit_info.place(x=180, y=480)



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
                                                             "Version 0.54 \n\n"
                                                             "Firas Hafiz - 2018 \n\n"
                                                             "You can visit the subject specification from the link below: \n")
                                                             
    about_text.pack()

    back_button1 = Button(about, text="Okay", command=about.destroy, height=2, width=10)
    back_button1.place(x=145, y=240)
    
    link = Label(about, bg="white", justify=LEFT, anchor=W, text="OCR AS Level Computer Science Specification", fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", callback)

    about.focus_set()
    about.grab_set()
    
    about.mainloop()


def confirmation1():
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



