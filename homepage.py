import os
from tkinter import *
from tkinter import  ttk
import tkinter.messagebox as mb
import mysql.connector as sq
from tkcalendar import DateEntry
from PIL import Image, ImageTk





m= Tk()
m.geometry("1366x768")
m.title("HOME PAGE")
m.resizable(0,0)

main = sq.connect(host='localhost', user='root', password='tiger',database= "school" )
mycursor= main.cursor()


def btn1_click():
    a= []
    b= []
    query= 'select count(*) from studdetails'
    mycursor.execute(query)
    all= mycursor.fetchone()
    a.append(all)
    for i in a:
        b.append(i[0])
    if bt['text']== "Total Students":
        bt.config(text= f"Total Students:- {b[0]}")
        bt.place(x= 660, y= 280)
    else:
        bt.config(text= "Total Students")
        bt.place(x= 680, y= 280)


def btn2_click():
    a= []
    b= []
    query= 'select count(*) from tdetails'
    mycursor.execute(query)
    all= mycursor.fetchone()
    a.append(all)
    for i in a:
        b.append(i[0])
    if btn2['text']== "Total Teachers":
        btn2.config(text= f"Total Teachers:- {b[0]}")
        btn2.place(x= 992, y= 280)
    else:
        btn2.config(text= "Total Teachers")
        btn2.place(x= 1015, y= 280)

def btn3_click():
    a= []
    b= []
    query= 'select count(*) from staff'
    mycursor.execute(query)
    all= mycursor.fetchone()
    a.append(all)
    for i in a:
        b.append(i[0])
    if btn3['text']== "Total Staffs":
        btn3.config(text= f"Total Staffs:- {b[0]}")
        btn3.place(x= 680, y= 570)
    else:
        btn3.config(text= "Total Staffs")
        btn3.place(x= 690, y= 570)

def btn4_click():
    a= []
    b= []
    query= 'select count(*) from vehicle'
    mycursor.execute(query)
    all= mycursor.fetchone()
    a.append(all)
    for i in a:
        b.append(i[0])
    if btn4['text']== "Total Vehicles":
        btn4.config(text= f"Total Vehicles:- {b[0]}")
        btn4.place(x= 992, y= 570)
    else:
        btn4.config(text= "Total Vehicles")
        btn4.place(x= 1015, y= 570)






def dash():
    for widget in m.winfo_children():
        if isinstance(widget, Frame):
            widget.destroy()


