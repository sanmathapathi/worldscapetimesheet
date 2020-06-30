import tkinter as tk
from tkinter import *
import os

window =Tk()
window.title("Worldscape Timesheet Login")
window.configure(background="white")

def logout():
    window3.destroy()

def company_select():
    global company_selected
    company_selected = company_listbox.get(ANCHOR)
    company_label.config(text="COMPANY SELECTED:\n" + company_selected)
    sessiondata1 = open(nameinfo + "session data", "w")
    sessiondata1.write(company_selected + "\n")
    sessiondata1.write(paytype_selected + "\n")
    sessiondata1.close()

def paytype_select():
    global paytype_selected
    paytype_selected = paytype_listbox.get(ANCHOR)
    paytype_label.config(text="PAYTYPE SELECTED:\n" + paytype_selected)
    sessiondata1 = open(nameinfo + "session data", "w")
    sessiondata1.write(company_selected + "\n")
    sessiondata1.write(paytype_selected + "\n")
    sessiondata1.close()

def log_hours():
    sessiondata1 = open(nameinfo + "session data", "w")
    sessiondata1.write(company_selected + "\n")
    sessiondata1.write(paytype_selected + "\n")
    sessiondata1.close()


def session():
    global window3
    global sessioninfo1
    global nameinfo
    global sessiondata
    window1.destroy()
    window3 = Toplevel(window)

    window3.title("Dashboard")
    window3.configure(background="white")
    Label (window3, image=logo, bg="white", justify="left") .pack()
    with open(username1) as sessioninfo:
        sessioninfo1 = sessioninfo.readlines()
        nameinfo = sessioninfo1[3]

    sessiondata = open(nameinfo + " session data", "w")
    sessiondata.close()

    Label(window3, text = nameinfo + "\'s Timesheet", bg="white", font="none 20 bold") .pack()

    Button(window3, text="Log Out", width=20, height=1, command=logout) .place(x=1300, y=75)
    Label(window3, text=" ", bg="white") .pack()

    Label(window3, text="Company Select", bg="white", font="none 12 bold") .place(x=125, y=125)
    company_frame = Frame(window3)
    company_scrollbar = Scrollbar(company_frame, orient=VERTICAL)
    global company_listbox
    global company_list
    company_listbox = Listbox(company_frame, yscrollcommand=company_scrollbar.set)
    company_scrollbar.config(command=company_listbox.yview)
    company_scrollbar.pack(side=RIGHT, fill=Y)
    company_frame.place(x=125, y=150)
    company_listbox.pack()
    company_list = ["Company A", "Company B", "Company C", "Other"]
    for company in company_list:
        company_listbox.insert(END, company)
    Button(window3, text="Select", command=company_select) .place(x=165, y=325)
    global company_label
    company_label = Label(window3, text='', bg="white", fg="green", font="none 12 bold")
    company_label.place(x=100, y=355)

    Label(window3, text="Paytype Select", bg="white", font="none 12 bold") .place(x=325, y=125)
    paytype_frame = Frame(window3)
    paytype_scrollbar = Scrollbar(paytype_frame, orient=VERTICAL)
    global paytype_listbox
    global paytype_list
    paytype_listbox = Listbox(paytype_frame, yscrollcommand=paytype_scrollbar.set)
    paytype_scrollbar.config(command=paytype_listbox.yview)
    paytype_scrollbar.pack(side=RIGHT, fill=Y)
    paytype_frame.place(x=325, y=150)
    paytype_listbox.pack()
    paytype_list = ["Hourly", "Weekly", "Monthly", "Annually","Other"]
    for paytype in paytype_list:
        paytype_listbox.insert(END, paytype)
    Button(window3, text="Select", command=paytype_select) .place(x=365, y=325)
    global paytype_label
    paytype_label = Label(window3, text='', bg="white", fg="green", font="none 12 bold")
    paytype_label.place(x=300, y=325)

    global hoursentry1_info
    hoursentry1_info = StringVar()
    Label(window3, text="Day 1", bg="white", fg="black", font="none 12 bold") .place(x=485, y=125)
    hoursentry1 = Entry(window3, textvariable = hoursentry1_info, width=5) .place(x=490, y=150)

    global hoursentry2_info
    hoursentry2_info = StringVar()
    Label(window3, text="Day 2", bg="white", fg="black", font="none 12 bold") .place(x=545, y=125)
    hoursentry2 = Entry(window3, textvariable = hoursentry2_info, width=5) .place(x=550, y=150)

    global hoursentry3_info
    hoursentry3_info = StringVar()
    Label(window3, text="Day 3", bg="white", fg="black", font="none 12 bold") .place(x=605, y=125)
    hoursentry3 = Entry(window3, textvariable = hoursentry3_info, width=5) .place(x=610, y=150)

    global hoursentry4_info
    hoursentry4_info = StringVar()
    Label(window3, text="Day 4", bg="white", fg="black", font="none 12 bold") .place(x=665, y=125)
    hoursentry4 = Entry(window3, textvariable = hoursentry4_info, width=5) .place(x=670, y=150)

    global hoursentry5_info
    hoursentry5_info = StringVar()
    Label(window3, text="Day 5", bg="white", fg="black", font="none 12 bold") .place(x=725, y=125)
    hoursentry5 = Entry(window3, textvariable = hoursentry5_info, width=5) .place(x=730, y=150)

    global hoursentry_notes
    hoursentry_notes = StringVar()
    Label(window3, text="Notes", bg="white", fg="black", font="none 12 bold") .place(x=785, y=125)
    hoursentrynotes = Entry(window3, textvariable = hoursentry_notes, width=20) .place(x=790, y=150)

    Button(window3, text="Log Hours", command = log_hours) .place(x=950, y=150)

