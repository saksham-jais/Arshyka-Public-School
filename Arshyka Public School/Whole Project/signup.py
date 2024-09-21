from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector as mycon


signup_window=Tk()
signup_window.title("sign_up")
bg1= ImageTk.PhotoImage(file='logepage.jpg')
signup_window.resizable(False,False)
bgl1=Label(signup_window,image=bg1)
bgl1.grid()


def clear():
    emailEntry.delete(0,END)
    username1Entry.delete(0,END)
    Password1Entry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def signup():
    if emailEntry.get() =="" or username1Entry.get() =="" or Password1Entry.get() =="" or confirmEntry.get() =="":
        messagebox.showerror("Error",'All fields are requires')
    elif Password1Entry.get() != confirmEntry.get():
        messagebox.showerror("Error","Password mismatched")
    elif check.get()==0:
        messagebox.showerror("Error","PLEASE ACCEPT TERMS AND CONDITIONS")
    else:
        try:
            main_con =mycon.connect(host="localhost", user="root", passwd="tiger")
            mycursor=main_con.cursor()
        except:
            messagebox.showerror("Error","Database connectivity issue, please try again")
            return

        try:
            mycursor.execute("use school")
            query = "select * from userdata where username=%s"
            mycursor.execute(query, [username1Entry.get()])
            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "username already exists")
            else:
                query = "insert into userdata(email,username,password) values(%s,%s,%s)"

                mycursor.execute(query, [emailEntry.get(), username1Entry.get(), Password1Entry.get()])
                main_con.commit()
                main_con.close()
                messagebox.showinfo("Success", "REGISTRATION IS SUCCESSFUL")
                signup_window.destroy()
                import login

        except Exception as e:
            messagebox.showerror('Error' , f"An error occured {str(e)}")







def on_enter4(event):
    if emailEntry.get() == "Email":
        emailEntry.delete(0, END)

def on_enter1(event):
    if username1Entry.get() == "Username":
        username1Entry.delete(0, END)

def on_enter2(event):
    if Password1Entry.get() == "Password":
        Password1Entry.delete(0, END)
def on_enter3(event):
    if confirmEntry.get() == "Confirm Password":
        confirmEntry.delete(0, END)

def loge_page():
    signup_window.destroy()
    import login

emil=Label(signup_window,text="EMAIL",font=("Microsoft Yahei UI Light",10,"bold"),bg="#f7838d")
emil.place(x=650,y=190)

emailEntry=Entry(signup_window,width=20,font=("Microsoft Yahei UI Light",15,"bold"),bd=0)
emailEntry.place(x=650,y=230)
emailEntry.insert(0,"Email")
emailEntry.bind("<FocusIn>", on_enter4)
# signup_window.mainloop()
u=Label(signup_window,text="USERNAME",font=("Microsoft Yahei UI Light",10,"bold"),bg="#f7838d")
u.place(x=650,y=270)
username1Entry=Entry(signup_window, width=20, font=("Microsoft Yahei UI Light", 15, "bold"), bd=0)
username1Entry.place(x=650, y=300)
username1Entry.insert(0, "Username")
username1Entry.bind("<FocusIn>", on_enter1)

# u=Label(signup_window,text="USERNAME",font=("Microsoft Yahei UI Light",10,"bold"),bg="#f7838d")
P=Label(signup_window,text="PASSWORD",font=("Microsoft Yahei UI Light",10,"bold"),bg="#f7838d")
P.place(x=650,y=345.5)
Password1Entry=Entry(signup_window, width=20, font=("Microsoft Yahei UI Light", 15, "bold"), bd=0)
Password1Entry.place(x=650, y=380)
Password1Entry.insert(0, "Password")
Password1Entry.bind("<FocusIn>", on_enter2)

c=Label(signup_window,text="CONFIRM PASSWORD",font=("Microsoft Yahei UI Light",10,"bold"),bg="#f7838d")
c.place(x=650,y=425)
confirmEntry=Entry(signup_window, width=20, font=("Microsoft Yahei UI Light", 15, "bold"), bd=0)
confirmEntry.place(x=650, y=460)
confirmEntry.insert(0, "Confirm Password")
confirmEntry.bind("<FocusIn>", on_enter3)
check=IntVar()
tc=Checkbutton(signup_window,text="I AGREE ALL THE TERMS AND CONDITIONS",font=("Microsoft Yahei UI Light",8,"bold"),bg="#f7838d",activebackground="#f7838d",variable=check)
tc.place(x=650, y=500)

signupbutton=Button(text="SIGNUP",command=signup,font=("Microsoft Yahei UI Light",13,"bold"),bd=0,bg="#3b3935",activebackground="#3b3935",activeforeground="white",cursor="hand2")
signupbutton.place(x=730,y=532)

alreadyaccount=Label(signup_window,text="Already have an account?",font=("Open Sans",9,"bold"),bg="#f7838d",activeforeground="white",cursor="hand2",width=20)
alreadyaccount.place(x=650,y=590)


loginbutton=Button(signup_window,text="Log in",command=loge_page,font=("Open Sans",9,"bold"),bd=0,bg="light pink",activeforeground="white",activebackground="blue",cursor="hand2")
loginbutton.place(x=800,y=590)

signup_window.mainloop()