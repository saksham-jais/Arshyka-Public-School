
from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as mycon
import os

def login_user():
    if UsernameEntry.get()=="" or PasswordEntry.get() =="":
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
    else:
        try:
            my=mycon.connect(host="localhost", user="root", passwd="tiger")
            mycursor=my.cursor()
        except:
            messagebox.showerror("ERROR","Connection is not established try again")
            return
        query="use school"
        mycursor.execute(query)
        query = "select * from userdata where username=%s and password=%s"
        mycursor.execute(query, [UsernameEntry.get(),PasswordEntry.get()])

        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "INVALID USERNAME AND PASSWORD")

        else:
            messagebox.showinfo("WELCOME","login is successful")
            root.destroy()
            # os.system('homepage.py')
            import homepage
def forget():
    window= Toplevel()
    window.title("change password")
    window.geometry("1000x700+60+50")
    pic=ImageTk.PhotoImage(file='forget.jpg')
    piclabel=Label(window,image=pic)
    piclabel.place(x=0,y=0)

    def change():
        if User_Entry.get() =="" or Pass_Entry.get() =="":
            messagebox.showerror("ERROR","All fields are required",parent=window)
        else:
            my = mycon.connect(host="localhost", user="root", passwd="tiger",database="school")
            mycursor = my.cursor()
            query = "select * from userdata where username=%s"
            mycursor.execute(query, [User_Entry.get()])

            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "INCORRECT USERNAME",parent=window)
            else:
                query="update data set password=%s where username=%s"

                mycursor.execute(query, [Pass_Entry.get(),User_Entry.get()])
                # my.commit()
                # my.close()
                messagebox.showinfo("SUCCESS","Password is reset, please login with new password",parent=window)
                my.commit()
                my.close()
                window.destroy()

    def on_enter6(event):
        if User_Entry.get() == "Username":
            User_Entry.delete(0,END)


    def on_enter7(event):
        if Pass_Entry.get() == "New Password":
            Pass_Entry.delete(0,END)

    User_Entry = Entry(window, width=20, font=("Microsoft Yahei UI Light", 15, "bold"), bd=0)
    User_Entry.place(x=650, y=350)
    User_Entry.insert(0, "Username")
    User_Entry.bind("<FocusIn>", on_enter6)
    Pass_Entry = Entry(window, width=20, font=("Microsoft Yahei UI Light", 15, "bold"), bd=0)

    Pass_Entry.place(x=650, y=430)
    Pass_Entry.insert(0, "New Password")
    Pass_Entry.bind("<FocusIn>", on_enter7)

    subButton=Button(window,text="SUBMIT",font=("Open Sans",15,"bold"),bg="#3b3935",activeforeground="#3b3935",activebackground="black",cursor="hand2",bd=0,width=15,command=change)
    subButton.place(x=680,y=515)




    window.mainloop()

def loge_up():
    root.destroy()
    import signup
def on_enter(event):
    if UsernameEntry.get()=="Username":
        UsernameEntry.delete(0,END)
def on_enter1(event):
    if PasswordEntry.get() == "Password":
        PasswordEntry.delete(0, END)


root=Tk()
root.geometry("1000x700+60+50")
root.title("loge_page")
bgImage=ImageTk.PhotoImage(file='logein.jpg')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)
h=Label(root,text="USERNAME",font=("Microsoft Yahei UI Light",11),bd=0,bg="#f7838d").place(x=140,y=270)
UsernameEntry=Entry(root,width=20,font=("Microsoft Yahei UI Light",15,"bold"),bd=0)
UsernameEntry.place(x=140,y=300)
UsernameEntry.insert(0,"Username")
UsernameEntry.bind("<FocusIn>",on_enter)
P=Label(root,text="PASSWORD",font=("Microsoft Yahei UI Light",11),bd=0,bg="#f7838d").place(x=140,y=340)
PasswordEntry=Entry(root,width=20,font=("Microsoft Yahei UI Light",15,"bold"),bd=0)

PasswordEntry.place(x=140,y=380)
PasswordEntry.insert(0,"Password")
PasswordEntry.bind("<FocusIn>",on_enter1)

# el=Label(root,text="EMAIL",font=("Microsoft Yahei UI Light",10,"bold"),bg="#917b5d").place(x=100,y=360)
# emEntry=Entry(root,width=30,font=("Microsoft Yahei UI Light",15,"bold"),bd=0)
# emEntry.place(x=100,y=380)
# emEntry.insert(0,"Email")
# emEntry.bind("<FocusIn>",on_enter2)

forgetbutton=Button(root,text="forget password?",font=("Microsoft Yahei UI Light",10,"bold"),bg="#f7838d",bd=0,activeforeground="white",activebackground="#f7838d",cursor="hand2",command=forget)
forgetbutton.place(x=290,y=420)

Lbutton=Button(root,text="LOGIN",font=("Open Sans",15,"bold"),bg="#3b3935",activeforeground="#3b3935",activebackground="black",cursor="hand2",bd=0,width=15,command=login_user)
Lbutton.place(x=180,y=450)

s=Label(root,text="Don't have an account?",font=("Open Sans",9,"bold"),bg="#f7838d",activeforeground="white",cursor="hand2",width=20)
s.place(x=130,y=580)


s=Button(root,text="Create a new one",command=loge_up,font=("Open Sans",9,"bold"),bd=0,bg="light pink",activeforeground="white",activebackground="blue",cursor="hand2")
s.place(x=270,y=580)
# Frame(root,width=145,height=2,bg="black").place(x=240,y=610)


root.mainloop()