def stud():


    def add():
        if not name_strvar.get() or not class_strvar.get() or not section_strvar.get() or not admis_strvar.get() or not contact_strvar.get() or not email_strvar.get() or gender_strvar.get()== 'Select' or not dob_date.get() or stream_strvar.get()== 'Select' or not pname_strvar.get() or not mname_strvar.get()  or not doa_date.get():
            mb.showerror(title="Error", message='PLEASE ENTER ALL THE DETAILS')

        elif len(contact_strvar.get()) != 10:
            mb.showerror('Error', 'Invalid Contact')

        elif admis_strvar.get()== '0':
            mb.showerror(title="Error", message='invalid admission number')


        else:
            aa = (name_strvar.get(), class_strvar.get(), section_strvar.get(), contact_strvar.get(), email_strvar.get(),gender_strvar.get(), dob_date.get(), stream_strvar.get(), admis_strvar.get(), pname_strvar.get(),mname_strvar.get(), address_strvar.get(), doa_date.get())
            sql = "insert into studdetails(sname, sclass,section, phone_no,email, gender,sdob,stream, admission_no, Father_name, Mother_name, Address, DOA) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s)"
            mycursor.execute(sql, aa)
            main.commit()
            mb.showinfo(title="Record Inserted", message=f" Record of {name_strvar.get()} is Inserted")



    def delete():

        if not name_strvar.get()  or not admis_strvar.get():
            mb.showerror(title="Error", message='PLEASE ENTER ALL THE NECESSARY DETAILS')


        else:
            aa = []
            b = [admis_strvar.get()]
            query = "select * from studdetails where admission_no= %s"
            mycursor.execute(query, b)
            all = mycursor.fetchone()
            aa.append(all)

            if aa[0] == None:
                mb.showerror("Error", f"No Record of id {admis_strvar.get()}")

            else:
                aa = [admis_strvar.get()]
                sql = "delete from studdetails where admission_no= %s "
                mycursor.execute(sql, aa)
                main.commit()
                query= 'delete from junior where admission_no = %s'
                mycursor.execute(query,aa)
                main.commit()
                query= 'delete from class6_8 where admission_no= %s'
                mycursor.execute(query, aa)
                main.commit()
                query = 'delete from class9_10 where admission_no= %s'
                mycursor.execute(query, aa)
                main.commit()
                query = 'delete from maths where admission_no= %s'
                mycursor.execute(query, aa)
                main.commit()
                query = 'delete from biology where admission_no= %s'
                mycursor.execute(query, aa)
                main.commit()
                query = 'delete from commerce where admission_no= %s'
                mycursor.execute(query, aa)
                main.commit()
                query = 'delete from humanity where admission_no= %s'
                mycursor.execute(query, aa)
                main.commit()
                mb.showinfo("Record Deleted", f" Record of {name_strvar.get()} is Deleted")


    def modify():

        if not name_strvar.get() or not class_strvar.get() or not section_strvar.get() or not contact_strvar.get() or not email_strvar.get() or gender_strvar.get()=='Select' or not admis_strvar.get() or not dob_date.get() or stream_strvar.get()== 'Select' or not pname_strvar.get() or not mname_strvar.get() or not address_strvar.get() or not doa_date:
            mb.showerror(title="error", message='PLEASE ENTER ALL THE DETAILS')

        else:
            aa = []
            b = [admis_strvar.get()]
            query = "select * from studdetails where admission_no= %s"
            mycursor.execute(query, b)
            all = mycursor.fetchone()
            aa.append(all)

            if aa[0] == None:
                mb.showerror("Error", f"No Record of id {admis_strvar.get()}")

            else:
                a = (name_strvar.get(), class_strvar.get(), section_strvar.get(), contact_strvar.get(), email_strvar.get(),gender_strvar.get(), dob_date.get(), stream_strvar.get(), pname_strvar.get(), mname_strvar.get(), address_strvar.get(), admis_strvar.get())
                sql = "update studdetails set sname= %s,sclass= %s,section= %s, phone_no= %s,email= %s, gender= %s, sdob= %s, stream=%s, Father_name= %s, Mother_name= %s, Address= %s" \
                      "where admission_no= %s "
                mycursor.execute(sql, a)
                main.commit()
                mb.showinfo("record inserted", f" Record of {name_strvar.get()} is modified")


    def clear():
        for widget in fm.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, 'end')

        for widget in fm1.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, 'end')

        gender_strvar.set("Select")
        stream_strvar.set("Select")



    def view():

        if not name_strvar.get() or not admis_strvar.get():
            mb.showerror(title="error", message='Please Enter the Necessary Details Like Name And Admission no.')

        else:
            a= []
            b= []
            sql= "Select * from studdetails" \
                 " where admission_no= %s"
            aa= [admis_strvar.get()]
            mycursor.execute(sql, aa)
            all= mycursor.fetchone()
            a.append(all)

            if a[0]== None:
                mb.showerror("Error", "No Record Found")

            else:
                for i in a[0]:
                    b.append(i)

                if b[1] != name_strvar.get():
                    mb.showerror("Error", "Invalid Name")


                else:
                    img = PhotoImage(file="Untitled design.png")
                    lb = Label(fm, image=img)
                    lb.place(x=0, y=0, height=726, width=835)

                    lb.image = img
                    fm2 = Frame(fm, bg="#f1c2bd", highlightbackground="#d8aeaa", highlightthickness=10)
                    fm2.place(x=180, y=100, width=500, height=550)

                    Label(fm, bg="#f3e7fa", text=f"Record of {name_strvar.get()}:",
                          font=('Courier', 26, 'bold', 'underline')).place(
                        x=100, y=5, width=735)

                    img1 = PhotoImage(file="arr.png")
                    bb = Button(fm, image=img1, command=stud)
                    bb.place(x=10, y=5, width=50, height=50)

                    bb.image = img1

                    Label(fm2, text="Addmission no:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=10)
                    Label(fm2, text=f"{b[0]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=235, y=10)
                    Frame(fm2, bg="black").place(x=235, y=37, width=200, height=4)

                    Label(fm2, text="Student Name:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=45)
                    Label(fm2, text=f"{b[1]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=225, y=45)
                    Frame(fm2, bg="black").place(x=225, y=75, width=250, height=4)

                    Label(fm2, text="Class:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=90)
                    Label(fm2, text=f"{b[4]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=125, y=90)
                    Frame(fm2, bg="black").place(x=125, y=120, width=100, height=4)

                    Label(fm2, text="Section:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=250, y=90)
                    Label(fm2, text=f"{b[5]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=390, y=90)
                    Frame(fm2, bg="black").place(x=390, y=120, width=80, height=4)

                    Label(fm2, text="Father's Name:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=145)
                    Label(fm2, text=f"{b[2]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=250, y=145)
                    Frame(fm2, bg="black").place(x=250, y=175, width=225, height=4)

                    Label(fm2, text="Mother's Name:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=195)
                    Label(fm2, text=f"{b[3]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=250, y=195)
                    Frame(fm2, bg="black").place(x=250, y=225, width=225, height=4)

                    Label(fm2, text="Contact:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=245)
                    Label(fm2, text=f"{b[6]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=150, y=245)
                    Frame(fm2, bg="black").place(x=150, y=275, width=225, height=4)

                    Label(fm2, text="Email:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=295)
                    Label(fm2, text=f"{b[9]}", bg="#f1c2bd", fg="red", font=("Courier", 17, 'bold')).place(x=115, y=295)
                    Frame(fm2, bg="black").place(x=115, y=325, width=370, height=4)

                    Label(fm2, text="Date of Birth:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=345)
                    Label(fm2, text=f"{b[11]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=250,
                                                                                                            y=345)
                    Frame(fm2, bg="black").place(x=250, y=375, width=225, height=4)

                    Label(fm2, text="Address:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=395)
                    Label(fm2, text=f"{b[8]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=150, y=395)
                    Frame(fm2, bg="black").place(x=150, y=425, width=300, height=4)

                    Label(fm2, text="Gender:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=445)
                    Label(fm2, text=f"{b[10]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=125,
                                                                                                            y=445)
                    Frame(fm2, bg="black").place(x=125, y=475, width=200, height=4)

                    Label(fm2, text="Stream:", bg="#f1c2bd", font=("Courier", 20, 'bold')).place(x=10, y=495)
                    Label(fm2, text=f"{b[12]}", bg="#f1c2bd", fg="red", font=("Courier", 19, 'bold')).place(x=125,
                                                                                                            y=495)
                    Frame(fm2, bg="black").place(x=125, y=525, width=300, height=4)


    fm= Frame(m, bg="#7FFFD4")
    fm.place(x=510, y=10, height=726, width=835)
    img= PhotoImage(file= "Untitled design.png")
    a= Label(fm, image = img)
    a.place(x= 0, y= 0, height= 726, width= 835)

    a.image= img

    img2 = PhotoImage(file="arr.png")
    bb = Button(fm, image=img2, command=dash)
    bb.place(x=5, y=10, width=50, height=50)

    bb.image = img2


    Label(fm, bg= "#f3e7fa").place(x= 60, y= 15, width= 775, height= 40)
    Label(fm, bg="#f3e7fa", text= "Enter Student Details Here",fg= "black", font= ('Courier',23,'bold','underline')).place(x= 110,y= 15)
    Label(fm, bg="#f3e7fa", bd= 2).place(x=0, y=70, width=835, height=30)

    Label(fm, text= "Addmission no:", fg= "black", bg="#f3e7fa", font=('Courier',15,'bold')).place(x= 10, y= 71)
    admis_strvar= Entry(fm,textvariable= IntVar() , bg= 'white', width= 15)
    admis_strvar.place(x= 200, y= 76, height= 20)


    Label(fm, text= "Date:", bg= "#f3e7fa", fg= "black",font=('Courier',15,'bold')).place(x= 400, y= 71)
    doa_date= DateEntry(fm, bg= "white", fg= "black",date_pattern= 'dd/mm/yy' ,textvariable= StringVar(), width= 20)
    doa_date.place(x= 470, y= 76)

    fm1= Frame(fm, bg= "#f1c2bd", highlightbackground= "#d8aeaa", highlightthickness= 5)
    fm1.place(x= 70, y= 130, width= 700, height= 400)

    Label(fm1, text= "Student Name:-", bg= "#f1c2bd", font= ('Arial', 18, 'bold')).place(x= 10, y= 30)
    name_strvar= Entry(fm1, bg= "white", textvariable= StringVar(), width= 20, bd= 0, font= ('Arial', 18))
    name_strvar.place(x= 195, y= 32)

    Label(fm1, text="Father's Name:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=10, y=79)
    pname_strvar= Entry(fm1, bg="white", textvariable=StringVar(), width=20, bd=0, font=('Arial', 18))
    pname_strvar.place(x=200, y=81)

    Label(fm1, text="Mother's Name:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=10, y=130)
    mname_strvar= Entry(fm1, bg="white", textvariable=StringVar(), width=20, bd=0, font=('Arial', 18))
    mname_strvar.place(x=210, y=137)

    Label(fm1, text= "Class:-", bg= '#f1c2bd', font= ('Arial', 18, 'bold')).place(x= 12, y= 179)
    class_strvar= Entry(fm1, textvariable= StringVar(), bg= 'white', width= 10, bd=0, font= ('Arial', 18))
    class_strvar.place(x= 100, y= 181)

    Label(fm1, text="Section:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=380, y= 179)
    section_strvar= Entry(fm1, textvariable= StringVar(), bg= 'white', width= 8, bd=0, font= ('Arial', 18))
    section_strvar.place(x= 500, y= 181)

    Label(fm1, text="Email:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=10, y=219)
    email_strvar= Entry(fm1, textvariable= StringVar(), bg= 'white', width=30,  bd=0, font= ('Arial', 18))
    email_strvar.place(x= 100, y= 223)

    Label(fm1, text="Gender:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=10, y=259)
    gender_strvar= ttk.Combobox(fm1, textvariable= StringVar(),values= ['Male', 'Female'], state= 'readonly')
    gender_strvar.set("Select")
    gender_strvar.place(x= 120, y=265, width= 100)


    Label(fm1, text="Stream:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=350, y=259)
    stream_strvar= ttk.Combobox(fm1, textvariable= StringVar(),values= ['Science with Maths', 'Science with Bio', 'Humanity', 'Commerce', 'None'], state= 'readonly')
    stream_strvar.set("Select")
    stream_strvar.place(x= 460, y= 265, width= 200 )

    Label(fm1, text="Address:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=10, y=304)
    address_strvar= Entry(fm1, textvariable= StringVar(), bg= 'white', width=30,  bd=0, font= ('Arial', 18))
    address_strvar.place(x= 130, y= 308)

    Label(fm1, text="Date of Birth:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=10, y=349)
    dob_date= DateEntry(fm1, bg= "white", fg= "black",date_pattern= 'dd/mm/YY', textvariable= StringVar(), width= 20, bd= 0)
    dob_date.place(x= 200, y= 354, width= 100)

    Label(fm1, text="Contact No:-", bg="#f1c2bd", font=('Arial', 18, 'bold')).place(x=320, y=349)
    contact_strvar= Entry(fm1,textvariable= IntVar() ,bg='white', width=15, bd=0, font=('Arial', 18))
    contact_strvar.place(x=480, y=354)


    Button(fm, text= "Submit And Add Record", font= ('Arial', 15, 'bold'), bg= "#f3e7fa", command= add, bd= 2, width= 20).place(x= 300, y= 550)
    Button(fm, text= "Delete Record", font= ('Arial', 15, 'bold'), bg= "#f3e7fa", bd= 2, width= 20, command= delete).place(x= 480, y=600)
    Button(fm, text= "Modify Record", font= ('Arial', 15, 'bold'), bg= "#f3e7fa", bd= 2, width=20, command= modify).place(x= 100, y=600)
    Button(fm, text= "Clear Record", font= ('Arial', 15, 'bold'), bg= "#f3e7fa", bd= 2, width= 20, command= clear).place(x= 480, y=650)
    Button(fm, text= "View Record", font= ('Arial', 15, 'bold'), bg= "#f3e7fa", bd= 2, width= 20, command= view).place(x= 100, y=650)



def teacher():

    def add():
        if not t_name.get() or not t_id.get() or not t_dob.get() or not t_hire.get() or not t_sal.get() or not t_email.get() or not t_gender.get() or not t_address.get() or not t_qualification.get() or not t_contact.get():
            mb.showerror('Error', 'All Fields are required')

        elif len(t_contact.get()) != 10:
            mb.showerror('Error', 'Invalid Contact number')

        else:
            b = []
            aa = [t_id.get()]
            query = 'select * from  tdetails where teacher_id= %s'
            mycursor.execute(query, aa)
            all = mycursor.fetchone()
            b.append(all)
            print(b)
            if b[0]== None:
                a = (t_id.get(), t_name.get(), t_contact.get(), t_dob.get(), t_hire.get(), t_qualification.get(),
                     t_address.get(), t_gender.get(), t_sal.get(), t_email.get())
                query = "insert into tdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query, a)
                main.commit()
                tree.insert(parent='', index='end', values=(
                t_id.get(), t_name.get(), t_contact.get(), t_dob.get(), t_hire.get(), t_qualification.get(),
                t_address.get(), t_gender.get(), t_sal.get(), t_email.get()))
                mb.showinfo('Record Inserted', f'Record of {t_name.get()} is inserted')
                clear()

            else:
                mb.showerror('Error', 'Record Already Present')


    def clear():
        for widget in fm3.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, 'end')

            if isinstance(widget, DateEntry):
                widget.delete(0, 'end')


    def delete():
        if not t_name.get() or not t_id.get():
             mb.showerror('Error', 'some fields are required like Name,  T_id')


        else:
             a= [t_id.get(), t_name.get()]
             query = "delete from tdetails where Teacher_id= %s and Name= %s"
             mycursor.execute(query, a)
             main.commit()
             for item in tree.get_children():
                   tree.delete(item)
             query = 'select * from tdetails'
             mycursor.execute(query)
             all = mycursor.fetchall()
             for val in all:
                    tree.insert(parent='', index='end', values=val)
                    mb.showinfo('Deleted', 'Record deleted')
        clear()

    def modify():
        if not t_name.get() or not t_id.get() or not t_dob.get() or not t_hire.get() or not t_sal.get() or not t_email.get() or not t_gender.get() or not t_address.get() or not t_qualification.get() or not t_contact.get():
            mb.showerror('Error', 'All Fields are required')

        else:
            aa= []
            b= [t_id.get()]
            query= "select * from tdetails where Teacher_id= %s"
            mycursor.execute(query, b)
            all = mycursor.fetchone()
            aa.append(all)

            if aa[0] == None:
                mb.showerror("Error", f"No Record of id {t_id.get()}")

            else:
                a = [t_name.get(), t_contact.get(), t_dob.get(), t_hire.get(), t_qualification.get(), t_address.get(),
                     t_gender.get(), t_sal.get(), t_email.get(), t_id.get()]
                query = "Update tdetails set Name= %s, Contact= %s, DOB=%s, Hiredate= %s, Qualifications= %s, Address= %s, Gender= %s, Salary= %s, Email= %s" \
                        "where Teacher_id= %s"
                mycursor.execute(query, a)
                main.commit()
                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from tdetails'
                mycursor.execute(query)
                all = mycursor.fetchall()
                for val in all:
                    tree.insert(parent='', index='end', values=val)

                mb.showinfo('Updated', f'Record of {t_name.get()} is modified')


            clear()

    def display(a):
        clear()
        selecteditem = tree.selection()[0]
        t_id.insert(0, tree.item(selecteditem)['values'][0])
        t_name.insert(0, tree.item(selecteditem)['values'][1])
        t_contact.insert(0, tree.item(selecteditem)['values'][2])
        t_dob.insert(0, tree.item(selecteditem)['values'][3])
        t_hire.insert(0, tree.item(selecteditem)['values'][4])
        t_qualification.insert(0, tree.item(selecteditem)['values'][5])
        t_address.insert(0, tree.item(selecteditem)['values'][6])
        t_gender.insert(0, tree.item(selecteditem)['values'][7])
        t_sal.insert(0, tree.item(selecteditem)['values'][8])
        t_email.insert(0, tree.item(selecteditem)['values'][9])



    fm= Frame(m, bg= "#4EEE94")
    fm.place(x= 510, y= 10, height= 726, width= 835)

    Frame(fm, bg= "#FAF0E6", highlightbackground= 'black', highlightthickness=2).place(x= 60,y= 7, width= 775, height= 45)
    Label(fm, bg= "#FAF0E6", text= "Teachers Record", font= ('Arial', 20, 'underline', 'bold')).place(x= 320, y= 9)
    Label(fm, bg= "#FAF0E6", text= ".", font= ('Arial', 20, 'bold')).place(x= 548, y= 9)

    img = PhotoImage(file="arr.png")
    lb = Button(fm, image=img, command= dash)
    lb.place(x=5, y=7, height= 50, width=50)

    lb.image = img

    fm3= Frame(fm, bg= "#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground= 'black')
    fm3.place(x= 5, y= 60, height= 650, width= 280 )

    Label(fm3, bg="#E6E6FA", fg="black", text="Name  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=5)
    t_name= Entry(fm3, bg="#E6E6FA", fg='red', bd=0, font=("Giddyup Std", 13))
    t_name.place(x=5, y=30,width=250,height=30)
    Frame(fm3, bg='black').place(x=5, y=55, width=250, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="Teacher's ID  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=60)
    t_id= Entry(fm3, bg="#E6E6FA", fg='red', bd=0, font=("Giddyup Std", 15))
    t_id.place(x=5, y=85, width=250,height=30)
    Frame(fm3, bg='black').place(x=5, y=110, width=250, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="Contact  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=115)
    t_contact= Entry(fm3, bg="#E6E6FA", fg='red', bd=0, font=("Giddyup Std", 15))
    t_contact.place(x=5, y=140, width=250,height=30)
    Frame(fm3, bg='black').place(x=5, y=165, width=250, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="DOB  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=170)
    t_dob= DateEntry(fm3, bg="#E6E6FA",date_pattern='dd/mm/yyyy', fg='red', bd=0,font=("Giddyup Std", 12))
    t_dob.place(x=5, y=195, width=125, height=30)
    Frame(fm3, bg='black').place(x=5, y=220, width=125, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="HireDate  :", font=("Giddyup Std", 14, 'bold')).place(x=150, y=170)
    t_hire = DateEntry(fm3, bg="#E6E6FA", date_pattern='dd/mm/yyyy', fg='red', bd=0, font=("Giddyup Std", 12))
    t_hire.place(x=150, y=195, width=120, height=30)
    Frame(fm3, bg='black').place(x=150, y=220, width=120, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text= "Qualifications  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=225)
    t_qualification = Entry(fm3, bg="#E6E6FA",fg='red', bd=0,font=("Giddyup Std", 15))
    t_qualification.place(x=5, y=250, width=250, height=30)
    Frame(fm3, bg='black').place(x=5, y=275, width=250, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="Address  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=280)
    t_address = Entry(fm3, bg="#E6E6FA", fg='red', bd=0,font=("Giddyup Std", 15))
    t_address.place(x=5, y=305, width=250, height=30)
    Frame(fm3, bg='black').place(x=5, y=330, width=250, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="Gender  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=335)
    t_gender = Entry(fm3, bg="#E6E6FA", fg='red', bd=0,font=("Giddyup Std", 15))
    t_gender.place(x=5, y=360, width=250, height=30)
    Frame(fm3, bg='black').place(x=5, y=385, width=250, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="Salary  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=390)
    t_sal = Entry(fm3, bg="#E6E6FA",fg='red', bd=0,font=("Giddyup Std", 15))
    t_sal.place(x=5, y=415, width=250, height=30)
    Frame(fm3, bg='black').place(x=5, y=440, width=250, height=4)

    Label(fm3, bg="#E6E6FA", fg="black", text="Email  :", font=("Giddyup Std", 14, 'bold')).place(x=5, y=445)
    t_email = Entry(fm3, bg="#E6E6FA",fg='red', bd=0,font=("Giddyup Std", 15))
    t_email.place(x=5, y=470, width=250, height=30)
    Frame(fm3, bg='black').place(x=5, y=495, width=250, height=4)

    Frame(fm3, bg='black').place(x=0, y=520, width=280, height=8)
    Frame(fm3, bg='black').place(x=0, y=530, width=280, height=8)

    Button(fm3, relief= RAISED, bg= "#BFEFFF", bd= 2, width= 16, text= "Add Record",font= ('Comic Sans MS', 10, 'bold'), command= add).place(x= 2, y= 550)
    Button(fm3, relief=RAISED, bg="#BFEFFF", bd=2, width=15, text="Modify Record",font= ('Comic Sans MS', 10, 'bold'), command= modify).place(x=140, y=550)
    Button(fm3, relief=RAISED, bg="#BFEFFF", bd=2, width=16, text="Delete Record",font= ('Comic Sans MS', 10, 'bold'), command= delete).place(x=2, y=600)
    Button(fm3, relief=RAISED, bg="#BFEFFF", bd=2, width=15, text="Clear Fields",font= ('Comic Sans MS', 10, 'bold'), command= clear).place(x=140, y=600)


    fm2= Frame(fm,  bg= "#BFEFFF", highlightthickness=4, highlightbackground= 'black')
    fm2.place(x= 290, y= 60, height= 650, width= 540)

    STYLE=ttk.Style()
    STYLE.theme_use('clam')

    columns= ['Teacher id', 'Name', 'Contact', 'DOB', 'HireDate', 'Qualifications', 'Address', 'Gender', 'Salary', 'Email' ]
    tree= ttk.Treeview(fm2, columns= columns, height= 100, selectmode= BROWSE)
    xscroll= Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    yscroll= Scrollbar(tree, orient=VERTICAL, command=tree.yview)

    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

    tree.heading('Teacher id', text='T_id', anchor=CENTER)
    tree.heading('Name', text='Name', anchor=CENTER)
    tree.heading('Contact', text='Contact', anchor=CENTER)
    tree.heading('DOB', text='DOB', anchor=CENTER)
    tree.heading('HireDate', text='H_Date', anchor=CENTER)
    tree.heading('Qualifications', text='Qualifications', anchor=CENTER)
    tree.heading('Address', text='Address', anchor=CENTER)
    tree.heading('Gender', text='Gender', anchor=CENTER)
    tree.heading('Salary', text='Salary', anchor=CENTER)
    tree.heading('Email', text='Email', anchor=CENTER)



    tree.place(y=0, x= 0, relwidth= 1, relheight= 1, relx= 0)

    tree.column('#0', width=0, stretch=NO, anchor= CENTER)
    tree.column('#1', width=60, stretch=NO, anchor= CENTER)  #t_id
    tree.column('#2', width=140, stretch=NO, anchor= CENTER)  #name
    tree.column('#3', width=100, stretch=NO, anchor= CENTER)   #contact
    tree.column('#4', width=80, stretch=NO, anchor= CENTER)   #dob
    tree.column('#5', width=80, stretch=NO, anchor= CENTER )  #hiredate
    tree.column('#6', width=140, stretch=NO, anchor= CENTER)   #qualifications
    tree.column('#7', width=180, stretch=NO, anchor= CENTER)   #address
    tree.column('#8', width=60, stretch=NO, anchor= CENTER)   #gender
    tree.column('#9', width=70, stretch=NO, anchor= CENTER)   #salary
    tree.column('#10', width=180, stretch=NO, anchor= CENTER)   #email


    query = 'select * from tdetails'
    mycursor.execute(query)
    all = mycursor.fetchall()
    for val in all:
        tree.insert(parent= '', index= 'end', values= val)

    tree.bind("<<TreeviewSelect>>", display)

def staff():
    def clear():
        for widget in dtl2.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, 'end')

            if isinstance(widget, DateEntry):
                widget.delete(0, 'end')

        dptmnt_entry.set("select")
        gndr_entry.set("select")


    def add():
            if not id_entry.get() or not name_entry.get()  or not cntct_entry.get() or not dob_cal.get()  or not hired_cal.get() or not add_entry.get() or not sal_entry.get() or gndr_entry.get()== 'select' or dptmnt_entry.get()== 'select':
                mb.showerror('Error', 'All Fields are required')

            elif len(cntct_entry.get()) != 10:
                mb.showerror('Error', 'Invalid Contact number')

            else:
                b=[]
                aa= [id_entry.get()]
                query= 'select * from staff where staff_id= %s'
                mycursor.execute(query,aa)
                all= mycursor.fetchone()
                b.append(all)
                if b[0]== None:
                    a = (id_entry.get(), name_entry.get(), gndr_entry.get(), add_entry.get(), cntct_entry.get(),
                         dob_cal.get(), dptmnt_entry.get(),
                         hired_cal.get(), sal_entry.get())
                    query = "insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(query, a)
                    main.commit()
                    tree.insert(parent='', index='end', values=(
                    id_entry.get(), name_entry.get(), gndr_entry.get(), add_entry.get(), cntct_entry.get(),
                    dob_cal.get(), dptmnt_entry.get(),
                    hired_cal.get(), sal_entry.get()))
                    mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                else:
                    mb.showerror('Error', f'Record of {id_entry.get()} is already present')

            clear()

    def modify():
        if not id_entry.get() or not name_entry.get() or  gndr_entry.get()=='select' or not cntct_entry.get() or not dob_cal.get() or dptmnt_entry.get()== 'select' or not hired_cal.get() or not add_entry.get() or not sal_entry.get():
            mb.showerror('Error', 'All Fields are required')

        else:
            aa= []
            b= [id_entry.get()]
            query= "select * from staff where staff_id= %s"
            mycursor.execute(query, b)
            all = mycursor.fetchone()
            aa.append(all)

            if aa[0] == None:
                mb.showerror("Error", f"No Record of id {id_entry.get()}")

            else:
                a = (name_entry.get(),gndr_entry.get(), add_entry.get(), cntct_entry.get(), dob_cal.get(),dptmnt_entry.get(),hired_cal.get(), sal_entry.get(), id_entry.get())
                query = "Update staff set name= %s, gender= %s,address= %s,contact= %s, DOB=%s,designation= %s ,Hiredate= %s, Salary= %s" \
                        "where staff_id= %s"
                mycursor.execute(query, a)
                main.commit()
                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from staff'
                mycursor.execute(query)
                all = mycursor.fetchall()
                for val in all:
                    tree.insert(parent='', index='end', values=val)

                mb.showinfo('Updated', f'Record of {name_entry.get()} is modified')
            clear()

    def delete():
        if not id_entry.get() or not name_entry.get() :
            mb.showerror('Error', 'Please Enter Necessary Details Like Name And ID')

        else:
            aa = []
            bb= []
            b = [id_entry.get()]
            query = "select * from staff where staff_id= %s"
            mycursor.execute(query, b)
            all = mycursor.fetchone()
            aa.append(all)

            if aa[0] == None:
                mb.showerror("Error", f"No Record of id {id_entry.get()}")

            else:
                for i in aa[0]:
                    bb.append(i)

                if bb[1]!= name_entry.get():
                    mb.showerror('Error', 'Name not match')

                else:
                    a= [id_entry.get()]
                    query= "Delete from staff where staff_id= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)
                    query = 'select * from staff'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)

                    mb.showinfo("Deleted", f"Record of {id_entry.get()} is deleted")
                    clear()

    def search():
        query= "select * from staff where name like '%"+srch_entry.get()+"%'"
        mycursor.execute(query)
        all= mycursor.fetchall()
        for item in tree.get_children():
            tree.delete(item)
        for val in all:
            tree.insert(parent= '', index= 'end', values= val)

    def cancel():
        srch_entry.delete(0, 'end')
        for item in tree.get_children():
            tree.delete(item)
        query= 'select * from staff'
        mycursor.execute(query)
        all= mycursor.fetchall()
        for val in all:
            tree.insert(parent= '', index= 'end', values= val)



    def display(a):
        clear()
        selecteditem = tree.selection()[0]
        id_entry.insert(0, tree.item(selecteditem)['values'][0])
        name_entry.insert(0, tree.item(selecteditem)['values'][1])
        gndr_entry.set(tree.item(selecteditem)['values'][2])
        add_entry.insert(0, tree.item(selecteditem)['values'][3])
        cntct_entry.insert(0, tree.item(selecteditem)['values'][4])
        dob_cal.insert(0, tree.item(selecteditem)['values'][5])
        dptmnt_entry.set(tree.item(selecteditem)['values'][6])
        hired_cal.insert(0, tree.item(selecteditem)['values'][7])
        sal_entry.insert(0, tree.item(selecteditem)['values'][8])




    fm = Frame(m, bg="#FFDAB9")
    fm.place(x=510, y=10, height=726, width=835)

    title = Label(fm, text='STAFF DETAILS', border=12, font=('Cambria', 20, 'bold'), relief=RIDGE, bg='#EECBAD')
    title.pack(side=TOP, fill=X)

    title2 = Label(fm, text='Enter details:', font=('Cambria', 20, 'bold'), bg="#FFDAB9")#BFEFFF
    title2.place(x=20, y=80)

    dtl2 = Label(fm, font=('Arial', 16, 'italic', 'bold'), border=8, relief='groove', bg='#EECBAD')
    dtl2.place(x=10, y=120, height=510, width=300)

    frm_right = Frame(fm, border=10, relief='groove', bg='#EECBAD')
    frm_right.place(x=320, y=120, height=510, width=500)

    btm_frm = Frame(frm_right, relief='groove', bd=6, bg='#EECBAD')
    btm_frm.place(x=10, y=50, height=430, width=460)

    vrtcl_scrl = Scrollbar(btm_frm, orient='vertical')
    hrzntl_scrl = Scrollbar(btm_frm, orient='horizontal')

    tree = ttk.Treeview(btm_frm,columns=('ID','Name', 'Gender', 'Address', 'Contact', 'DOB', 'Department', 'Hiredate', 'Salary'),yscrollcommand=vrtcl_scrl.set, xscrollcommand=hrzntl_scrl.set)

    vrtcl_scrl.config(command=tree.yview)
    hrzntl_scrl.config(command=tree.xview)

    vrtcl_scrl.pack(side='right', fill=Y)
    hrzntl_scrl.pack(side='bottom', fill=X)

    tree['show'] = 'headings'

    tree.column('ID', width= 60, anchor= CENTER)
    tree.column('Name', width=160, anchor= CENTER)
    tree.column('Gender', width=80, anchor= CENTER)
    tree.column('Address', width=180, anchor= CENTER)
    tree.column('Contact', width=120, anchor= CENTER)
    tree.column('DOB', width=100, anchor= CENTER)
    tree.column('Department', width=100, anchor= CENTER)
    tree.column('Hiredate', width=80, anchor= CENTER)
    tree.column('Salary', width=60, anchor= CENTER)

    tree.heading('ID', text= 'ID')
    tree.heading('Name', text='Name')
    tree.heading('Gender', text='Gender')
    tree.heading('Address', text='Address')
    tree.heading('Contact', text='Contact')
    tree.heading('DOB', text='DOB')
    tree.heading('Department', text='Department')
    tree.heading('Hiredate', text='Hiredate')
    tree.heading('Salary', text='Salary')

    tree.pack(fill='both', expand=True)
    query = 'select * from staff'
    mycursor.execute(query)
    all = mycursor.fetchall()
    for val in all:
        tree.insert(parent='', index='end', values=val)

    tree.bind("<<TreeviewSelect>>", display)

    staffid = Label(dtl2, text='ID', font=('Arial', 14, 'bold'), bg='#EECBAD')
    staffid.place(x=2, y=8)

    id_entry = Entry(dtl2, width=28)
    id_entry.place(x=100, y=12)

    name_lbl = Label(dtl2, text='Name', font=('Arial', 14, 'bold'), bg='#EECBAD')
    name_lbl.place(x=2, y=46)

    name_entry = Entry(dtl2, width=28)
    name_entry.place(x=100, y=48)

    gndr_lbl = Label(dtl2, text='Gender', font=('Arial', 14, 'bold'), bg='#EECBAD')
    gndr_lbl.place(x=2, y=84)

    gndr_entry = ttk.Combobox(dtl2, font=('Arial', 12), width=16, state='readonly')
    gndr_entry['values'] = ('Male', 'Female', 'Others')
    gndr_entry.place(x=100, y=88, height= 22)
    gndr_entry.set("select")

    add_lbl = Label(dtl2, text='Address', font=('Arial', 14, 'bold'), bg='#EECBAD')
    add_lbl.place(x=2, y=120)

    add_entry = Entry(dtl2, width=28)
    add_entry.place(x=100, y=126)

    cntct_lbl = Label(dtl2, text='Contact', font=('Arial', 14, 'bold'), bg='#EECBAD')
    cntct_lbl.place(x=2, y=160)

    cntct_entry = Entry(dtl2, width=28)
    cntct_entry.place(x=100, y=164)

    dob_lbl = Label(dtl2, text='DOB', font=('Arial', 14, 'bold'), bg='#EECBAD')
    dob_lbl.place(x=2, y=198)

    dob_cal = DateEntry(dtl2, setmode='day', date_pattern='dd/mm/yyyy', width=25)
    dob_cal.place(x=100, y=204)

    dptmnt_lbl = Label(dtl2, text='Department', font=('Arial', 14, 'bold'), bg='#EECBAD')
    dptmnt_lbl.place(x=2, y=238)

    dptmnt_entry = ttk.Combobox(dtl2, width=22, state='readonly')
    dptmnt_entry['values'] = ('Clerks', 'Electricians', 'Kitchen workers','Helper', 'Driver', 'Conductor')
    dptmnt_entry.place(x=120, y=244)
    dptmnt_entry.set("select")

    hiredate_lbl = Label(dtl2, text='Hiredate', font=('Arial', 14, 'bold'), bg='#EECBAD')
    hiredate_lbl.place(x=2, y=276)

    hired_cal = DateEntry(dtl2, setmode='day', date_pattern='dd/mm/yyyy', width=25)
    hired_cal.place(x=100, y=282)

    sal_lbl = Label(dtl2, text='Salary', font=('Arial', 14, 'bold'), bg='#EECBAD')
    sal_lbl.place(x=2, y=312)

    sal_entry = Entry(dtl2, width=28)
    sal_entry.place(x=100, y=320)

    add_btn = Button(dtl2, text='Add Record', font=('Arial', 14, 'bold'), bg='#CDAF95', width=10, command= add)
    add_btn.place(x=9, y=360)

    edit_btn = Button(dtl2, text='Edit Record', font=('Arial', 14, 'bold'), bg='#CDAF95', width=10, command= modify)
    edit_btn.place(x=148, y=360)

    dlt_btn = Button(dtl2, text='Delete Record', font=('Arial', 14, 'bold'), bg='#CDAF95', width=10, command= delete)
    dlt_btn.place(x=9, y=410)

    rst_btn = Button(dtl2, text='Reset all', font=('Arial', 14, 'bold'),command= clear ,bg='#CDAF95', width=10)
    rst_btn.place(x=148, y=410)

    srch_lbl = Label(frm_right, text='Search by Name', font=('Arial', 9, 'bold'), bg='#EECBAD')
    srch_lbl.place(x=2, y=10)

    srch_entry = Entry(frm_right, width=28)
    srch_entry.place(x=100, y=10)

    srch_btn = Button(frm_right, text='Search', font=('Arial', 8, 'bold'), width=10, bg='#CDAF95', command= search)
    srch_btn.place(x=300, y=8)

    clear_btn = Button(frm_right, text='Cancel', font=('Arial', 8, 'bold'), width=10, bg='#CDAF95', command= cancel)
    clear_btn.place(x=390, y=8)



def academics():
    def exit():
        opt.destroy()

    def junior():
        def add():
                if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not hindi_entry.get() or not maths_entry.get() or not social_entry.get() or not science_entry.get() or not computer_entry.get() or not gk_entry.get() or not art_entry.get():
                    mb.showerror('Error', 'All Fields are required')

                elif class_entry.get() >'5':
                    mb.showerror('Error', 'Record of class greater than 5 is not inserted here')


                else:
                    a = []
                    b = []
                    sql = "Select * from studdetails" \
                          " where admission_no= %s"
                    aa = [Ad_no_entry.get()]
                    mycursor.execute(sql, aa)
                    all = mycursor.fetchone()
                    a.append(all)

                    if a[0] == None:
                        mb.showerror("Error", f"No Record Found of {Ad_no_entry.get()}")

                    else:
                        for i in a[0]:
                            b.append(i)

                        if b[1] != name_entry.get():
                            mb.showerror("Error", "Invalid Name")

                        elif b[4]!= class_entry.get() or b[4] > '5':
                            mb.showerror("Error", "Class doesn't match")

                        else:
                            c= []
                            sql = "Select * from junior" \
                                  " where admission_no= %s"
                            aa = [Ad_no_entry.get()]
                            mycursor.execute(sql, aa)
                            all = mycursor.fetchone()
                            c.append(all)
                            if c[0]== None:
                                a = (Ad_no_entry.get(), eng_entry.get(), hindi_entry.get(), maths_entry.get(),
                                     social_entry.get(), science_entry.get(),
                                     computer_entry.get(), gk_entry.get(), art_entry.get())
                                query = "insert into junior values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                mycursor.execute(query, a)
                                main.commit()
                                tree.insert(parent='', index='end', values=(
                                Ad_no_entry.get(), name_entry.get(), class_entry.get(), eng_entry.get(),
                                hindi_entry.get(), maths_entry.get(), social_entry.get(), science_entry.get(),
                                computer_entry.get(), gk_entry.get(), art_entry.get()))
                                mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                            else:
                                mb.showerror("Error","Record already present")

        def clear():
            for widget in fm1.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, 'end')



        def modify():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not maths_entry.get() or not hindi_entry.get() or not social_entry.get() or not science_entry.get() or not computer_entry.get() or not gk_entry.get() or not art_entry.get():
                mb.showerror('Error', 'All Fields are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from junior where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    a = [eng_entry.get(), hindi_entry.get(), maths_entry.get(),
                         social_entry.get(),
                         science_entry.get(), computer_entry.get(), gk_entry.get(),art_entry.get(), Ad_no_entry.get()]
                    query = "Update junior set english=%s, hindi= %s, maths= %s, social_studies= %s, science= %s, computer= %s, gk= %s, arts= %s" \
                            "where ADMISSION_NO= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, j.english, j.hindi, j.maths, j.social_studies, j.science, j.computer, j.gk, j.arts from studdetails s, junior j where s.admission_no= j.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)

                    mb.showinfo('Modified', f'Record of {name_entry.get()} is modified')

                clear()

        def display(a):

            clear()
            selecteditem= tree.selection()[0]
            Ad_no_entry.insert(0, tree.item(selecteditem)['values'][0])
            name_entry.insert(0, tree.item(selecteditem)['values'][1])
            class_entry.insert(0 , tree.item(selecteditem)['values'][2])
            eng_entry.insert(0, tree.item(selecteditem)['values'][3])
            hindi_entry.insert(0, tree.item(selecteditem)['values'][4])
            maths_entry.insert(0, tree.item(selecteditem)['values'][5])
            social_entry.insert(0, tree.item(selecteditem)['values'][6])
            science_entry.insert(0, tree.item(selecteditem)['values'][7])
            computer_entry.insert(0, tree.item(selecteditem)['values'][8])
            gk_entry.insert(0, tree.item(selecteditem)['values'][9])
            art_entry.insert(0, tree.item(selecteditem)['values'][10])

            fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
            fm2.place(x=460, y=5, height=400, width=370)

            Label(fm2, text="Admission No :", font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=30)
            Label(fm2, text= tree.item(selecteditem)['values'][0], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=150, y=30)

            Label(fm2, text= 'Name            :', font= ('Arial', 15,'bold'), bg="#E6E6FA").place(x= 2, y= 60)
            Label(fm2, text=tree.item(selecteditem)['values'][1], bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=60)

            Label(fm2, text='Class            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=90)
            Label(fm2, text=tree.item(selecteditem)['values'][2], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=90)

            Label(fm2, text='English         :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=120)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][3]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=120)

            Label(fm2, text='Hindi            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=150)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][4]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=150)
            #
            Label(fm2, text='Mathematics :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=180)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][5]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=180)
            #
            Label(fm2, text='Social           :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=210)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][6]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=210)
            #
            Label(fm2, text='Science        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=240)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][7]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=240)

            Label(fm2, text='Computer     :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=270)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][8]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=270)

            Label(fm2, text='GK                :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=300)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][9]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=300)

            Label(fm2, text='Arts              :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=330)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][10]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=330)

            Frame(fm2, bg= 'black').place(x= 210, y= 85 , width= 4, height= 400)

            a= tree.item(selecteditem)['values'][3]+tree.item(selecteditem)['values'][4]+tree.item(selecteditem)['values'][5]+tree.item(selecteditem)['values'][6]+tree.item(selecteditem)['values'][7]+tree.item(selecteditem)['values'][8]+tree.item(selecteditem)['values'][9]+tree.item(selecteditem)['values'][10]
            Label(fm2, text= 'Total Marks :', font=('Arial', 15, 'bold'), bg="#E6E6FA" ).place(x= 215, y= 180)
            Label(fm2, text= f"{a}/800",  font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x=230,y=210)

            b= (a/800)*100
            b= str(b)
            Label(fm2,text= 'Percentage :', font=('Arial', 15, 'bold'), bg="#E6E6FA"  ).place(x= 215, y= 250)
            Label(fm2, text= f"{b[0:5]} %", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x= 230, y= 280)
            b= float(b)

            Label(fm2, text='Grade :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x= 215, y= 320)
            if b>=95:
                Label(fm2, text= 'A+', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=350)

            elif b<= 95 and b>= 90:
                Label(fm2, text='A1', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<=90 and b>= 80:
                Label(fm2, text='A2', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 80 and b>= 70:
                Label(fm2, text='B', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 70 and b>= 60:
                Label(fm2, text='C', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 60 and b>= 50:
                Label(fm2, text='D', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 50 and b>= 40:
                Label(fm2, text='E', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            else:
                Label(fm2, text='FAIL', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

        def delete():
            if not Ad_no_entry.get() or not class_entry.get() or not name_entry.get():
                mb.showerror('Error', 'Admission no,Name and Class are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from junior where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                        lst= [Ad_no_entry.get()]
                        query= 'delete from junior where admission_no= %s'
                        mycursor.execute(query, lst)
                        main.commit()
                        for item in tree.get_children():
                            tree.delete(item)

                        query = 'select s.admission_no,s.sname, s.sclass, j.english, j.hindi, j.maths, j.social_studies, j.science, j.computer, j.gk, j.arts from studdetails s, junior j where s.admission_no= j.admission_no;'
                        mycursor.execute(query)
                        all = mycursor.fetchall()
                        for val in all:
                            tree.insert(parent='', index='end', values=val)

                        mb.showinfo('Deleted', f'Record of {Ad_no_entry.get()} is Deleted')
                        clear()





        fm = Frame(m, bg="#4EEE94")
        fm.place(x=510, y=10, height=726, width=835)

        fm1 = Frame(fm, bg="light pink", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm1.place(x=5, y=5, height=400, width=450)

        Label(fm1, text='Admission no :', fg='black', bg='light pink', font=('Comic Sans MS', 14,'bold')).place(x=8, y=10)
        Ad_no_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        Ad_no_entry.place(x=150, y=14)

        Label(fm1, text='Name :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=40)
        name_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        name_entry.place(x=150, y=44)

        Label(fm1, text='Class :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=70)
        class_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        class_entry.place(x=150, y=74)

        Label(fm1, text='English :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=100)
        eng_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eng_entry.place(x=150, y=104)

        Label(fm1, text='Hindi :', fg='black', bg='light pink', font=('Comic Sans MS', 14,'bold' )).place(x=8, y=130)
        hindi_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        hindi_entry.place(x=150, y=134)

        Label(fm1, text='Maths :', fg='black', bg='light pink', font=('Comic Sans MS', 14,'bold')).place(x=8, y=160)
        maths_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        maths_entry.place(x=150, y=164)

        Label(fm1, text='Social :', fg='black', bg='light pink', font=('Comic Sans MS', 14,'bold')).place(x=8, y=190)
        social_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        social_entry.place(x=150, y=194)

        Label(fm1, text='Science :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=220)
        science_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        science_entry.place(x=150, y=224)

        Label(fm1, text='Computer :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=250)
        computer_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        computer_entry.place(x=150, y=254)

        Label(fm1, text='GK :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=280)
        gk_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        gk_entry.place(x=150, y=284)

        Label(fm1, text='Arts :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=310)
        art_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        art_entry.place(x=150, y=314)

        Button(fm1, text= 'Add Record',command= add ,font=('Comic Sans MS', 15, 'bold'),bg= "#f3e7fa" ).place(x= 310,y= 40, width= 125, height= 40)
        Button(fm1, text='Modify Record',command= modify, font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa").place(x=310, y=100, width=125,height=40)
        Button(fm1, text='Delete Record',command= delete, font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa").place(x=310, y=160, width=125,height=40)
        Button(fm1, text='Clear Field', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa", command= clear).place(x=310, y=220, width=125,height=40)


        fm3 = Frame(fm, bg='red', highlightthickness=4, highlightbackground='black')
        fm3.place(x=5, y=410, height=310, width=823)

        columns = ['Admission number', 'Name', 'Class', 'English', 'Hindi', 'Maths', 'Social', 'Science', 'Computer',
                   'Gk',
                   'Arts']
        tree = ttk.Treeview(fm3, columns=columns, height=100, selectmode=BROWSE)
        xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
        yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        tree.heading('Admission number', text='AD_NO', anchor=CENTER)
        tree.heading('Name', text='NAME', anchor=CENTER)
        tree.heading('Class', text='CLASS', anchor=CENTER)
        tree.heading('English', text='ENGLISH', anchor=CENTER)
        tree.heading('Hindi', text='HINDI', anchor=CENTER)
        tree.heading('Maths', text='MATHS', anchor=CENTER)
        tree.heading('Social', text='SOCIAL', anchor=CENTER)
        tree.heading('Science', text='SCIENCE', anchor=CENTER)
        tree.heading('Computer', text='COMPUTER', anchor=CENTER)
        tree.heading('Gk', text='GK', anchor=CENTER)
        tree.heading('Arts', text='ARTS', anchor=CENTER)

        tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

        tree.column('#0', width=20, stretch=NO)
        tree.column('#1', width=60, stretch=NO)
        tree.column('#2', width=160, stretch=NO)
        tree.column('#3', width=80, stretch=NO)
        tree.column('#4', width=100, stretch=NO)
        tree.column('#5', width=100, stretch=NO)
        tree.column('#6', width=100, stretch=NO)
        tree.column('#7', width=100, stretch=NO)
        tree.column('#8', width=100, stretch=NO)
        tree.column('#9', width=100, stretch=NO)
        tree.column('#10', width=100, stretch=NO)
        tree.column('#11', width=100, stretch=NO)

        query = 'select s.admission_no,s.sname, s.sclass, j.english, j.hindi, j.maths, j.social_studies, j.science, j.computer, j.gk, j.arts from studdetails s, junior j where s.admission_no= j.admission_no;'
        mycursor.execute(query)
        all = mycursor.fetchall()
        for val in all:
            tree.insert(parent='', index='end', values=val)

        tree.bind("<<TreeviewSelect>>", display)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)






    def middle():
        def add():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not maths_entry.get() or not hindi_entry.get() or not social_entry.get() or not science_entry.get() or not computer_entry.get() or not gk_entry.get() or not art_entry.get() or not sanskrit_entry.get():
                mb.showerror('Error', 'All Fields are required')

            else:
                a = []
                b = []
                sql = "Select * from studdetails" \
                      " where admission_no= %s"
                aa = [Ad_no_entry.get()]
                mycursor.execute(sql, aa)
                all = mycursor.fetchone()
                a.append(all)

                if a[0] == None:
                    mb.showerror("Error", f"No Record Found of {Ad_no_entry.get()}")

                elif class_entry.get() > '8' or class_entry.get() < '6':
                    mb.showerror('Error', 'Record of class greater than 8 and less than 6 is not inserted here')

                else:
                    for i in a[0]:
                        b.append(i)

                    if b[1] != name_entry.get():
                        mb.showerror("Error", "Invalid Name")

                    elif b[4] != class_entry.get():
                        mb.showerror("Error", "Class doesn't match")

                    elif b[4] < '6' or b[4] > '8':
                        mb.showerror('Error', 'Record of class greater than 8 and less than 6 is not inserted here')

                    else:
                        a = []
                        sql = "Select * from class6_8" \
                              " where admission_no= %s"
                        aa = [Ad_no_entry.get()]
                        mycursor.execute(sql, aa)
                        all = mycursor.fetchone()
                        a.append(all)

                        if a[0] == None:
                            a = (Ad_no_entry.get(), eng_entry.get(), hindi_entry.get(), maths_entry.get(),
                                 social_entry.get(), science_entry.get(), sanskrit_entry.get(),
                                 computer_entry.get(), gk_entry.get(), art_entry.get())
                            query = "insert into class6_8 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            mycursor.execute(query, a)
                            main.commit()
                            tree.insert(parent='', index='end',values=(Ad_no_entry.get(), name_entry.get(), class_entry.get(), eng_entry.get(),
                                                hindi_entry.get(), maths_entry.get(), social_entry.get(),
                                                science_entry.get(), sanskrit_entry.get(),
                                                computer_entry.get(), gk_entry.get(), art_entry.get()))
                            mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                        else:
                            mb.showerror('Error', 'Record already present')




        def clear():
                for widget in fm1.winfo_children():
                    if isinstance(widget, Entry):
                        widget.delete(0, 'end')




        def modify():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not maths_entry.get() or not hindi_entry.get() or not social_entry.get() or not science_entry.get() or not computer_entry.get() or not gk_entry.get() or not art_entry.get() or not sanskrit_entry.get():
                mb.showerror('Error', 'All Fields are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from class6_8 where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    a = [eng_entry.get(), hindi_entry.get(), maths_entry.get(),
                         social_entry.get(),
                         science_entry.get(),sanskrit_entry.get(), computer_entry.get(), gk_entry.get(),art_entry.get(), Ad_no_entry.get()]
                    query = "Update class6_8 set english=%s, hindi= %s, maths= %s, social_studies= %s, science= %s,sanskrit= %s, computer= %s, gk= %s, arts= %s" \
                            "where ADMISSION_NO= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, c.english, c.hindi, c.maths, c.social_studies, c.science,c.sanskrit, c.computer, c.gk, c.arts from studdetails s, class6_8 c where s.admission_no= c.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)

                    mb.showinfo('Modified', f'Record of {name_entry.get()} is modified')

                clear()

        def delete():
            if not Ad_no_entry.get() or not class_entry.get() or not name_entry.get():
                mb.showerror('Error', 'Admission no,Name and Class are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from class6_8 where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    lst = [Ad_no_entry.get()]
                    query = 'delete from class6_8 where admission_no= %s'
                    mycursor.execute(query, lst)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, c.english, c.hindi, c.maths, c.social_studies, c.science,c.sanskrit, c.computer, c.gk, c.arts from studdetails s, class6_8 c where s.admission_no= j.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)

                    mb.showinfo('Deleted', f'Record of {Ad_no_entry.get()} is Deleted')
                    clear()

        def display(a):
            clear()
            selecteditem= tree.selection()[0]
            Ad_no_entry.insert(0, tree.item(selecteditem)['values'][0])
            name_entry.insert(0, tree.item(selecteditem)['values'][1])
            class_entry.insert(0 , tree.item(selecteditem)['values'][2])
            eng_entry.insert(0, tree.item(selecteditem)['values'][3])
            hindi_entry.insert(0, tree.item(selecteditem)['values'][4])
            maths_entry.insert(0, tree.item(selecteditem)['values'][5])
            social_entry.insert(0, tree.item(selecteditem)['values'][6])
            science_entry.insert(0, tree.item(selecteditem)['values'][7])
            sanskrit_entry.insert(0, tree.item(selecteditem)['values'][8])
            computer_entry.insert(0, tree.item(selecteditem)['values'][9])
            gk_entry.insert(0, tree.item(selecteditem)['values'][10])
            art_entry.insert(0, tree.item(selecteditem)['values'][11])

            fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
            fm2.place(x=460, y=5, height=400, width=370)

            Label(fm2, text="Admission No :", font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=30)
            Label(fm2, text= tree.item(selecteditem)['values'][0], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=150, y=30)

            Label(fm2, text= 'Name            :', font= ('Arial', 15,'bold'), bg="#E6E6FA").place(x= 2, y= 60)
            Label(fm2, text=tree.item(selecteditem)['values'][1], bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=60)

            Label(fm2, text='Class            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=90)
            Label(fm2, text=tree.item(selecteditem)['values'][2], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=90)

            Label(fm2, text='English         :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=120)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][3]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=120)

            Label(fm2, text='Hindi            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=150)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][4]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=150)
            #
            Label(fm2, text='Mathematics :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=180)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][5]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=180)
            #
            Label(fm2, text='Social           :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=210)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][6]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=210)
            #
            Label(fm2, text='Science        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=240)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][7]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=240)

            Label(fm2, text='Sanskrit        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=270)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][8]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=270)

            Label(fm2, text='Computer     :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=300)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][9]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=300)

            Label(fm2, text='GK                :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=330)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][10]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=330)

            Label(fm2, text='Arts              :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=360)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][11]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=360)

            Frame(fm2, bg= 'black').place(x= 210, y= 40, width= 4, height= 400)

            a= tree.item(selecteditem)['values'][3]+tree.item(selecteditem)['values'][4]+tree.item(selecteditem)['values'][5]+tree.item(selecteditem)['values'][6]+tree.item(selecteditem)['values'][7]+tree.item(selecteditem)['values'][8]+tree.item(selecteditem)['values'][9]+tree.item(selecteditem)['values'][10]+tree.item(selecteditem)['values'][11]
            Label(fm2, text= 'Total Marks :', font=('Arial', 15, 'bold'), bg="#E6E6FA" ).place(x= 215, y= 180)
            Label(fm2, text= f"{a}/800",  font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x=230,y=210)

            b= (a/900)*100
            b= str(b)

            Label(fm2,text= 'Percentage :', font=('Arial', 15, 'bold'), bg="#E6E6FA"  ).place(x= 215, y= 250)
            Label(fm2, text= f"{b[0:5]} %", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x= 230, y= 280)
            b= float(b)

            Label(fm2, text='Grade :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x= 215, y= 320)
            if b>=95:
                Label(fm2, text= 'A+', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=350)

            elif b<= 95 and b>= 90:
                Label(fm2, text='A1', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<=90 and b>= 80:
                Label(fm2, text='A2', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 80 and b>= 70:
                Label(fm2, text='B', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 70 and b>= 60:
                Label(fm2, text='C', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 60 and b>= 50:
                Label(fm2, text='D', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 50 and b>= 40:
                Label(fm2, text='E', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            else:
                Label(fm2, text='FAIL', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)




        fm = Frame(m, bg="#4EEE94")
        fm.place(x=510, y=10, height=726, width=835)

        fm1 = Frame(fm, bg="light pink", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm1.place(x=5, y=5, height=400, width=450)

        Label(fm1, text='Admission no :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,                                                                                                        y=10)
        Ad_no_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        Ad_no_entry.place(x=150, y=14)

        Label(fm1, text='Name :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=40)
        name_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        name_entry.place(x=150, y=44)

        Label(fm1, text='Class :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=70)
        class_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        class_entry.place(x=150, y=74)

        Label(fm1, text='English :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=100)
        eng_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eng_entry.place(x=150, y=104)

        Label(fm1, text='Hindi :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=130)
        hindi_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        hindi_entry.place(x=150, y=134)

        Label(fm1, text='Maths :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=160)
        maths_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        maths_entry.place(x=150, y=164)

        Label(fm1, text='Social :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=190)
        social_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        social_entry.place(x=150, y=194)

        Label(fm1, text='Science :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=220)
        science_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        science_entry.place(x=150, y=224)

        Label(fm1, text='Sanskrit :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=250)
        sanskrit_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        sanskrit_entry.place(x=150, y=254)

        Label(fm1, text='Computer :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=280)
        computer_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        computer_entry.place(x=150, y=284)

        Label(fm1, text='GK :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=310)
        gk_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        gk_entry.place(x=150, y=314)

        Label(fm1, text='Arts :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=340)
        art_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        art_entry.place(x=150, y=344)

        Button(fm1, text='Add Record',command= add,font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa").place(x=310, y=40, width=125, height=40)
        Button(fm1, text='Modify Record',command=modify, font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa").place(x=310, y=100,width=125, height=40)
        Button(fm1, text='Delete Record',command=delete, font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa").place(x=310, y=160,width=125, height=40)
        Button(fm1, text='Clear Field',command= clear, font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa").place(x=310, y=220, width=125,height=40)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)

        fm3 = Frame(fm, bg='yellow', highlightthickness=4, highlightbackground='black')
        fm3.place(x=5, y=410, height=310, width=823)

        columns = ['Admission number', 'Name', 'Class', 'English', 'Hindi', 'Maths', 'Social', 'Science','Sanskrit', 'Computer', 'GK',
                   'Arts']
        tree = ttk.Treeview(fm3, columns=columns, height=100, selectmode=BROWSE)
        xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
        yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        tree.heading('Admission number', text='AD_NO', anchor=CENTER)
        tree.heading('Name', text='NAME', anchor=CENTER)
        tree.heading('Class', text='CLASS', anchor=CENTER)
        tree.heading('English', text='ENGLISH', anchor=CENTER)
        tree.heading('Hindi', text='HINDI', anchor=CENTER)
        tree.heading('Maths', text='MATHS', anchor=CENTER)
        tree.heading('Social', text='SOCIAL', anchor=CENTER)
        tree.heading('Science', text='SCIENCE', anchor=CENTER)
        tree.heading('Sanskrit', text='SANSKRIT', anchor=CENTER)
        tree.heading('Computer', text='COMPUTER', anchor=CENTER)
        tree.heading('GK', text='GK', anchor=CENTER)
        tree.heading('Arts', text='ARTS', anchor=CENTER)

        tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

        tree.column('#0', width=20, stretch=NO, anchor= CENTER)
        tree.column('#1', width=60, stretch=NO, anchor= CENTER)
        tree.column('#2', width=160, stretch=NO, anchor= CENTER)
        tree.column('#3', width=80, stretch=NO, anchor= CENTER)
        tree.column('#4', width=100, stretch=NO, anchor= CENTER)
        tree.column('#5', width=100, stretch=NO, anchor= CENTER)
        tree.column('#6', width=100, stretch=NO, anchor= CENTER)
        tree.column('#7', width=100, stretch=NO, anchor= CENTER)
        tree.column('#8', width=100, stretch=NO, anchor= CENTER)
        tree.column('#9', width=100, stretch=NO, anchor= CENTER)
        tree.column('#10', width=100, stretch=NO, anchor= CENTER)
        tree.column('#11', width=100, stretch=NO, anchor= CENTER)
        tree.column('#12', width=100, stretch=NO, anchor= CENTER)

        query = 'select s.admission_no,s.sname, s.sclass, c.english, c.hindi, c.maths, c.social_studies, c.science,c.sanskrit, c.computer, c.gk, c.arts from studdetails s, class6_8 c  where s.admission_no= c.admission_no;'
        mycursor.execute(query)
        all = mycursor.fetchall()
        for val in all:
            tree.insert(parent='', index='end', values=val)


        tree.bind("<<TreeviewSelect>>", display)





    def class9_10():
        def add():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not maths_entry.get() or not hindi_entry.get() or not social_entry.get() or not science_entry.get() or not computer_entry.get() or not gs_entry.get() :
                mb.showerror('Error', 'All Fields are required')

            else:
                a = []
                b = []
                sql = "Select * from studdetails" \
                      " where admission_no= %s"
                aa = [Ad_no_entry.get()]
                mycursor.execute(sql, aa)
                all = mycursor.fetchone()
                a.append(all)

                if a[0] == None:
                    mb.showerror("Error", f"No Record Found of {Ad_no_entry.get()}")

                elif int(class_entry.get()) > 10 or int(class_entry.get()) < 9:
                    mb.showerror('Error', 'Record of class greater than 10 and less than 9 is not inserted here')


                else:
                    for i in a[0]:
                        b.append(i)

                    if b[1] != name_entry.get():
                        mb.showerror("Error", "Invalid Name")

                    elif b[4] != class_entry.get():
                        mb.showerror("Error", "Class doesn't match")

                    else:
                        a = []
                        sql = "Select * from class9_10" \
                              " where admission_no= %s"
                        aa = [Ad_no_entry.get()]
                        mycursor.execute(sql, aa)
                        all = mycursor.fetchone()
                        a.append(all)

                        if a[0] == None:
                            a = (Ad_no_entry.get(), eng_entry.get(), hindi_entry.get(), maths_entry.get(),
                                 social_entry.get(), science_entry.get(),
                                 computer_entry.get(), gs_entry.get())
                            query = "insert into class9_10 values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            mycursor.execute(query, a)
                            main.commit()
                            tree.insert(parent='', index='end',
                                        values=(Ad_no_entry.get(), name_entry.get(), class_entry.get(), eng_entry.get(),
                                                hindi_entry.get(), maths_entry.get(), social_entry.get(),
                                                science_entry.get(),
                                                computer_entry.get(), gs_entry.get()))
                            mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                        else:
                            mb.showerror('Error', 'Record Already Present')



        def clear():
            for widget in fm1.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, 'end')




        def modify():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not maths_entry.get() or not hindi_entry.get() or not social_entry.get() or not science_entry.get() or not computer_entry.get() or not gs_entry.get() :
                mb.showerror('Error', 'All Fields are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from class9_10 where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    a = [eng_entry.get(), hindi_entry.get(), maths_entry.get(),
                         social_entry.get(),
                         science_entry.get(), computer_entry.get(), gs_entry.get(), Ad_no_entry.get()]
                    query = "Update class9_10 set english=%s, hindi= %s, mathematics= %s, social= %s, science= %s, computer= %s, gs= %s" \
                            "where ADMISSION_NO= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, c.english, c.hindi, c.mathematics, c.social, c.science, c.computer, c.gs from studdetails s, class9_10 c where s.admission_no= c.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)

                    mb.showinfo('Modified', f'Record of {name_entry.get()} is modified')

                clear()

        def delete():
            if not Ad_no_entry.get() or not class_entry.get() or not name_entry.get():
                mb.showerror('Error', 'Admission no,Name and Class are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from class9_10 where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    lst = [Ad_no_entry.get()]
                    query = 'delete from class9_10 where admission_no= %s'
                    mycursor.execute(query, lst)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, c.english, c.hindi, c.maths, c.social_studies, c.science, c.computer, c.gk from studdetails s, class9_10 c where s.admission_no= c.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)
                    mb.showinfo('Deleted', f'Record of {Ad_no_entry.get()} is Deleted')
                    clear()

        def display(a):
            clear()
            selecteditem= tree.selection()[0]
            Ad_no_entry.insert(0, tree.item(selecteditem)['values'][0])
            name_entry.insert(0, tree.item(selecteditem)['values'][1])
            class_entry.insert(0 , tree.item(selecteditem)['values'][2])
            eng_entry.insert(0, tree.item(selecteditem)['values'][3])
            hindi_entry.insert(0, tree.item(selecteditem)['values'][4])
            maths_entry.insert(0, tree.item(selecteditem)['values'][5])
            social_entry.insert(0, tree.item(selecteditem)['values'][6])
            science_entry.insert(0, tree.item(selecteditem)['values'][7])
            computer_entry.insert(0, tree.item(selecteditem)['values'][8])
            gs_entry.insert(0, tree.item(selecteditem)['values'][9])


            fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
            fm2.place(x=460, y=5, height=400, width=370)

            Label(fm2, text="Admission No :", font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=30)
            Label(fm2, text= tree.item(selecteditem)['values'][0], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=150, y=30)

            Label(fm2, text= 'Name            :', font= ('Arial', 15,'bold'), bg="#E6E6FA").place(x= 2, y= 60)
            Label(fm2, text=tree.item(selecteditem)['values'][1], bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=60)

            Label(fm2, text='Class            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=90)
            Label(fm2, text=tree.item(selecteditem)['values'][2], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=90)

            Label(fm2, text='English         :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=120)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][3]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=120)

            Label(fm2, text='Hindi            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=150)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][4]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=150)
            #
            Label(fm2, text='Mathematics :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=180)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][5]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=180)
            #
            Label(fm2, text='Social           :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=210)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][6]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=210)
            #
            Label(fm2, text='Science        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=240)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][7]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=240)

            Label(fm2, text='Computer        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=270)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][8]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=270)

            Label(fm2, text='GS     :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=300)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][9]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=300)


            Frame(fm2, bg= 'black').place(x= 210, y= 40, width= 4, height= 400)

            a= tree.item(selecteditem)['values'][3]+tree.item(selecteditem)['values'][4]+tree.item(selecteditem)['values'][5]+tree.item(selecteditem)['values'][6]+tree.item(selecteditem)['values'][7]+tree.item(selecteditem)['values'][8]+tree.item(selecteditem)['values'][9]
            Label(fm2, text= 'Total Marks :', font=('Arial', 15, 'bold'), bg="#E6E6FA" ).place(x= 215, y= 180)
            Label(fm2, text= f"{a}/700",  font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x=230,y=210)

            b= (a/700)*100
            b= str(b)
            Label(fm2,text= 'Percentage :', font=('Arial', 15, 'bold'), bg="#E6E6FA"  ).place(x= 215, y= 250)
            Label(fm2, text= f"{b[0:5]} %", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x= 230, y= 280)
            b= float(b)

            Label(fm2, text='Grade :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x= 215, y= 320)
            if b>=95:
                Label(fm2, text= 'A+', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=350)

            elif b<= 95 and b>= 90:
                Label(fm2, text='A1', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<=90 and b>= 80:
                Label(fm2, text='A2', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 80 and b>= 70:
                Label(fm2, text='B', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 70 and b>= 60:
                Label(fm2, text='C', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 60 and b>= 50:
                Label(fm2, text='D', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 50 and b>= 40:
                Label(fm2, text='E', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            else:
                Label(fm2, text='FAIL', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)



        fm = Frame(m, bg="#4EEE94")
        fm.place(x=510, y=10, height=726, width=835)

        fm1 = Frame(fm, bg="light pink", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm1.place(x=5, y=5, height=400, width=450)

        Label(fm1, text='Admission no :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,y=10)
        Ad_no_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        Ad_no_entry.place(x=150, y=14)

        Label(fm1, text='Name :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=40)
        name_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        name_entry.place(x=150, y=44)

        Label(fm1, text='Class :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=70)
        class_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        class_entry.place(x=150, y=74)

        Label(fm1, text='English :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=100)
        eng_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eng_entry.place(x=150, y=104)

        Label(fm1, text='Hindi :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=130)
        hindi_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        hindi_entry.place(x=150, y=134)

        Label(fm1, text='Maths :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=160)
        maths_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        maths_entry.place(x=150, y=164)

        Label(fm1, text='Social :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=190)
        social_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        social_entry.place(x=150, y=194)

        Label(fm1, text='Science :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=220)
        science_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        science_entry.place(x=150, y=224)

        Label(fm1, text='Computer :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=250)
        computer_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        computer_entry.place(x=150, y=254)

        Label(fm1, text='GS :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=280)
        gs_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        gs_entry.place(x=150, y=284)

        Button(fm1, text='Add Record', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa", command= add).place(x=310, y=40,width=125,height=40)
        Button(fm1, text='Modify Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa", command= modify).place(x=310,y=100,width=125,height=40)
        Button(fm1, text='Delete Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa", command= delete).place(x=310,y=160,width=125,height=40)
        Button(fm1, text='Clear Field', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command= clear).place(x=310,y=220,width=125,height=40)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)

        fm3 = Frame(fm, bg='yellow', highlightthickness=4, highlightbackground='black')
        fm3.place(x=5, y=410, height=310, width=823)

        columns = ['Admission number', 'Name', 'Class', 'English', 'Hindi', 'Maths', 'Social', 'Science','Computer', 'GS']
        tree = ttk.Treeview(fm3, columns=columns, height=100, selectmode=BROWSE)
        xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
        yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        tree.heading('Admission number', text='AD_NO', anchor=CENTER)
        tree.heading('Name', text='NAME', anchor=CENTER)
        tree.heading('Class', text='CLASS', anchor=CENTER)
        tree.heading('English', text='ENGLISH', anchor=CENTER)
        tree.heading('Hindi', text='HINDI', anchor=CENTER)
        tree.heading('Maths', text='MATHS', anchor=CENTER)
        tree.heading('Social', text='SOCIAL', anchor=CENTER)
        tree.heading('Science', text='SCIENCE', anchor=CENTER)
        tree.heading('Computer', text='COMPUTER', anchor=CENTER)
        tree.heading('GS', text='GS', anchor=CENTER)

        tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

        tree.column('#0', width=0, stretch=NO, anchor= CENTER)
        tree.column('#1', width=60, stretch=NO, anchor= CENTER)
        tree.column('#2', width=160, stretch=NO, anchor= CENTER)
        tree.column('#3', width=80, stretch=NO, anchor= CENTER)
        tree.column('#4', width=100, stretch=NO, anchor= CENTER)
        tree.column('#5', width=100, stretch=NO, anchor= CENTER)
        tree.column('#6', width=100, stretch=NO, anchor= CENTER)
        tree.column('#7', width=100, stretch=NO, anchor= CENTER)
        tree.column('#8', width=100, stretch=NO, anchor= CENTER)
        tree.column('#9', width=100, stretch=NO, anchor= CENTER)
        tree.column('#10', width=100, stretch=NO, anchor= CENTER)

        query = 'select s.admission_no,s.sname, s.sclass, c.english, c.hindi, c.mathematics, c.social, c.science, c.computer, c.gs from studdetails s, class9_10 c  where s.admission_no= c.admission_no;'
        mycursor.execute(query)
        all = mycursor.fetchall()
        for val in all:
            tree.insert(parent='', index='end', values=val)

        tree.bind("<<TreeviewSelect>>", display)

    def maths():
        def add():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not maths_entry.get()  or not gs_entry.get() or not physics_entry.get() or not chemistry_entry.get() or not opt_entry.get() or not add_entry.get() :
                mb.showerror('Error', 'All Fields are required')

            else:
                a = []
                b = []
                sql = "Select * from studdetails" \
                      " where admission_no= %s"
                aa = [Ad_no_entry.get()]
                mycursor.execute(sql, aa)
                all = mycursor.fetchone()
                a.append(all)

                if a[0] == None:
                    mb.showerror("Error", f"No Record Found of {Ad_no_entry.get()}")

                elif int(class_entry.get()) > 12 or int(class_entry.get()) < 11:
                    mb.showerror('Error', 'Record of class greater than 12 and less than 11 is not inserted here')


                else:
                    for i in a[0]:
                        b.append(i)

                    if b[1] != name_entry.get():
                        mb.showerror("Error", "Invalid Name")

                    elif b[4] != class_entry.get():
                        mb.showerror("Error", "Class doesn't match")

                    elif b[12]!= 'Science with Maths':
                        mb.showerror('Error', 'Stream is not Maths')

                    else:
                        a = []
                        sql = "Select * from maths" \
                              " where admission_no= %s"
                        aa = [Ad_no_entry.get()]
                        mycursor.execute(sql, aa)
                        all = mycursor.fetchone()
                        a.append(all)

                        if a[0] == None:
                            a = (Ad_no_entry.get(), eng_entry.get(),physics_entry.get(),chemistry_entry.get(), maths_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get())
                            query = "insert into maths values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            mycursor.execute(query, a)
                            main.commit()
                            tree.insert(parent='', index='end',
                                        values=(Ad_no_entry.get(),name_entry.get(),class_entry.get(), eng_entry.get(),physics_entry.get(),chemistry_entry.get(), maths_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get()))
                            mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                        else:
                            mb.showerror('Error', 'Record Already Present')



        def clear():
            for widget in fm1.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, 'end')




        def modify():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not maths_entry.get() or not gs_entry.get() or not physics_entry.get() or not chemistry_entry.get() or not opt_entry.get() or not add_entry.get():
                mb.showerror('Error', 'All Fields are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from maths where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    a = [eng_entry.get(),physics_entry.get(),chemistry_entry.get(), maths_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get(),Ad_no_entry.get()]
                    query = "Update maths set english=%s,physics= %s, chemistry= %s, maths= %s,optional= %s,additional= %s, gs= %s" \
                            "where ADMISSION_NO= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, m.english, m.physics, m.chemistry, m.maths,m.optional, m.additional, m.gs from studdetails s, maths m  where s.admission_no= m.admission_no;'
                    mycursor.execute(query)
                    all_records = mycursor.fetchall()

                    for record in all_records:
                        tree.insert(parent='', index='end', values=record)

                    mb.showinfo('Modified', f'Record of {name_entry.get()} is modified')

                clear()

        def delete():
            if not Ad_no_entry.get() or not class_entry.get() or not name_entry.get():
                mb.showerror('Error', 'Admission no,Name and Class are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from maths where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    lst = [Ad_no_entry.get()]
                    query = 'delete from maths where admission_no= %s'
                    mycursor.execute(query, lst)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, m.english,m.physics,m.chemistry, m.maths,m.optional,m.addtional, m.gs from studdetails s, maths m where s.admission_no= m.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)
                    mb.showinfo('Deleted', f'Record of {Ad_no_entry.get()} is Deleted')
                    clear()

        def display(a):
            clear()
            selecteditem= tree.selection()[0]
            Ad_no_entry.insert(0, tree.item(selecteditem)['values'][0])
            name_entry.insert(0, tree.item(selecteditem)['values'][1])
            class_entry.insert(0 , tree.item(selecteditem)['values'][2])
            eng_entry.insert(0, tree.item(selecteditem)['values'][3])
            physics_entry.insert(0, tree.item(selecteditem)['values'][4])
            chemistry_entry.insert(0, tree.item(selecteditem)['values'][5])
            maths_entry.insert(0, tree.item(selecteditem)['values'][6])
            opt_entry.insert(0, tree.item(selecteditem)['values'][7])
            add_entry.insert(0, tree.item(selecteditem)['values'][8])
            gs_entry.insert(0, tree.item(selecteditem)['values'][9])


            fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
            fm2.place(x=460, y=5, height=400, width=370)

            Label(fm2, text="Admission No :", font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=30)
            Label(fm2, text= tree.item(selecteditem)['values'][0], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=150, y=30)

            Label(fm2, text= 'Name            :', font= ('Arial', 15,'bold'), bg="#E6E6FA").place(x= 2, y= 60)
            Label(fm2, text=tree.item(selecteditem)['values'][1], bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=60)

            Label(fm2, text='Class            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=90)
            Label(fm2, text=tree.item(selecteditem)['values'][2], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=90)

            Label(fm2, text='English         :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=120)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][3]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=120)

            Label(fm2, text='Physics            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=150)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][4]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=150)

            Label(fm2, text='Chemistry :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=180)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][5]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=180)

            Label(fm2, text='Mathematics           :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=210)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][6]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=210)

            Label(fm2, text='Optional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=240)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][7]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=240)

            Label(fm2, text='Additional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=270)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][8]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=270)

            Label(fm2, text='GS     :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=300)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][9]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=300)


            Frame(fm2, bg= 'black').place(x= 210, y= 80, width= 4, height= 400)

            a= tree.item(selecteditem)['values'][3]+tree.item(selecteditem)['values'][4]+tree.item(selecteditem)['values'][5]+tree.item(selecteditem)['values'][6]+tree.item(selecteditem)['values'][7]+tree.item(selecteditem)['values'][8]+tree.item(selecteditem)['values'][9]
            Label(fm2, text= 'Total Marks :', font=('Arial', 15, 'bold'), bg="#E6E6FA" ).place(x= 215, y= 180)
            Label(fm2, text= f"{a}/700",  font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x=230,y=210)

            b= (a/700)*100
            b= str(b)
            Label(fm2,text= 'Percentage :', font=('Arial', 15, 'bold'), bg="#E6E6FA"  ).place(x= 215, y= 250)
            Label(fm2, text= f"{b[0:5]} %", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x= 230, y= 280)
            b= float(b)

            Label(fm2, text='Grade :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x= 215, y= 320)
            if b>=95:
                Label(fm2, text= 'A+', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=350)

            elif b<= 95 and b>= 90:
                Label(fm2, text='A1', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<=90 and b>= 80:
                Label(fm2, text='A2', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 80 and b>= 70:
                Label(fm2, text='B', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 70 and b>= 60:
                Label(fm2, text='C', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 60 and b>= 50:
                Label(fm2, text='D', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 50 and b>= 40:
                Label(fm2, text='E', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            else:
                Label(fm2, text='FAIL', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)



        fm = Frame(m, bg="#4EEE94")
        fm.place(x=510, y=10, height=726, width=835)

        fm1 = Frame(fm, bg="light pink", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm1.place(x=5, y=5, height=400, width=450)

        Label(fm1, text='Admission no :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,y=40)
        Ad_no_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        Ad_no_entry.place(x=150, y=44)

        Label(fm1, text='Name :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=70)
        name_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        name_entry.place(x=150, y=74)

        Label(fm1, text='Class :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=100)
        class_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        class_entry.place(x=150, y=104)

        Label(fm1, text='English :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=130)
        eng_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eng_entry.place(x=150, y=134)

        Label(fm1, text='Physics :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=160)
        physics_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        physics_entry.place(x=150, y=164)

        Label(fm1, text='Chemistry :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=190)
        chemistry_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        chemistry_entry.place(x=150, y=194)

        Label(fm1, text='Maths :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=220)
        maths_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        maths_entry.place(x=150, y=224)

        Label(fm1, text='Optional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=250)
        opt_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        opt_entry.place(x=150, y=254)

        Label(fm1, text='Additional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=280)
        add_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        add_entry.place(x=150, y=284)

        Label(fm1, text='GS :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=310)
        gs_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        gs_entry.place(x=150, y=314)

        Button(fm1, text='Add Record', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command= add).place(x=310, y=70, width=125,height=40)
        Button(fm1, text='Modify Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= modify).place(x=310, y=130,width=125, height=40)
        Button(fm1, text='Delete Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= delete).place(x=310, y=190,width=125, height=40)
        Button(fm1, text='Clear Field', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command= clear).place(x=310, y=250, width=125,height=40)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)

        fm3 = Frame(fm, bg='yellow', highlightthickness=4, highlightbackground='black')
        fm3.place(x=5, y=410, height=310, width=823)

        columns = ['Admission number', 'Name', 'Class', 'English','Physics','Chemistry',  'Maths','Opt', 'Add' ,'GS']
        tree = ttk.Treeview(fm3, columns=columns, height=100, selectmode=BROWSE)
        xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
        yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        tree.heading('Admission number', text='AD_NO', anchor=CENTER)
        tree.heading('Name', text='NAME', anchor=CENTER)
        tree.heading('Class', text='CLASS', anchor=CENTER)
        tree.heading('English', text='ENGLISH', anchor=CENTER)
        tree.heading('Physics', text='PHYSICS', anchor=CENTER)
        tree.heading('Chemistry', text='CHEMISTRY', anchor=CENTER)
        tree.heading('Maths', text='MATHS', anchor=CENTER)
        tree.heading('Opt', text='OPTIONAL', anchor=CENTER)
        tree.heading('Add', text='ADDITIONAL', anchor=CENTER)
        tree.heading('GS', text='GS', anchor=CENTER)


        tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

        tree.column('#0', width=0, stretch=NO, anchor=CENTER)
        tree.column('Admission number', width=60, stretch=NO, anchor=CENTER)
        tree.column('Name', width=160, stretch=NO, anchor=CENTER)
        tree.column('Class', width=80, stretch=NO, anchor=CENTER)
        tree.column('English', width=100, stretch=NO, anchor=CENTER)
        tree.column('Physics', width=100, stretch=NO, anchor=CENTER)
        tree.column('Chemistry', width=100, stretch=NO, anchor=CENTER)
        tree.column('Maths', width=100, stretch=NO, anchor=CENTER)
        tree.column('Opt', width=100, stretch=NO, anchor=CENTER)
        tree.column('Add', width=100, stretch=NO, anchor=CENTER)
        tree.column('GS', width=100, stretch=NO, anchor=CENTER)

        # Assuming you have a database connection and cursor (mycursor)
        query = 'select s.admission_no,s.sname, s.sclass, m.english, m.physics, m.chemistry, m.maths,m.optional, m.additional, m.gs from studdetails s, maths m  where s.admission_no= m.admission_no;'
        mycursor.execute(query)
        all_records = mycursor.fetchall()

        for record in all_records:
            tree.insert(parent='', index='end', values=record)

        tree.bind("<<TreeviewSelect>>", display)


        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)

    def bio():
        def add():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not bio_entry.get()  or not gs_entry.get() or not physics_entry.get() or not chemistry_entry.get() or not opt_entry.get() or not add_entry.get() :
                mb.showerror('Error', 'All Fields are required')

            else:
                a = []
                b = []
                sql = "Select * from studdetails" \
                      " where admission_no= %s"
                aa = [Ad_no_entry.get()]
                mycursor.execute(sql, aa)
                all = mycursor.fetchone()
                a.append(all)

                if a[0] == None:
                    mb.showerror("Error", f"No Record Found of {Ad_no_entry.get()}")

                elif int(class_entry.get()) > 12 or int(class_entry.get()) < 11:
                    mb.showerror('Error', 'Record of class greater than 12 and less than 11 is not inserted here')


                else:
                    for i in a[0]:
                        b.append(i)

                    if b[1] != name_entry.get():
                        mb.showerror("Error", "Invalid Name")

                    elif b[4] != class_entry.get():
                        mb.showerror("Error", "Class doesn't match")

                    elif b[12]!= 'Science with Bio':
                        mb.showerror('Error', 'Stream is not Biology')

                    else:
                        a = []
                        sql = "Select * from biology" \
                              " where admission_no= %s"
                        aa = [Ad_no_entry.get()]
                        mycursor.execute(sql, aa)
                        all = mycursor.fetchone()
                        a.append(all)

                        if a[0] == None:
                            a = (Ad_no_entry.get(), eng_entry.get(),physics_entry.get(),chemistry_entry.get(), bio_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get())
                            query = "insert into biology values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            mycursor.execute(query, a)
                            main.commit()
                            tree.insert(parent='', index='end',
                                        values=(Ad_no_entry.get(),name_entry.get(),class_entry.get(), eng_entry.get(),physics_entry.get(),chemistry_entry.get(), bio_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get()))
                            mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                        else:
                            mb.showerror('Error', 'Record Already Present')



        def clear():
            for widget in fm1.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, 'end')




        def modify():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not bio_entry.get() or not gs_entry.get() or not physics_entry.get() or not chemistry_entry.get() or not opt_entry.get() or not add_entry.get():
                mb.showerror('Error', 'All Fields are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from biology where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    a = [eng_entry.get(),physics_entry.get(),chemistry_entry.get(), bio_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get(),Ad_no_entry.get()]
                    query = "Update biology set english=%s,physics= %s, chemistry= %s, biology= %s,optional= %s,additional= %s, gs= %s" \
                            "where ADMISSION_NO= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, b.english, b.physics, b.chemistry, b.biology,b.optional, b.additional, b.gs from studdetails s, biology b  where s.admission_no= b.admission_no;'
                    mycursor.execute(query)
                    all_records = mycursor.fetchall()

                    for record in all_records:
                        tree.insert(parent='', index='end', values=record)

                    mb.showinfo('Modified', f'Record of {name_entry.get()} is modified')

                clear()

        def delete():
            if not Ad_no_entry.get() or not class_entry.get() or not name_entry.get():
                mb.showerror('Error', 'Admission no,Name and Class are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from biology where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    lst = [Ad_no_entry.get()]
                    query = 'delete from biology where admission_no= %s'
                    mycursor.execute(query, lst)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, b.english, b.physics, b.chemistry, b.biology,b.optional, b.additional, b.gs from studdetails s, biology b  where s.admission_no= b.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)
                    mb.showinfo('Deleted', f'Record of {Ad_no_entry.get()} is Deleted')
                    clear()

        def display(a):
            clear()
            selecteditem= tree.selection()[0]
            Ad_no_entry.insert(0, tree.item(selecteditem)['values'][0])
            name_entry.insert(0, tree.item(selecteditem)['values'][1])
            class_entry.insert(0 , tree.item(selecteditem)['values'][2])
            eng_entry.insert(0, tree.item(selecteditem)['values'][3])
            physics_entry.insert(0, tree.item(selecteditem)['values'][4])
            chemistry_entry.insert(0, tree.item(selecteditem)['values'][5])
            bio_entry.insert(0, tree.item(selecteditem)['values'][6])
            opt_entry.insert(0, tree.item(selecteditem)['values'][7])
            add_entry.insert(0, tree.item(selecteditem)['values'][8])
            gs_entry.insert(0, tree.item(selecteditem)['values'][9])


            fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
            fm2.place(x=460, y=5, height=400, width=370)

            Label(fm2, text="Admission No :", font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=30)
            Label(fm2, text= tree.item(selecteditem)['values'][0], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=150, y=30)

            Label(fm2, text= 'Name            :', font= ('Arial', 15,'bold'), bg="#E6E6FA").place(x= 2, y= 60)
            Label(fm2, text=tree.item(selecteditem)['values'][1], bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=60)

            Label(fm2, text='Class            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=90)
            Label(fm2, text=tree.item(selecteditem)['values'][2], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=90)

            Label(fm2, text='English         :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=120)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][3]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=120)

            Label(fm2, text='Physics            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=150)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][4]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=150)
            #
            Label(fm2, text='Chemistry :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=180)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][5]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=180)
            #
            Label(fm2, text='Biology           :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=210)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][6]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=210)
            #
            Label(fm2, text='Optional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=240)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][7]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=240)

            Label(fm2, text='Additional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=270)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][8]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=270)

            Label(fm2, text='GS     :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=300)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][9]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=300)


            Frame(fm2, bg= 'black').place(x= 210, y= 80, width= 4, height= 400)

            a= tree.item(selecteditem)['values'][3]+tree.item(selecteditem)['values'][4]+tree.item(selecteditem)['values'][5]+tree.item(selecteditem)['values'][6]+tree.item(selecteditem)['values'][7]+tree.item(selecteditem)['values'][8]+tree.item(selecteditem)['values'][9]
            Label(fm2, text= 'Total Marks :', font=('Arial', 15, 'bold'), bg="#E6E6FA" ).place(x= 215, y= 180)
            Label(fm2, text= f"{a}/700",  font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x=230,y=210)

            b= (a/700)*100
            b= str(b)
            Label(fm2,text= 'Percentage :', font=('Arial', 15, 'bold'), bg="#E6E6FA"  ).place(x= 215, y= 250)
            Label(fm2, text= f"{b[0:5]} %", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x= 230, y= 280)
            b= float(b)

            Label(fm2, text='Grade :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x= 215, y= 320)
            if b>=95:
                Label(fm2, text= 'A+', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=350)

            elif b<= 95 and b>= 90:
                Label(fm2, text='A1', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<=90 and b>= 80:
                Label(fm2, text='A2', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 80 and b>= 70:
                Label(fm2, text='B', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 70 and b>= 60:
                Label(fm2, text='C', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 60 and b>= 50:
                Label(fm2, text='D', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 50 and b>= 40:
                Label(fm2, text='E', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            else:
                Label(fm2, text='FAIL', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)



        fm = Frame(m, bg="#4EEE94")
        fm.place(x=510, y=10, height=726, width=835)

        fm1 = Frame(fm, bg="light pink", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm1.place(x=5, y=5, height=400, width=450)

        Label(fm1, text='Admission no :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,
                                                                                                                 y=40)
        Ad_no_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        Ad_no_entry.place(x=150, y=44)

        Label(fm1, text='Name :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=70)
        name_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        name_entry.place(x=150, y=74)

        Label(fm1, text='Class :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=100)
        class_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        class_entry.place(x=150, y=104)

        Label(fm1, text='English :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=130)
        eng_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eng_entry.place(x=150, y=134)

        Label(fm1, text='Physics :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=160)
        physics_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        physics_entry.place(x=150, y=164)

        Label(fm1, text='Chemistry :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,
                                                                                                              y=190)
        chemistry_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        chemistry_entry.place(x=150, y=194)

        Label(fm1, text='Biology :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=220)
        bio_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        bio_entry.place(x=150, y=224)

        Label(fm1, text='Optional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=250)
        opt_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        opt_entry.place(x=150, y=254)

        Label(fm1, text='Additional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,
                                                                                                               y=280)
        add_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        add_entry.place(x=150, y=284)

        Label(fm1, text='GS :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=310)
        gs_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        gs_entry.place(x=150, y=314)

        Button(fm1, text='Add Record', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa", command= add).place(x=310, y=70, width=125, height=40)
        Button(fm1, text='Modify Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= modify).place(x=310, y=130,width=125, height=40)
        Button(fm1, text='Delete Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= delete).place(x=310, y=190,width=125, height=40)
        Button(fm1, text='Clear Field', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command= clear).place(x=310, y=250, width=125,height=40)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)

        fm3 = Frame(fm, bg='yellow', highlightthickness=4, highlightbackground='black')
        fm3.place(x=5, y=410, height=310, width=823)

        columns = ['Admission number', 'Name', 'Class', 'English', 'Physics', 'Chemistry', 'Bio', 'Opt', 'Add', 'GS']
        tree = ttk.Treeview(fm3, columns=columns, height=100, selectmode=BROWSE)
        xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
        yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        tree.heading('Admission number', text='AD_NO', anchor=CENTER)
        tree.heading('Name', text='NAME', anchor=CENTER)
        tree.heading('Class', text='CLASS', anchor=CENTER)
        tree.heading('English', text='ENGLISH', anchor=CENTER)
        tree.heading('Physics', text='PHYSICS', anchor=CENTER)
        tree.heading('Chemistry', text='CHEMISTRY', anchor=CENTER)
        tree.heading('Bio', text='BIOLOGY', anchor=CENTER)
        tree.heading('Opt', text='OPTIONAL', anchor=CENTER)
        tree.heading('Add', text='ADDITIONAL', anchor=CENTER)
        tree.heading('GS', text='GS', anchor=CENTER)

        tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

        tree.column('#0', width=0, stretch=NO, anchor=CENTER)
        tree.column('#1', width=60,minwidth=60, stretch=NO, anchor=CENTER)
        tree.column('#2', width=160,minwidth= 160, stretch=NO, anchor=CENTER)
        tree.column('#3', width=80,minwidth=80, stretch=NO, anchor=CENTER)
        tree.column('#4', width=100,minwidth= 100, stretch=NO, anchor=CENTER)
        tree.column('#5', width=100,minwidth= 100, stretch=NO, anchor=CENTER)
        tree.column('#6', width=100,minwidth= 100, stretch=NO, anchor=CENTER)
        tree.column('#7', width=100,minwidth= 100, stretch=NO, anchor=CENTER)
        tree.column('#8', width=100,minwidth= 100, stretch=NO, anchor=CENTER)
        tree.column('#9', width=100,minwidth= 100, stretch=NO, anchor=CENTER)
        tree.column('#10', width=100,minwidth= 100, stretch=NO, anchor=CENTER)


        query = 'select s.admission_no,s.sname, s.sclass, b.english, b.physics, b.chemistry, b.biology,b.optional, b.additional, b.gs from studdetails s, biology b  where s.admission_no= b.admission_no;'
        mycursor.execute(query)
        all = mycursor.fetchall()
        for val in all:
            tree.insert(parent='', index='end', values=val)

        tree.bind("<<TreeviewSelect>>", display)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)






    def commerce():
        def add():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not accountancy_entry.get()  or not gs_entry.get() or not business_stu_entry.get() or not eco_entry.get() or not opt_entry.get() or not add_entry.get() :
                mb.showerror('Error', 'All Fields are required')

            else:
                a = []
                b = []
                sql = "Select * from studdetails" \
                      " where admission_no= %s"
                aa = [Ad_no_entry.get()]
                mycursor.execute(sql, aa)
                all = mycursor.fetchone()
                a.append(all)

                if a[0] == None:
                    mb.showerror("Error", f"No Record Found of {Ad_no_entry.get()}")

                elif int(class_entry.get()) > 12 or int(class_entry.get()) < 11:
                    mb.showerror('Error', 'Record of class greater than 12 and less than 11 is not inserted here')


                else:
                    for i in a[0]:
                        b.append(i)

                    if b[1] != name_entry.get():
                        mb.showerror("Error", "Invalid Name")

                    elif b[4] != class_entry.get():
                        mb.showerror("Error", "Class doesn't match")

                    elif b[12]!= 'Commerce':
                        mb.showerror('Error', 'Stream is not Commerce')

                    else:
                        a = []
                        sql = "Select * from commerce" \
                              " where admission_no= %s"
                        aa = [Ad_no_entry.get()]
                        mycursor.execute(sql, aa)
                        all = mycursor.fetchone()
                        a.append(all)

                        if a[0] == None:
                            a = (Ad_no_entry.get(), eng_entry.get(),accountancy_entry.get(),business_stu_entry.get(), eco_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get())
                            query = "insert into commerce values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            mycursor.execute(query, a)
                            main.commit()
                            tree.insert(parent='', index='end',
                                        values=(Ad_no_entry.get(),name_entry.get(),class_entry.get(), eng_entry.get(),accountancy_entry.get(),business_stu_entry.get(), eco_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get()))
                            mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                        else:
                            mb.showerror('Error', 'Record Already Present')



        def clear():
            for widget in fm1.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, 'end')




        def modify():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not accountancy_entry.get() or not gs_entry.get() or not business_stu_entry.get() or not eco_entry.get() or not opt_entry.get() or not add_entry.get():
                mb.showerror('Error', 'All Fields are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from commerce where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    a = [eng_entry.get(),accountancy_entry.get(),business_stu_entry.get(), eco_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get(),Ad_no_entry.get()]
                    query = "Update commerce set english=%s,accountancy= %s, business_studies= %s, economics= %s,optional= %s,additional= %s, gs= %s" \
                            "where ADMISSION_NO= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, c.english, c.accountancy, c.business_studies,c.economics,c.optional, c.additional, c.gs from studdetails s, commerce c  where s.admission_no= c.admission_no;'
                    mycursor.execute(query)
                    all_records = mycursor.fetchall()

                    for record in all_records:
                        tree.insert(parent='', index='end', values=record)

                    mb.showinfo('Modified', f'Record of {name_entry.get()} is modified')

                clear()

        def delete():
            if not Ad_no_entry.get() or not class_entry.get() or not name_entry.get():
                mb.showerror('Error', 'Admission no,Name and Class are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from commerce where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    lst = [Ad_no_entry.get()]
                    query = 'delete from commerce where admission_no= %s'
                    mycursor.execute(query, lst)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, c.english, c.accountancy, c.business_studies,c.economics,c.optional, c.additional, c.gs from studdetails s, commerce c  where s.admission_no= c.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)
                    mb.showinfo('Deleted', f'Record of {Ad_no_entry.get()} is Deleted')
                    clear()

        def display(a):
            clear()
            selecteditem= tree.selection()[0]
            Ad_no_entry.insert(0, tree.item(selecteditem)['values'][0])
            name_entry.insert(0, tree.item(selecteditem)['values'][1])
            class_entry.insert(0 , tree.item(selecteditem)['values'][2])
            eng_entry.insert(0, tree.item(selecteditem)['values'][3])
            accountancy_entry.insert(0, tree.item(selecteditem)['values'][4])
            business_stu_entry.insert(0, tree.item(selecteditem)['values'][5])
            eco_entry.insert(0, tree.item(selecteditem)['values'][6])
            opt_entry.insert(0, tree.item(selecteditem)['values'][7])
            add_entry.insert(0, tree.item(selecteditem)['values'][8])
            gs_entry.insert(0, tree.item(selecteditem)['values'][9])


            fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
            fm2.place(x=460, y=5, height=400, width=370)

            Label(fm2, text="Admission No :", font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=30)
            Label(fm2, text= tree.item(selecteditem)['values'][0], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=150, y=30)

            Label(fm2, text= 'Name            :', font= ('Arial', 15,'bold'), bg="#E6E6FA").place(x= 2, y= 60)
            Label(fm2, text=tree.item(selecteditem)['values'][1], bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=60)

            Label(fm2, text='Class            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=90)
            Label(fm2, text=tree.item(selecteditem)['values'][2], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=90)

            Label(fm2, text='English         :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=120)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][3]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=120)

            Label(fm2, text='Accountancy            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=150)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][4]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=150)
            #
            Label(fm2, text='Business :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=180)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][5]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=180)
            #
            Label(fm2, text='Economics           :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=210)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][6]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=210)
            #
            Label(fm2, text='Optional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=240)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][7]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=240)

            Label(fm2, text='Additional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=270)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][8]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=270)

            Label(fm2, text='GS     :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=300)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][9]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=300)


            Frame(fm2, bg= 'black').place(x= 210, y= 80, width= 4, height= 400)

            a= tree.item(selecteditem)['values'][3]+tree.item(selecteditem)['values'][4]+tree.item(selecteditem)['values'][5]+tree.item(selecteditem)['values'][6]+tree.item(selecteditem)['values'][7]+tree.item(selecteditem)['values'][8]+tree.item(selecteditem)['values'][9]
            Label(fm2, text= 'Total Marks :', font=('Arial', 15, 'bold'), bg="#E6E6FA" ).place(x= 215, y= 180)
            Label(fm2, text= f"{a}/700",  font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x=230,y=210)

            b= (a/700)*100
            b= str(b)

            Label(fm2,text= 'Percentage :', font=('Arial', 15, 'bold'), bg="#E6E6FA"  ).place(x= 215, y= 250)
            Label(fm2, text= f"{b[0:5]} %", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg= 'blue').place(x= 230, y= 280)
            b= float(b)
            Label(fm2, text='Grade :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x= 215, y= 320)
            if b>=95:
                Label(fm2, text= 'A+', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=350)

            elif b<= 95 and b>= 90:
                Label(fm2, text='A1', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<=90 and b>= 80:
                Label(fm2, text='A2', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 80 and b>= 70:
                Label(fm2, text='B', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 70 and b>= 60:
                Label(fm2, text='C', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 60 and b>= 50:
                Label(fm2, text='D', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b<= 50 and b>= 40:
                Label(fm2, text='E', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            else:
                Label(fm2, text='FAIL', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)


        fm = Frame(m, bg="#4EEE94")
        fm.place(x=510, y=10, height=726, width=835)

        fm1 = Frame(fm, bg="light pink", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm1.place(x=5, y=5, height=400, width=450)

        Label(fm1, text='Admission no :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,
                                                                                                                 y=40)
        Ad_no_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        Ad_no_entry.place(x=150, y=44)

        Label(fm1, text='Name :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=70)
        name_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        name_entry.place(x=150, y=74)

        Label(fm1, text='Class :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=100)
        class_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        class_entry.place(x=150, y=104)

        Label(fm1, text='English :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=130)
        eng_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eng_entry.place(x=150, y=134)

        Label(fm1, text='Accountancy :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=160)
        accountancy_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        accountancy_entry.place(x=150, y=164)

        Label(fm1, text='Business Studies:', fg='black', bg='light pink', font=('Comic Sans MS', 13, 'bold')).place(x=8,y=190)
        business_stu_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        business_stu_entry.place(x=150, y=194)

        Label(fm1, text='Economics :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=220)
        eco_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eco_entry.place(x=150, y=224)

        Label(fm1, text='Optional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=250)
        opt_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        opt_entry.place(x=150, y=254)

        Label(fm1, text='Additional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,y=280)
        add_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        add_entry.place(x=150, y=284)

        Label(fm1, text='GS :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=310)
        gs_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        gs_entry.place(x=150, y=314)

        Button(fm1, text='Add Record', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command= add).place(x=310, y=70, width=125,height=40)
        Button(fm1, text='Modify Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= modify).place(x=310, y=130,width=125, height=40)
        Button(fm1, text='Delete Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= delete).place(x=310, y=190,width=125, height=40)
        Button(fm1, text='Clear Field', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command= clear).place(x=310, y=250, width=125,height=40)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)

        fm3 = Frame(fm, bg='yellow', highlightthickness=4, highlightbackground='black')
        fm3.place(x=5, y=410, height=310, width=823)

        columns = ['Admission number', 'Name', 'Class', 'English', 'Accountancy', 'Business_stu', 'Economics', 'Opt', 'Add', 'GS']
        tree = ttk.Treeview(fm3, columns=columns, height=100, selectmode=BROWSE)
        xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
        yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        tree.heading('Admission number', text='AD_NO', anchor= CENTER)
        tree.heading('Name', text='NAME', anchor= CENTER)
        tree.heading('Class', text='CLASS', anchor= CENTER)
        tree.heading('English', text='ENGLISH', anchor=CENTER)
        tree.heading('Accountancy', text='ACCOUNTANCY', anchor=CENTER)
        tree.heading('Business_stu', text='BUSINESS STUDIES', anchor=CENTER)
        tree.heading('Economics', text='ECONOMICS', anchor=CENTER)
        tree.heading('Opt', text='OPTIONAL', anchor=CENTER)
        tree.heading('Add', text='ADDITIONAL', anchor=CENTER)
        tree.heading('GS', text='GS', anchor=CENTER)

        tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

        tree.column('#0', width=0, stretch=NO, anchor=CENTER)
        tree.column('#1', width=60, stretch=NO, anchor=CENTER)
        tree.column('#2', width=160, stretch=NO, anchor=CENTER)
        tree.column('#3', width=80, stretch=NO, anchor=CENTER)
        tree.column('#4', width=100, stretch=NO, anchor=CENTER)
        tree.column('#5', width=100, stretch=NO, anchor=CENTER)
        tree.column('#6', width=150, stretch=NO, anchor=CENTER)
        tree.column('#7', width=180, stretch=NO, anchor=CENTER)
        tree.column('#8', width=100, stretch=NO, anchor=CENTER)
        tree.column('#9', width=100, stretch=NO, anchor=CENTER)
        tree.column('#10', width=100, stretch=NO, anchor=CENTER)

        query = 'select s.admission_no,s.sname, s.sclass, c.english, c.accountancy, c.business_studies,c.economics,c.optional, c.additional, c.gs from studdetails s, commerce c  where s.admission_no= c.admission_no;'
        mycursor.execute(query)
        all = mycursor.fetchall()
        for val in all:
            tree.insert(parent='', index='end', values=val)

        tree.bind("<<TreeviewSelect>>", display)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)



    def humanity():
        def add():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not poli_sci_entry.get()  or not gs_entry.get() or not history_entry.get() or not sociology_entry.get() or not opt_entry.get() or not add_entry.get() :
                mb.showerror('Error', 'All Fields are required')

            else:
                a = []
                b = []
                sql = "Select * from studdetails" \
                      " where admission_no= %s"
                aa = [Ad_no_entry.get()]
                mycursor.execute(sql, aa)
                all = mycursor.fetchone()
                a.append(all)

                if a[0] == None:
                    mb.showerror("Error", f"No Record Found of {Ad_no_entry.get()}")

                elif int(class_entry.get()) > 12 or int(class_entry.get()) < 11:
                    mb.showerror('Error', 'Record of class greater than 12 and less than 11 is not inserted here')


                else:
                    for i in a[0]:
                        b.append(i)

                    if b[1] != name_entry.get():
                        mb.showerror("Error", "Invalid Name")

                    elif b[4] != class_entry.get():
                        mb.showerror("Error", "Class doesn't match")

                    elif b[12]!= 'Humanity':
                        mb.showerror('Error', 'Stream is not Humanity')

                    else:
                        a = []
                        sql = "Select * from humanity" \
                              " where admission_no= %s"
                        aa = [Ad_no_entry.get()]
                        mycursor.execute(sql, aa)
                        all = mycursor.fetchone()
                        a.append(all)

                        if a[0] == None:
                            a = (Ad_no_entry.get(), eng_entry.get(),poli_sci_entry.get(),history_entry.get(), sociology_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get())
                            query = "insert into humanity values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            mycursor.execute(query, a)
                            main.commit()
                            tree.insert(parent='', index='end',
                                        values=(Ad_no_entry.get(),name_entry.get(),class_entry.get(), eng_entry.get(),poli_sci_entry.get(),history_entry.get(), sociology_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get()))
                            mb.showinfo('Record Inserted', f'Record of {name_entry.get()} is inserted')

                        else:
                            mb.showerror('Error', 'Record Already Present')



        def clear():
            for widget in fm1.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, 'end')




        def modify():
            if not Ad_no_entry.get() or not name_entry.get() or not class_entry.get() or not eng_entry.get() or not poli_sci_entry.get() or not gs_entry.get() or not history_entry.get() or not sociology_entry.get() or not opt_entry.get() or not add_entry.get():
                mb.showerror('Error', 'All Fields are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from humanity where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    a = [eng_entry.get(),poli_sci_entry.get(),history_entry.get(), sociology_entry.get(),
                                 opt_entry.get(),add_entry.get(),gs_entry.get(),Ad_no_entry.get()]
                    query = "Update humanity set english=%s,political_science= %s, history= %s, sociology= %s,optional= %s,additional= %s, gs= %s" \
                            "where ADMISSION_NO= %s"
                    mycursor.execute(query, a)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, h.english, h.political_science, h.history, h.sociology,h.optional, h.additional, h.gs from studdetails s, humanity h  where s.admission_no= h.admission_no;'
                    mycursor.execute(query)
                    all_records = mycursor.fetchall()

                    for record in all_records:
                        tree.insert(parent='', index='end', values=record)

                    mb.showinfo('Modified', f'Record of {name_entry.get()} is modified')

                clear()

        def delete():
            if not Ad_no_entry.get() or not class_entry.get() or not name_entry.get():
                mb.showerror('Error', 'Admission no,Name and Class are required')

            else:
                aa = []
                b = [Ad_no_entry.get()]
                query = "select * from humanity where admission_no= %s"
                mycursor.execute(query, b)
                all = mycursor.fetchone()
                aa.append(all)

                if aa[0] == None:
                    mb.showerror("Error", f"No Record of id {Ad_no_entry.get()}")

                else:
                    lst = [Ad_no_entry.get()]
                    query = 'delete from humanity where admission_no= %s'
                    mycursor.execute(query, lst)
                    main.commit()
                    for item in tree.get_children():
                        tree.delete(item)

                    query = 'select s.admission_no,s.sname, s.sclass, h.english, h.political_science, h.history, h.sociology,h.optional, h.additional, h.gs from studdetails s, humanity h  where s.admission_no= h.admission_no;'
                    mycursor.execute(query)
                    all = mycursor.fetchall()
                    for val in all:
                        tree.insert(parent='', index='end', values=val)
                    mb.showinfo('Deleted', f'Record of {Ad_no_entry.get()} is Deleted')
                    clear()

        def display(a):
            clear()
            selecteditem= tree.selection()[0]
            Ad_no_entry.insert(0, tree.item(selecteditem)['values'][0])
            name_entry.insert(0, tree.item(selecteditem)['values'][1])
            class_entry.insert(0 , tree.item(selecteditem)['values'][2])
            eng_entry.insert(0, tree.item(selecteditem)['values'][3])
            poli_sci_entry.insert(0, tree.item(selecteditem)['values'][4])
            history_entry.insert(0, tree.item(selecteditem)['values'][5])
            sociology_entry.insert(0, tree.item(selecteditem)['values'][6])
            opt_entry.insert(0, tree.item(selecteditem)['values'][7])
            add_entry.insert(0, tree.item(selecteditem)['values'][8])
            gs_entry.insert(0, tree.item(selecteditem)['values'][9])


            fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
            fm2.place(x=460, y=5, height=400, width=370)

            Label(fm2, text="Admission No :", font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=30)
            Label(fm2, text= tree.item(selecteditem)['values'][0], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=150, y=30)

            Label(fm2, text= 'Name            :', font= ('Arial', 15,'bold'), bg="#E6E6FA").place(x= 2, y= 60)
            Label(fm2, text=tree.item(selecteditem)['values'][1], bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=60)

            Label(fm2, text='Class            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=90)
            Label(fm2, text=tree.item(selecteditem)['values'][2], bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=90)

            Label(fm2, text='English         :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=120)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][3]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg= 'red').place(x=140, y=120)

            Label(fm2, text='Political Sci            :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=150)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][4]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=150)
            #
            Label(fm2, text='History :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=180)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][5]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=180)
            #
            Label(fm2, text='Sociology           :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=210)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][6]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg='red').place(x=140, y=210)
            #
            Label(fm2, text='Optional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=240)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][7]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=240)

            Label(fm2, text='Additional        :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=270)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][8]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'),fg='red').place(x=140, y=270)

            Label(fm2, text='GS     :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=2, y=300)
            Label(fm2, text=f"{tree.item(selecteditem)['values'][9]}/100", bg="#E6E6FA", font=('Arial', 15, 'bold'), fg= 'red').place(x=140, y=300)

            Frame(fm2, bg='black').place(x=210, y=80, width=4, height=400)

            a = tree.item(selecteditem)['values'][3] + tree.item(selecteditem)['values'][4] + \
                tree.item(selecteditem)['values'][5] + tree.item(selecteditem)['values'][6] + \
                tree.item(selecteditem)['values'][7] + tree.item(selecteditem)['values'][8] + \
                tree.item(selecteditem)['values'][9]
            Label(fm2, text='Total Marks :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=215, y=180)
            Label(fm2, text=f"{a}/700", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=210)

            b = (a / 700) * 100
            b= str(b)
            Label(fm2, text='Percentage :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=215, y=250)
            Label(fm2, text=f"{b[0:5]} %", font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=280)
            b= float(b)
            Label(fm2, text='Grade :', font=('Arial', 15, 'bold'), bg="#E6E6FA").place(x=215, y=320)
            if b >= 95:
                Label(fm2, text='A+', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=230, y=350)

            elif b <= 95 and b >= 90:
                Label(fm2, text='A1', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b <= 90 and b >= 80:
                Label(fm2, text='A2', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b <= 80 and b >= 70:
                Label(fm2, text='B', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b <= 70 and b >= 60:
                Label(fm2, text='C', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b <= 60 and b >= 50:
                Label(fm2, text='D', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            elif b <= 50 and b >= 40:
                Label(fm2, text='E', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)

            else:
                Label(fm2, text='FAIL', font=('Arial', 15, 'bold'), bg="#E6E6FA", fg='blue').place(x=240, y=350)





        fm = Frame(m, bg="#4EEE94")
        fm.place(x=510, y=10, height=726, width=835)

        fm1 = Frame(fm, bg="light pink", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm1.place(x=5, y=5, height=400, width=450)

        Label(fm1, text='Admission no :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,y=40)
        Ad_no_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        Ad_no_entry.place(x=150, y=44)

        Label(fm1, text='Name :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=70)
        name_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        name_entry.place(x=150, y=74)

        Label(fm1, text='Class :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=100)
        class_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        class_entry.place(x=150, y=104)

        Label(fm1, text='English :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=130)
        eng_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        eng_entry.place(x=150, y=134)

        Label(fm1, text='Political Science:', fg='black', bg='light pink', font=('Comic Sans MS', 13, 'bold')).place(x=8,y=160)
        poli_sci_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        poli_sci_entry.place(x=150, y=164)

        Label(fm1, text='History :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=190)
        history_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        history_entry.place(x=150, y=194)

        Label(fm1, text='Sociology :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,y=220)
        sociology_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        sociology_entry.place(x=150, y=224)

        Label(fm1, text='Optional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=250)
        opt_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        opt_entry.place(x=150, y=254)

        Label(fm1, text='Additional :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8,y=280)
        add_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        add_entry.place(x=150, y=284)

        Label(fm1, text='GS :', fg='black', bg='light pink', font=('Comic Sans MS', 14, 'bold')).place(x=8, y=310)
        gs_entry = Entry(fm1, fg='black', bd=1, font=('Comic Sans MS', 9))
        gs_entry.place(x=150, y=314)

        Button(fm1, text='Add Record', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command=add).place(x=310, y=70, width=125,height=40)
        Button(fm1, text='Modify Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= modify).place(x=310, y=130,width=125, height=40)
        Button(fm1, text='Delete Record', font=('Comic Sans MS', 13, 'bold'), bg="#f3e7fa",command= delete).place(x=310, y=190,width=125, height=40)
        Button(fm1, text='Clear Field', font=('Comic Sans MS', 15, 'bold'), bg="#f3e7fa",command= clear).place(x=310, y=250, width=125,height=40)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)

        fm3 = Frame(fm, bg='yellow', highlightthickness=4, highlightbackground='black')
        fm3.place(x=5, y=410, height=310, width=823)

        columns = ['Admission number', 'Name', 'Class', 'English', 'political science', 'history', 'sociology', 'Opt','Add', 'GS']
        tree = ttk.Treeview(fm3, columns=columns, height=100, selectmode=BROWSE)
        xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
        yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        tree.heading('Admission number', text='AD_NO', anchor=CENTER)
        tree.heading('Name', text='NAME', anchor=CENTER)
        tree.heading('Class', text='CLASS', anchor=CENTER)
        tree.heading('English', text='ENGLISH', anchor=CENTER)
        tree.heading('political science', text='POLITICAL SCIENCE', anchor=CENTER)
        tree.heading('history', text='HISTORY', anchor=CENTER)
        tree.heading('sociology', text='SOCIOLOGY', anchor=CENTER)
        tree.heading('Opt', text='OPTIONAL', anchor=CENTER)
        tree.heading('Add', text='ADDITIONAL', anchor=CENTER)
        tree.heading('GS', text='GS', anchor=CENTER)

        tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

        tree.column('#0', width=0, stretch=NO, anchor=CENTER)
        tree.column('#1', width=60, stretch=NO, anchor=CENTER)
        tree.column('#2', width=160, stretch=NO, anchor=CENTER)
        tree.column('#3', width=80, stretch=NO, anchor=CENTER)
        tree.column('#4', width=100, stretch=NO, anchor=CENTER)
        tree.column('#5', width=200, stretch=NO, anchor=CENTER)
        tree.column('#6', width=100, stretch=NO, anchor=CENTER)
        tree.column('#7', width=100, stretch=NO, anchor=CENTER)
        tree.column('#8', width=120, stretch=NO, anchor=CENTER)
        tree.column('#9', width=100, stretch=NO, anchor=CENTER)
        tree.column('#10', width=100, stretch=NO, anchor=CENTER)

        query = 'select s.admission_no,s.sname, s.sclass, h.english, h.political_science, h.history, h.sociology,h.optional, h.additional, h.gs from studdetails s, humanity h  where s.admission_no= h.admission_no;'
        mycursor.execute(query)
        all = mycursor.fetchall()
        for val in all:
            tree.insert(parent='', index='end', values=val)

        tree.bind("<<TreeviewSelect>>", display)

        fm2 = Frame(fm, bg="#E6E6FA", highlightthickness=4, highlightcolor='black', highlightbackground='black')
        fm2.place(x=460, y=5, height=400, width=370)


    opt= Frame(m, bg= "#A6D0EB")
    opt.place(x= 40, y= 450, height= 250, width= 260)

    Button(opt, text="X", bg="#A6D0EB", bd=0, font=('Arial', 18, 'bold'), command= exit).place(x=2, y=2)

    Button(opt, text= "-- Class 1-5", bg= "#A6D0EB", bd= 0, font= ('Arial',15 ,'bold'), command= junior).place(x= 30, y= 2)
    Button(opt, text="-- Class 6-8", bg= "#A6D0EB", bd= 0, font= ('Arial', 15,'bold'), command= middle).place(x=30, y=30)
    Button(opt, text="-- Class 9-10", bg= "#A6D0EB", bd= 0, font= ('Arial',15 ,'bold'), command= class9_10).place(x=30, y=60)
    Button(opt, text="-- Maths 11-12", bg= "#A6D0EB", bd= 0, font= ('Arial', 15,'bold'), command= maths).place(x=30, y=90)
    Button(opt, text="-- Biology 11-12", bg= "#A6D0EB", bd= 0, font= ('Arial',15 ,'bold'), command= bio).place(x=30, y=120)
    Button(opt, text="-- Commerce 11-12", bg= "#A6D0EB", bd= 0, font= ('Arial', 15,'bold'), command= commerce).place(x=30, y=150)
    Button(opt, text="-- Humanity 11-12", bg= "#A6D0EB", bd= 0, font= ('Arial',15 ,'bold'), command= humanity).place(x=30, y=180)




def vehicles():
    def display(A):
            clear()
            selecteditem = tree.selection()[0]
            vh_id.insert(0, tree.item(selecteditem)['values'][0])
            vh_no.insert(0, tree.item(selecteditem)['values'][1])
            vh_model.insert(0,tree.item(selecteditem)['values'][2])
            vh_capacity.insert(0, tree.item(selecteditem)['values'][3])
            vh_gpsid.insert(0, tree.item(selecteditem)['values'][4])
            vh_driver.insert(0, tree.item(selecteditem)['values'][5])
            dr_license.insert(0,tree.item(selecteditem)['values'][6])
            vh_conductor.insert(0, tree.item(selecteditem)['values'][7])
            cn_contact.insert(0, tree.item(selecteditem)['values'][8])
            mn_Date.insert(0, tree.item(selecteditem)['values'][9])

    def add():
        if not vh_id.get() or not vh_no.get() or not vh_model.get() or not vh_capacity.get() or not vh_gpsid.get() or not vh_driver.get() or not dr_license.get() or not vh_conductor.get() or not cn_contact.get() or not mn_Date.get():
            mb.showerror('Error', 'All Fields are required')

        elif len(cn_contact.get()) != 10:
            mb.showerror('Error', 'Invalid Contact number')

        elif len(dr_license.get()) != 16:
            mb.showerror('Error', 'Invalid License number')

        else:
            b = []
            aa = [vh_id.get()]
            query = 'select * from vehicle where vehicle_id= %s'
            mycursor.execute(query, aa)
            all = mycursor.fetchone()
            b.append(all)
            print(b)
            if b[0]== None:
                a = [vh_id.get(), vh_no.get(), vh_model.get(), vh_capacity.get(), vh_gpsid.get(), vh_driver.get(),
                     dr_license.get(), vh_conductor.get(), cn_contact.get(), mn_Date.get()]
                query = "insert into Vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query, [vh_id.get(), vh_no.get(), vh_model.get(), vh_capacity.get(), vh_gpsid.get(), vh_driver.get(),
                     dr_license.get(), vh_conductor.get(), cn_contact.get(), mn_Date.get()])
                main.commit()
                tree.insert(parent='', index='end', values=(
                vh_id.get(), vh_no.get(), vh_model.get(), vh_capacity.get(), vh_gpsid.get(), vh_driver.get(),
                dr_license.get(), vh_conductor.get(), cn_contact.get(), mn_Date.get()))
                mb.showinfo('Record Inserted', f'Record of {vh_id.get()} is inserted')
                clear()

            else:
                mb.showerror('Error', 'Record  is already present')


    def clear():
        for widget in fm1.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, 'end')

            if isinstance(widget, DateEntry):
                widget.delete(0, 'end')

    def delete():
        if not vh_id.get()  or not vh_no.get() or not vh_driver.get() or not dr_license.get():
            mb.showerror(title="Error", message='PLEASE ENTER ALL THE NECESSARY DETAILS')


        else:
            aa = []
            query = "select * from vehicle where vehicle_id= %s"
            mycursor.execute(query, [vh_id.get()])
            all = mycursor.fetchone()
            aa.append(all)

            if aa[0] == None:
                mb.showerror("Error", f"No Record of id {vh_id.get()}")

            else:
                sql = "delete from vehicle where vehicle_id= %s "
                mycursor.execute(sql, [vh_id.get()])
                main.commit()

                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from vehicle'
                mycursor.execute(query)
                all = mycursor.fetchall()
                for val in all:
                    tree.insert(parent='', index='end', values=val)

                mb.showinfo("Record Deleted", f" Record of {vh_id.get()} is Deleted")

    def modify():
        if not vh_id.get() or not vh_no.get() or not vh_model.get() or not vh_capacity.get() or not vh_gpsid.get() or not vh_driver.get() or not dr_license.get() or not vh_conductor.get() or not cn_contact.get() or not mn_Date.get():
            mb.showerror('Error', 'All Fields are required')

        else:
            aa = []
            b = [vh_id.get()]
            query = "select * from vehicle where vehicle_id= %s"
            mycursor.execute(query, b)
            all = mycursor.fetchone()
            aa.append(all)

            if aa[0] == None:
                mb.showerror("Error", f"No Record of id {vh_id.get()}")

            else:
                a = [ vh_no.get(), vh_model.get(), vh_capacity.get(), vh_gpsid.get(), vh_driver.get(),
                     dr_license.get(), vh_conductor.get(), cn_contact.get(), mn_Date.get(),vh_id.get()]
                query = "Update vehicle set vehicle_no= %s, vehicle_model= %s, vehicle_capacity=%s, vehicle_gps_id= %s, driver_name= %s, driver_license_no= %s, conductor_name= %s, conductor_contact= %s,vehicle_last_maintenance_date= %s" \
                        "where vehicle_id= %s"
                mycursor.execute(query, a)
                main.commit()
                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from vehicle'
                mycursor.execute(query)
                all = mycursor.fetchall()
                for val in all:
                    tree.insert(parent='', index='end', values=val)

                mb.showinfo('Updated', f'Record of {vh_id.get()} is modified')

            clear()

    def cancel():
        srch.delete(0, 'end')
        option.set('Select')
        for item in tree.get_children():
            tree.delete(item)
        query= 'select * from vehicle'
        mycursor.execute(query)
        all= mycursor.fetchall()
        for val in all:
            tree.insert(parent= '', index= 'end', values= val)

    def search():
        if option.get()== 'Select' :
            mb.showerror('Error', 'Please select valid search by')

        elif not srch.get():
            mb.showerror('Error', 'Please enter valid search')

        else:
            if option.get() == 'Vehicle ID':
                query = "select * from vehicle where vehicle_id like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Vehicle No':
                query = "select * from vehicle where vehicle_no like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Vehicle Model':
                query = "select * from vehicle where vehicle_model like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Vehicle Capacity':
                query = "select * from vehicle where vehicle_capacity like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'GPS Device ID':
                query = "select * from vehicle where vehicle_gps_id like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Driver Name':
                query = "select * from vehicle where driver_name like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Driver License No':
                query = "select * from vehicle where driver_license_no like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Conductor Name':
                query = "select * from vehicle where conductor_name like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Conductor Contact':
                query = "select * from vehicle where conductor_contact like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            elif option.get() == 'Last Maintenance Date':
                query = "select * from vehicle where vehicle_last_maintenance_date like '%" + srch.get() + "%'"
                mycursor.execute(query)
                all = mycursor.fetchall()
                for item in tree.get_children():
                    tree.delete(item)
                for val in all:
                    tree.insert(parent='', index='end', values=val)

            else:
                pass




    fm = Frame(m, bg="#BBFFFF")
    fm.place(x=510, y=10, height=726, width=835)

    img = PhotoImage(file="arr.png")
    lb = Button(fm, image=img, command= dash)
    lb.place(x=5, y=7, height=50, width=50)

    lb.image = img

    Frame(fm, bg='#FFDAB9', highlightthickness=5, highlightbackground='black').place(x=60, y=6, width=770, height=50)
    Label(fm, bg="#FFDAB9", text="Vehicles Details", font=('Arial', 20, 'underline', 'bold')).place(x=320, y=12)

    fm1= Frame(fm, bg= "#FFE1FF", highlightbackground='black', highlightthickness= 5)
    fm1.place(x= 5,y= 65, width= 820, height= 250)

    Label(fm1, text= 'Vehicle ID         : ',bg= "#FFE1FF", font= ('Comic Sans MS', 14, 'bold')).place(x= 5, y= 10) #Comic Sans MS
    vh_id= Entry(fm1, font= ('Comic Sans MS', 10, 'bold'))
    vh_id.place(x= 200, y= 15, width= 150)

    Label(fm1, text= 'Vehicle No       :', font= ('Comic Sans MS', 15, 'bold'),bg= "#FFE1FF").place(x= 5, y= 50)
    vh_no= Entry(fm1, font= ('Comic Sans MS', 10, 'bold'))
    vh_no.place(x= 200, y= 55, width= 150)

    Label(fm1, text='Vehicle Model     :', font=('Comic Sans MS', 14, 'bold'), bg="#FFE1FF").place(x=5, y=90)
    vh_model= Entry(fm1, font= ('Comic Sans MS',10,'bold'))
    vh_model.place(x= 200, y= 95, width= 150)

    Label(fm1, text='Vehicle Capacity  :', font=('Comic Sans MS', 14, 'bold'), bg="#FFE1FF").place(x=5, y=130)
    vh_capacity = Entry(fm1, font=('Comic Sans MS', 10, 'bold'))
    vh_capacity.place(x=200, y=135, width= 150)

    Label(fm1, text='GPS Device ID    :', font=('Comic Sans MS', 14, 'bold'), bg="#FFE1FF").place(x=5, y=170)
    vh_gpsid = Entry(fm1, font=('Comic Sans MS', 10, 'bold'))
    vh_gpsid.place(x=200, y=175, width= 150)

    Label(fm1, text= 'Driver Name           :', font= ('Comic Sans MS', 15, 'bold'), bg="#FFE1FF").place(x= 355, y= 10)
    vh_driver= Entry(fm1, font=('Comic Sans MS', 10, 'bold'))
    vh_driver.place(x=610, y=15)

    Label(fm1, text='Driver License No     :', font=('Comic Sans MS', 15, 'bold'), bg="#FFE1FF").place(x=355, y=50)
    dr_license = Entry(fm1, font=('Comic Sans MS', 10, 'bold'))
    dr_license.place(x=610, y=55)

    Label(fm1, text='Conductor Name         :', font=('Comic Sans MS', 14, 'bold'), bg="#FFE1FF").place(x=355, y=90)
    vh_conductor = Entry(fm1, font=('Comic Sans MS', 10, 'bold'))
    vh_conductor.place(x=610, y=95)

    Label(fm1, text='Conductor Contact     :', font=('Comic Sans MS', 15, 'bold'), bg="#FFE1FF").place(x=355, y=130)
    cn_contact= Entry(fm1, font=('Comic Sans MS', 10, 'bold'))
    cn_contact.place(x=610, y=135)

    Label(fm1, text='Last Maintenance Date :', font=('Comic Sans MS', 14, 'bold'), bg="#FFE1FF").place(x=355, y=170)
    mn_Date = DateEntry(fm1, font=('Comic Sans MS', 10, 'bold'),date_pattern='dd/mm/yyyy',)
    mn_Date.place(x=610, y=175, width= 150)


    fm2 = Frame(fm, bg="#F5F5F5", highlightbackground='black', highlightthickness=5)
    fm2.place(x=5, y=320, width=820, height=60)

    Button(fm2, text= 'Add Record',command=add, font= ('Comic Sans MS', 12, 'bold'), width= 14, bd= 3, bg= "#BFEFFF").place(x= 45, y= 5)
    Button(fm2, text= 'Modify Record',command= modify, font= ('Comic Sans MS', 12, 'bold'), width= 14, bd= 3, bg= "#BFEFFF").place(x= 250, y= 5)
    Button(fm2, text= 'Delete Record',command= delete, font= ('Comic Sans MS', 12, 'bold'), width= 14, bd= 3, bg= "#BFEFFF").place(x= 450, y= 5)
    Button(fm2, text= 'Clear Field',command= clear, font= ('Comic Sans MS', 12, 'bold'), width= 14, bd= 3, bg= "#BFEFFF").place(x= 650, y= 5)

    fm3 = Frame(fm, bg="#F5F5F5", highlightbackground='black', highlightthickness=5)
    fm3.place(x=5, y=385, width=820, height=330)

    fm4= Frame(fm3, bg= 'yellow', highlightbackground='black', highlightthickness=2)
    fm4.place(x= -2, y= -2, width= 813, height= 50)

    Label(fm4, text= 'Search By:', bg= 'yellow', font= ('Comic Sans MS', 14, 'bold')).place(x= 3, y= 3)

    val= ['Vehicle ID', 'Vehicle No', 'Vehicle Model', 'Vehicle Capacity', 'GPS Device ID', 'Driver Name', 'Driver License No', 'Conductor Name','Conductor Contact', 'Last Maintenance Date']
    option= ttk.Combobox(fm4, font = ('Comic Sans MS', 10, 'bold'), width = 14, state = 'readonly', values= val )
    option.place(x= 120, y= 10, width= 170)
    option.set('Select')

    Label(fm4, text= 'Search :', bg= 'yellow', font= ('Comic Sans MS', 14, 'bold')).place(x= 300, y= 3)
    srch= Entry(fm4, font= ('Comic Sans MS', 10, 'bold'))
    srch.place(x= 385, y= 10)

    Button(fm4, text= 'Search',command= search, font=('Comic Sans MS', 10, 'bold'), bg="#FFE1FF").place(x= 560, y= 7, width= 100)
    Button(fm4, text='Cancel',command= cancel, font=('Comic Sans MS', 10, 'bold'), bg="#FFE1FF").place(x=680, y=7, width=100)

    fm5= Frame(fm3, highlightthickness=2, highlightbackground= 'black')
    fm5.place(x= -2, y= 48, width= 813, height= 275)

    col= ['Vehicle ID', 'Vehicle No', 'Vehicle Model', 'Vehicle Capacity', 'GPS Device ID', 'Driver Name', 'Driver License No', 'Conductor Name','Conductor Contact', 'Last Maintenance Date']
    tree = ttk.Treeview(fm5, columns=col, height=100, selectmode=BROWSE)
    xscroll = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    yscroll = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

    tree.heading('Vehicle ID', text='Vehicle ID', anchor=CENTER)
    tree.heading('Vehicle No', text='Vehicle No', anchor=CENTER)
    tree.heading('Vehicle Model', text='Vehicle Model', anchor=CENTER)
    tree.heading('Vehicle Capacity', text='Vehicle Capacity', anchor=CENTER)
    tree.heading('GPS Device ID', text='GPS Device ID', anchor=CENTER)
    tree.heading('Driver Name', text='Driver Name', anchor=CENTER)
    tree.heading('Driver License No', text='Driver License No', anchor=CENTER)
    tree.heading('Conductor Name', text='Conductor Name', anchor=CENTER)
    tree.heading('Conductor Contact', text='Conductor Contact', anchor=CENTER)
    tree.heading('Last Maintenance Date', text='Last Maintenance Date', anchor=CENTER)

    tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

    tree.column('#0', width=0, stretch=NO, anchor=CENTER)
    tree.column('#1', width=80, stretch=NO, anchor=CENTER)
    tree.column('#2', width=140, stretch=NO, anchor=CENTER)
    tree.column('#3', width=120, stretch=NO, anchor=CENTER)
    tree.column('#4', width=160, stretch=NO, anchor=CENTER)
    tree.column('#5', width=100, stretch=NO, anchor=CENTER)
    tree.column('#6', width=140, stretch=NO, anchor=CENTER)
    tree.column('#7', width=180, stretch=NO, anchor=CENTER)
    tree.column('#8', width=160, stretch=NO, anchor=CENTER)
    tree.column('#9', width=170, stretch=NO, anchor=CENTER)
    tree.column('#10', width=180, stretch=NO, anchor=CENTER)

    query = 'select * from Vehicle'
    mycursor.execute(query)
    all = mycursor.fetchall()
    for val in all:
        tree.insert(parent='', index='end', values=val)

    tree.bind("<<TreeviewSelect>>", display)


def logout():

    ans = mb.askyesno('Exit', 'Do you want to Log Out?')
    if ans == True:
        m.destroy()
        import login

    else:
        pass



   
zzz= PhotoImage(file= 'abcd.png')
lb= Label(m, image=zzz)
lb.place(x= 0, y=0, relheight= 1, relwidth=1)
bt = Button(text= "Total Students", bg= "#FFDA00", bd= 0, font= ("Arial", 18,"bold" ), activebackground= "#FFDA00", command= btn1_click)
bt.place(x= 680, y= 280)
btn2= Button(text= "Total Teachers", bg= "#FFDA00", bd= 0, font= ("Arial", 18, "bold"), activebackground= "#FFDA00", command= btn2_click)
btn2.place(x= 1015,y= 280)
btn3= Button(text= "Total Staffs", bg= "#FFDA00", bd= 0, font= ("Arial", 18, "bold"), activebackground= "#FFDA00", command= btn3_click)
btn3.place(x= 690, y= 570)
btn4= Button(text= "Total Vehicles", bg= "#FFDA00", bd= 0, font= ("Arial", 18, "bold"), activebackground= "#FFDA00", command=btn4_click)
btn4.place(x= 1020,y= 570)



Button(m, text= "> Dashboard", bg= "#A6D0EB", font= ("Arial", 24, "bold"),bd= 0, activebackground= "#A6D0EB", command= dash).place(x= 30, y= 200)
Button(m, text= "> Students", bg= "#A6D0EB", font= ("Arial", 24, "bold"),bd= 0, activebackground= "#A6D0EB", command= stud).place(x= 30, y= 250)
Button(m, text= "> Teachers", bg= "#A6D0EB", font= ("Arial", 24, "bold"),bd= 0, activebackground= "#A6D0EB", command= teacher).place(x= 30, y= 300)
Button(m, text= "> Staffs", bg= "#A6D0EB", font= ("Arial", 24, "bold"),bd= 0, activebackground= "#A6D0EB", command= staff).place(x= 30, y= 350)
Button(m, text= "> Academics", bg= "#A6D0EB", font= ("Arial", 24, "bold"),bd= 0, activebackground= "#A6D0EB",command= academics).place(x= 30, y= 400)
Button(m, text= "> Vehicle Details", bg= "#A6D0EB", font= ("Arial", 24, "bold"),bd= 0, activebackground= "#A6D0EB", command= vehicles).place(x= 30, y= 450)
Button(m, text= "> Log Out", bg= "#A6D0EB", font= ("Arial", 24, "bold"),bd= 0, activebackground= "#A6D0EB", command=logout).place(x= 30, y= 500)


m.mainloop()



