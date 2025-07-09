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