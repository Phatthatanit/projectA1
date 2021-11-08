from tkinter import*

from functools import partial

def validateLogin(username, password):
   print("username entered :", username.get())
   print("password entered :", password.get())
   return


def showWindowMenu1():
    window1 = Tk()  
    window1.geometry('1000x400')  
    window1.title('PLAY')
    window1.mainloop()

def showWindowMenu2():
    window2 =Tk()
    window2.title("HOW TO")
    window2.geometry("1000x400")
    window2.mainloop()

def showWindowMenu3():
    window3 =Tk()
    window3.title("SCORE")
    window3.geometry("1000x400")
    window3.mainloop()
check = True

root = Tk()
root.title("Game")
myMenu = Menu()
  

#pic1 = Tk()
#photo  =PhotoImage(file="projectA1/xx.png")
#Button(root,image=photo).pack()
#pic.mainloop


#menuItem = Menu()
#menuItem.add_command(label="file",command = showWindow)

#root.config(menu=myMenu)
#myMenu.add_cascade(label="manu",menu=menuItem)


myLable1 = Button(text="PLAY",fg="pink",font=('Tahoma', 20, 'bold'),bg="black",activebackground='pink',activeforeground="black",command=lambda:[validateLogin(),showWindowMenu1()]).place(x=467, y=175)
myLable2 = Button(text="HOW TO",fg="pink",font=('Tahoma', 20, 'bold'),bg="black",activebackground='pink',activeforeground="black",command = showWindowMenu2).place(x=444, y=245)
myLable3 = Button(text="SCORE",fg="pink",font=('Tahoma', 20, 'bold'),bg="black",activebackground='pink',activeforeground="black",command = showWindowMenu3).place(x=456, y=315)

if check == True:
    print("window on")
root.geometry("1000x400")

cheak = False

#username label and text entry box
usernameLabel = Label(root, text="User Name",font=('Tahoma', 15, 'bold')).place(x=377, y=75)
username = StringVar()
usernameEntry = Entry(root, textvariable=username).place(x=507, y=80)

#password label and password entry box
passwordLabel = Label(root,text="Password",font=('Tahoma', 15, 'bold')).place(x=377, y=115)  
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*').place(x=507, y=120) 

validateLogin = partial(validateLogin, username, password)

#login button
#loginButton = Button(root, text="log in",fg="pink",font=('Tahoma', 10, 'bold'),bg="black",activebackground='pink',activeforeground="black", command=validateLogin).grid(row=4, column=0)  
root.mainloop()


