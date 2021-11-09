from tkinter import*
from functools import partial
root = Tk()
#def validateLogin(username, password):
def validateLogin(username):
   print("username entered :", username.get())
  #print("password entered :", password.get())
   return
def quit():
        root.destroy()
def showWindowMenu1():
    window1 = Tk()  
    window1.geometry('1000x400')  
    window1.title('PLAY')
    myMenu1 = Menu()
    menuItem1 = Menu(tearoff=0)
    menuItem1.add_command(label="Hard" , command = showWindowMenu4)
    menuItem1.add_command(label="Normal")
    menuItem1.add_command(label="Easy")
    myMenu1.add_cascade(label="Mode",menu=menuItem1,)
    window1.config(menu=myMenu1)
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
def showWindowMenu4():
    window4 =Tk()
    window4.title("HARD")
    window4.geometry("1000x400")
    window4.mainloop()
    myMenu2 = Menu()
    menuItem2 = Menu(tearoff=0)
    menuItem2.add_command(label="Food")
    menuItem2.add_command(label="Animal")
    menuItem2.add_command(label="Fruit")
    menuItem2.add_command(label="Internal Organs")
    menuItem2.add_command(label="Family")
    menuItem2.add_command(label="Occupations")
    menuItem2.add_command(label="Places")
    myMenu2.add_cascade(label="Category",menu=menuItem2)
    window4.config(menu=myMenu2)
    window4.mainloop()
check = True
root.title("Game")
#pic1 = Tk()
#photo  =PhotoImage(file="projectA1/xx.png")
#Button(root,image=photo).pack()
#pic.mainloop

myLable1 = Button(text="PLAY",fg="pink",font=('Tahoma', 20, 'bold'),bg="black",activebackground='pink',activeforeground="black",command=lambda:[validateLogin(),quit(),showWindowMenu1()]).place(x=467, y=175)
myLable2 = Button(text="HOW TO",fg="pink",font=('Tahoma', 20, 'bold'),bg="black",activebackground='pink',activeforeground="black",command = showWindowMenu2).place(x=444, y=245)
myLable3 = Button(text="SCORE",fg="pink",font=('Tahoma', 20, 'bold'),bg="black",activebackground='pink',activeforeground="black",command = showWindowMenu3).place(x=456, y=315)

if check == True:
    print("window on")
root.geometry("1000x400")
cheak = False


#username label and text entry box
usernameLabel = Label(root, text="User Name",font=('Tahoma', 15, 'bold')).place(x=377, y=100)
username = StringVar()
usernameEntry = Entry(root, textvariable=username).place(x=507, y=110)
'''
#password label and password entry box
passwordLabel = Label(root,text="Password",font=('Tahoma', 15, 'bold')).place(x=377, y=115)  
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*').place(x=507, y=120) 
'''

#validateLogin = partial(validateLogin, username, password)
validateLogin = partial(validateLogin, username)

#login button
#loginButton = Button(root, text="log in",fg="pink",font=('Tahoma', 10, 'bold'),bg="black",activebackground='pink',activeforeground="black", command=validateLogin).grid(row=4, column=0)  
root.mainloop()


