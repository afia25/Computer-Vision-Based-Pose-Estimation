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