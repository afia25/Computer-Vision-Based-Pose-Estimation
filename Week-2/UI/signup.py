from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error', "Password Doesn't Match")
    elif check.get() == 0:
        messagebox.showerror('Error', 'Must Accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='12345')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Issue. Try Again!')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username = %s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exists')
        else:
            query = 'insert into data(email, username, password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', "Signup Successful")
            clear()
            signup_window.destroy()
            import Login


signup_window = Tk()
signup_window.geometry('990x660+50+50')
signup_window.title('Signup')
signup_window.resizable(False, False)

bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(signup_window, text='Sign up', font=('Microsoft YaHei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=640, y=120)

heading2 = Label(signup_window, text='Gesture Translator', font=('Microsoft YaHei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading2.place(x=200, y=120)

#Email
def email_enter(e):
    if emailEntry.get() == 'Email':
        emailEntry.delete(0, END)


emailEntry = Entry(signup_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
emailEntry.place(x=580, y=200)
emailEntry.insert(0, 'Email')
emailEntry.bind('<FocusIn>', email_enter)
# usernameEntry.bind('<FocusOut', on_leave)

Frame(signup_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)

#Username Part


def name_enter(e):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


usernameEntry = Entry(signup_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=260)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', name_enter)
# usernameEntry.bind('<FocusOut', on_leave)

Frame(signup_window, width=250, height=2, bg='firebrick1').place(x=580, y=282)

#Password Part


def pass_enter(e):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def conpass_enter(e):
    if confirmpasswordEntry.get() == 'Confirm Password':
        confirmpasswordEntry.delete(0, END)


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    confirmpasswordEntry.config(show='*')
    eyeButton.config(command=show)
    eyeButton2.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    confirmpasswordEntry.config(show='')
    eyeButton.config(command=hide)
    eyeButton2.config(command=hide)


passwordEntry = Entry(signup_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=320)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', pass_enter)
# usernameEntry.bind('<FocusOut', on_leave)

Frame(signup_window, width=250, height=2, bg='firebrick1').place(x=580, y=342)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(signup_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=315)

confirmpasswordEntry = Entry(signup_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
confirmpasswordEntry.place(x=580, y=380)
confirmpasswordEntry.insert(0, 'Confirm Password')
confirmpasswordEntry.bind('<FocusIn>', conpass_enter)
# usernameEntry.bind('<FocusOut', on_leave)

Frame(signup_window, width=250, height=2, bg='firebrick1').place(x=580, y=402)

eyeButton2 = Button(signup_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton2.place(x=800, y=375)


check = IntVar()
termsbutton = Checkbutton(signup_window, text='I Agree to the Terms & Conditions', font=('Microsoft YaHei UI Light',9,'bold'), bg='white', fg='firebrick1', activebackground='white', activeforeground='firebrick1', bd=0, cursor='hand2', variable=check)
termsbutton.place(x=578, y=420)

signupButton = Button(signup_window, text='Signup', font=('open sand', 16, 'bold'), fg='white', bg='firebrick1', activeforeground='white',  activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=connect_database)
signupButton.place(x=578, y=450)

signinLabel = Label(signup_window, text="Already Have An Account?", font=('open sand', 9, 'bold'), fg='firebrick1', bg='white')
signinLabel.place(x=600, y=500)

def signinpage():
    signup_window.destroy()
    import Login

signinButton = Button(signup_window, text='Sign in', font=('open sand', 9, 'bold underline'), fg='blue', bg='white', activeforeground='blue',  activebackground='white', cursor='hand2', bd=0, command=signinpage)
signinButton.place(x=755, y=500)

signup_window.mainloop()