def login_success():
    session()
def password_not_recognized():
        Label(window1, text="Password not recognized.", bg="white", fg="red", font="none 12 bold") .pack()
def user_not_found():
        Label(window1, text="User not recognized.", bg="white", fg="red", font="none 12 bold") .pack()

def login():
    global window1
    window1 = Toplevel(window)
    window1.title("Login")
    window1.configure(background="white")
    Label(window1, text="Please enter details below to login.", bg="white", font="none 14 bold") .pack()
    Label(window1, text=" ", bg="white") .pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()


    global username_entry1
    global password_entry1

    Label(window1, text = "Username *", bg="white", font="none 12") .pack()
    username_entry1 = Entry(window1, textvariable = username_verify)
    username_entry1.pack()
    Label(window1, text=" ", bg="white") .pack()
    Label(window1, text="Password *", bg="white", font = "none 12") .pack()
    password_entry1 = Entry(window1, textvariable = password_verify)
    password_entry1.pack()
    Label(window1, text=" ", bg="white") .pack()
    Button(window1, text="Login", width=10, height=1, bg="white", command=login_verify) .pack()

def login_verify():
    global activesessioninfo
    global username1

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            password_not_recognized()
    else:
        user_not_found()

def register_user():

    global firstname_info
    global lastname_info
    global email_info
    global username_info
    global password_info
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    email_info = email.get()
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(email_info)
    file.write("\n")
    file.write(username_info)
    file.write("\n")
    file.write(password_info)
    file.write("\n")
    file.write(firstname_info + " " + lastname_info)
    file.close()

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(window2, text = "Registration Success", fg="green", font="none 12 bold") .pack()
def newuser():
    global window2
    window2 = Toplevel(window)
    window2.title("New User")
    window2.configure(background="white")

    global firstname
    global lastname
    global email
    global username
    global password
    global firstname_entry
    global lastname_entry
    global email_entry
    global username_entry
    global password_entry

    firstname = StringVar()
    lastname = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()


    Label(window2, text="Please enter details below to register.", bg="white", font="none 14 bold") .pack()
    Label(window2, text=" ", bg="white") .pack()
    Label(window2, text="First Name", bg="white", font="none 12") .pack()
    firstname_entry = Entry(window2, textvariable = firstname)
    firstname_entry.pack()
    Label(window2, text="Last Name", bg="white", font="none 12") .pack()
    lastname_entry = Entry(window2, textvariable = lastname)
    lastname_entry.pack()
    Label(window2, text="Email", bg="white", font="none 12") .pack()
    email_entry = Entry(window2, textvariable = email)
    email_entry.pack()
    Label(window2, text="Username", bg="white", font="none 12") .pack()
    username_entry = Entry(window2, textvariable = username)
    username_entry.pack()
    Label(window2, text="Password", bg="white", font="none 12") .pack()
    password_entry = Entry(window2, textvariable = password)
    password_entry.pack()
    Label(window2, text=" ", bg="white") .pack()
    Button(window2, text="Register", width=10, height=1, command=register_user) .pack()





global logo
logo = PhotoImage(file="worldscapeinc.png")
Label (window, image=logo, bg="white", justify="left") .pack()

Label (window, text="Worldscape Timesheet", bg="white", fg="black", font="none 20 bold") .pack()

Button(text="Login", width=20, command=login) .pack()
Label(window, text=" ", bg="white") .pack()
Button(window, text="New User?", width=20, command=newuser) .pack()
window.mainloop()
