from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

home_window = Tk()
home_window.geometry('990x660+50+50')
home_window.title('Home Page')
home_window.resizable(False, False)

bgImage = ImageTk.PhotoImage(file='bgbg.jpg')
bgLabel = Label(home_window, image=bgImage, width=990, height=900)
bgLabel.place(x=0, y=0)

heading = Label(home_window, text='Gesture Translator', font=('Courier', 40, 'bold'), fg='white', bg='firebrick1')
heading.place(x=220, y=100)

def tranlatepage():
    home_window.destroy()
    import final_pred

translateButton = Button(home_window, text='Translate', font=('open sand', 16, 'bold'), fg='white', bg='firebrick1', activeforeground='white',  activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=tranlatepage)
translateButton.place(x=378, y=200)

def signinpage():
    home_window.destroy()
    import Login

logoutButton = Button(home_window, text='Logout', font=('open sand', 16, 'bold'), fg='white', bg='firebrick1', activeforeground='white',  activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=signinpage)
logoutButton.place(x=378, y=250)

heading2 = Label(home_window, text='------ Meet The Developers ------', font=('Courier', 23, 'bold'), fg='firebrick1')
heading2.place(x=180, y=380)

plabon = ImageTk.PhotoImage(file='pd.jpg')
plabonLabel = Label(home_window, image=plabon, width=300, height=200)
plabonLabel.place(x=30, y=440)

bidita = ImageTk.PhotoImage(file='bd.jpg')
biditaLabel = Label(home_window, image=bidita, width=300, height=200)
biditaLabel.place(x=345, y=440)

mahmud = ImageTk.PhotoImage(file='md.jpg')
mahmudLabel = Label(home_window, image=mahmud, width=300, height=200)
mahmudLabel.place(x=659, y=440)

home_window.mainloop()
