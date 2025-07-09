from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def forget_pass():
    def change_pass():
        if user_Entry.get() == '' or password_Entry.get() == '':
            messagebox.showerror('Error', 'All Fields are Required', parent = window)
        elif password_Entry.get() != confirmpassword_Entry.get():
            messagebox.showerror('Error', "Password Doesn't Matched", parent = window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='12345', database='userdata')
            mycursor = con.cursor()
            query = 'use userdata'
            mycursor.execute(query)
            query = 'select * from data where username = %s'
            mycursor.execute(query, (user_Entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username')
            else:
                query = 'update data set password = %s where username = %s'
                mycursor.execute(query, (password_Entry.get(), user_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password Reset Successfully', parent=window)
                window.destroy()
    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('arial', '18', 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    user_Label = Label(window, text='Username', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
    user_Label.place(x=470, y=130)

    user_Entry = Entry(window, width=25, font=('arial', '11', 'bold'), bd=0, fg='magenta2')
    user_Entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    password_Label = Label(window, text='Password', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
    password_Label.place(x=470, y=210)

    password_Entry = Entry(window, width=25, font=('arial', '11', 'bold'), bd=0, fg='magenta2')
    password_Entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpassword_Label = Label(window, text='Confirm Password', font=('arial', '12', 'bold'), bg='white', fg='orchid1')
    confirmpassword_Label.place(x=470, y=290)

    confirmpassword_Entry = Entry(window, width=25, font=('arial', '11', 'bold'), bd=0, fg='magenta2')
    confirmpassword_Entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submit_Button = Button(window, text='Submit', bd=0, bg='magenta2', fg='white', font=('open sans', '16', 'bold'), width=19, cursor='hand2', activeforeground='white', activebackground='magenta2', command=change_pass)
    submit_Button.place(x=470, y=390)


    window.mainloop()

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are Required!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='12345', database='userdata')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection Failed. Try Again!')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username = %s and password = %s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invaild Username or Password')
        else:
            # messagebox.showinfo('Success', 'Login Successful')
            login_window.destroy()
            import Home


login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.title('Login Page')
login_window.resizable(False, False)

bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='Sign in', font=('Microsoft YaHei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=640, y=120)

heading2 = Label(login_window, text='Gesture Translator', font=('Microsoft YaHei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading2.place(x=200, y=120)

#Username Part


def name_enter(e):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


usernameEntry = Entry(login_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', name_enter)
# usernameEntry.bind('<FocusOut', on_leave)

Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)

#Password Part


def pass_enter(e):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


passwordEntry = Entry(login_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', pass_enter)
# usernameEntry.bind('<FocusOut', on_leave)

Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2', font=('Microsoft YaHei UI Light', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1', command=forget_pass)
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login', font=('open sand', 16, 'bold'), fg='white', bg='firebrick1', activeforeground='white',  activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

orLabel = Label(login_window, text='--------------OR--------------', font=('open sand', 16), fg='firebrick1', bg='white')
orLabel.place(x=583, y=400)

facebooklogo = PhotoImage(file='facebook.png')
googlelogo = PhotoImage(file='Glogo.png')
twiterlogo = PhotoImage(file='X-Logo.png')

fbLabel = Label(login_window, image=facebooklogo, bg='white')
fbLabel.place(x=640, y=440)

GLabel = Label(login_window, image=googlelogo, bg='white')
GLabel.place(x=690, y=440)

TLabel = Label(login_window, image=twiterlogo, bg='white')
TLabel.place(x=740, y=440)

signupLabel = Label(login_window, text="Don't Have An Account?", font=('open sand', 9, 'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=593, y=500)

def signuppage():
    login_window.destroy()
    import signup

signupButton = Button(login_window, text='Sign up', font=('open sand', 9, 'bold underline'), fg='blue', bg='white', activeforeground='blue',  activebackground='white', cursor='hand2', bd=0, command=signuppage)
signupButton.place(x=732, y=500)

login_window.mainloop()