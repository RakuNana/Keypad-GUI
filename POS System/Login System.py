from tkinter import *

root = Tk()
root.title("Rakus Restaurant")
root.geometry("600x600")

employee_id = {
"0207" : "Dally",
"2728" : "Raku",
"0126" : "Saree",
"0415" : "Ilze",
"8989" : "Troy"}

employee_title = {
"0207" : "Manager",
"2728" : "Chef",
"0126" : "Linecook",
"0415" : "Prep Cook",
"8989":  "Server",
"0000" : "Dishwasher",
"1111" : "Food runner",
"2222" : "Busser"}

#employee_title_number = {"0207" : 0 , "2728" : 1 , "0126" : 2 , "0415" : 3 , "8989" : 4} can I use to match employee_id????

login = Label(root, text =" ")
login.place(x=280,y=370)

entry_box = Entry()
entry_box.grid(row=0,column=1)


timer = 2

class Main_Gui:

    def __init__(self,master):
        entry_frame = Frame(master)
        entry_frame.grid(row=1,column=0,padx=125)
        numpad = Frame(master)
        numpad.grid(row=1,column=1)


        self.btn0 = Button(root,text="0",width=4,height= 4,command=button_0)
        self.btn0.grid(row=3,column=1)

        self.btn_ent = Button(master,text= "Enter",bg = "green" , width=4,height=4, command =enter_button)
        self.btn_ent.place(x=372,y=270)

        self.btn_clr = Button(master,text= "Clear", bg = "red" ,  width=4,height=4, command =clear_box)
        self.btn_clr.place(x=250,y=270)

    #def number_pad(self):
        keypad = "1234567890"
        i = 0
        btn = []

        for r in range(3):
            for c in range(3):
                btn.append(Button(numpad, width=4,height= 4, text= keypad[i], command = lambda b = i : entry_box.insert(END, keypad[b])))
                btn[i].grid(row=r,column=c)
                i += 1



def enter_button():
    x = entry_box.get()
    if x in employee_id:
        print("Found Match")
        login.config(text = "Logged in as : " + employee_id[entry_box.get()])
        clock_jobs_win()
        entry_box.delete(0,"end")


    else:
        print("No Match Found")
        login.config(text ="No Match Found")
        entry_box.delete(0,"end")



def clock_jobs_win():

    #et = 0

    primary_window = Toplevel()
    primary_window.title("Clock-in/out window")
    primary_window.geometry("600x600")

    jobs_list = Listbox(primary_window,width=20,height=1)
    jobs_list.grid()
    for et in entry_box.get():
        jobs_list.insert(0,employee_title[entry_box.get()])
    #jobs_list.insert(0,employee_title[et]

    btn_clin = Button(primary_window,text= "Clock in", bg = "green" ,  width=8,height=2, command =None)
    btn_clin.place(x=500,y=0)

    btn_clout = Button(primary_window, text = "Clock out" , bg = "red" , width=8 , height=2, command = None)
    btn_clout.place(x=500,y=50)



def button_0():
    zero = entry_box.insert(END,"0")

def clear_box():
    entry_box.delete(0,"end")


MG = Main_Gui(root)
root.mainloop()
