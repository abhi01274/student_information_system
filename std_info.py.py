from tkinter import *
import pymysql
import tkinter.messagebox
import re



def login():
        obk.destroy()
        def log():
            name = e1.get()
            passwd = e2.get()
            if len(name) == 0 or len(passwd) == 0:
                tkinter.messagebox.showerror(title="Error", message="Fields are empty")
            else:
                con = pymysql.connect("localhost", "root", "abhi", "test1")
                cur = con.cursor()
                q = "select * from login1 where username='" + name + "'and password='" + passwd + "' "
                try:
                    i = cur.execute(q)

                    if (i == 1):
                        ob1.destroy()
                        ob2 = Tk()
                        ob2.geometry("600x300")
                        ob2.config(bg="Beige")

                        def delete():
                            a = ex.get()

                            if len(a) == 0:
                                tkinter.messagebox.showerror("Error", "Fields are empty")
                            else:
                                try:
                                    q = "DELETE FROM login1 where name='" + a + "' or  email='" + a + "' or  mob='" + a + "'"
                                    i = cur.execute(q)
                                    con.commit()
                                    cur.close()
                                    con.close()
                                    tkinter.messagebox.showinfo(title="SUCCESS", message="Entry is deleted")
                                except Exception:
                                    tkinter.messagebox.showwarning("Wrong Input", "Input not found")
                        def search():
                            name = StringVar()
                            email = StringVar()
                            mob = StringVar()
                            username = StringVar()
                            fname = StringVar()
                            pincode = StringVar()

                            a = ex.get()

                            if len(a) == 0:
                                tkinter.messagebox.showerror("Error", "Fields are empty")
                            else:
                                q = "select * from login1 where name='" + a + "' or  email='" + a + "' or  mob='" + a + "'"
                                i = cur.execute(q)
                                o = cur.fetchall()
                                try:
                                    name.set(o[0][0])
                                    email.set(o[0][1])
                                    mob.set(o[0][2])
                                    username.set(o[0][3])
                                    fname.set(o[0][5])
                                    pincode.set(o[0][6])
                                except Exception:
                                    tkinter.messagebox.showwarning("wrong input", "input does not exist")

                                l2 = Label(text="your results are >>>>", font=('Times New Roman', '15'))
                                l2.place(x=80, y=160)

                                l2 = Label(text="Name", font=('Times New Roman', '15'))
                                l2.place(x=80, y=200)

                                e2 = Entry(width=20, textvariable=name)
                                e2.place(x=250, y=205)

                                l2 = Label(text="Email", font=('Times New Roman', '15'))
                                l2.place(x=80, y=230)

                                e3 = Entry(width=20, textvariable=email)
                                e3.place(x=250, y=230)

                                l2 = Label(text="mobile no", font=('Times New Roman', '15'))
                                l2.place(x=80, y=260)

                                e4 = Entry(width=20, textvariable=mob)
                                e4.place(x=250, y=260)

                                l2 = Label(text="username", font=('Times New Roman', '15'))
                                l2.place(x=80, y=290)

                                e5 = Entry(width=20, textvariable=username)
                                e5.place(x=250, y=290)

                                l2 = Label(text="father's name", font=('Times New Roman', '15'))
                                l2.place(x=80, y=320)

                                e6 = Entry(width=20, textvariable=fname)
                                e6.place(x=250, y=320)

                                l2 = Label(text="pin code", font=('Times New Roman', '15'))
                                l2.place(x=80, y=350)

                                e7 = Entry(width=20, textvariable=pincode)
                                e7.place(x=250, y=350)

                        l = Label(text="SEARCH ANY STUDENT \n (by name or by email or by mobile)",
                                  font=('Times New Roman', '19'))
                        l.place(x=80, y=20)

                        la = Label(text="Enter name or email or mobile no:::")
                        la.place(x=75, y=100)

                        ex = Entry(width=25)
                        ex.place(x=80, y=130)

                        b1 = Button(text="Search", width=16, height=1, command=search)
                        b1.place(x=250, y=130)

                        by=Button(text="Delete", width=16, height=1, command=delete)
                        by.place(x=400,y=130)

                        ob2.mainloop()


                    else:
                        tkinter.messagebox.showerror("Error", "data Not Matched!!")
                except pymysql.err.InternalError as e:
                    print(e)
                    cur.close()
                    con.close()


        def cancel():
            e1.delete(0, END)
            e2.delete(0, END)



        def fp():
            ob1.destroy()
            object = Tk()
            object.geometry("450x300")
            object.config(bg="beige")
            con = pymysql.connect("localhost", "root", "abhi", "test1")
            cur = con.cursor()

            def match():
                a = e1.get()
                b = e2.get()
                c = e3.get()
                d = e4.get()

                if len(a) == 0 or len(b) == 0 or len(c) == 0:
                    tkinter.messagebox.showerror(title="ERROR", message="Fields are empty")
                elif c != d:
                    tkinter.messagebox.showerror(title="error", message="new passwords did not matched")
                else:
                    q = "select * from login1 where username='" + a + "'and password='" + b + "'"
                    i = cur.execute(q)
                    if (i != 1):
                        tkinter.messagebox.showerror(title="ERROR", message="Username or password is wrong")
                    else:
                        q = "update login1 SET password ='" + c + "'where username= '" + a + "'"
                        j = cur.execute(q)
                        tkinter.messagebox.showinfo(title="SUCCESS", message="password is changed")
                        print(j)
                        con.commit()
                        cur.close()
                        con.close()

            def reset():
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)

            l1 = Label(text="Forgot password ?", font=('Times New Roman', 20, 'bold'))
            l1.place(x=120, y=5)
            l2 = Label(text="Enter username:")
            l2.place(x=100, y=50)
            l3 = Label(text="Enter old password:")
            l3.place(x=100, y=80)
            l4 = Label(text="Enter new password:")
            l4.place(x=100, y=110)
            l4 = Label(text="Confirm new password:")
            l4.place(x=100, y=140)

            e1 = Entry()
            e1.place(x=250, y=50)
            e2 = Entry()
            e2.place(x=250, y=80)
            e3 = Entry()
            e3.place(x=250, y=110)
            e4 = Entry()
            e4.place(x=250, y=140)

            b1 = Button(text="submit", width=16, command=match)
            b1.place(x=100, y=170)
            b1 = Button(text="Reset", width=16, command=reset)
            b1.place(x=250, y=170)
            object.mainloop()

        ob1 = Tk()
        ob1.geometry("550x400+100+100")
        ob1.config(bg="Beige")
        l=Label(text="LOGIN PAGE",width=38,height=2,font=('Times New Roman',10,'bold'))
        l.place(x=90,y=20)
        l1 = Label(ob1,text="ENTER USERNAME:")
        l1.place(x=90, y=60)
        e1 = Entry(ob1)
        e1.place(x=230, y=60)
        l2 = Label(ob1,text="ENTER PASSWORD:")
        l2.place(x=90, y=90)
        e2 = Entry(ob1)
        e2.place(x=230, y=90)
        b1 = Button(ob1, text="login", width=15, command=log)
        b1.place(x=90, y=130)
        b2 = Button(ob1,text="cancel", width=15, command=cancel)
        b2.place(x=230, y=130)
        b3=Button(ob1,width=35 ,text= "forgot password?",command=fp)
        b3.place(x=90, y=160)
        ob1.mainloop()


def register():
    obj = Tk()
    obj.geometry("450x400+370+50")
    obj.config(background="#CBCBCB")
    obk.destroy()
    con = pymysql.connect("localhost", "root", "abhi", "test1")
    cur = con.cursor()

    def reset():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)


    def Save():
        a = e1.get()
        b = e2.get()
        c = e3.get()
        d = e4.get()
        e = e5.get()
        f = e6.get()
        g = e8.get()
        h = e7.get()


        if len(a) == 0 or len(b) == 0 or len(c) == 0 or len(d) == 0 or len(e) == 0 or len(f) == 0 or len(g)==0 or len(h)==0:
            tkinter.messagebox.showwarning(title="empty fields", message="fields are empty")
            con.close()
            cur.close()
        else:
            if e != f:
                tkinter.messagebox.showerror(title="Error", message="passwords are not match")
            else:


                try:
                    if re.search("\w.{1,20}@\w{2,10}.[A-Za-z]{1,6}", b):
                        if re.search("[0-9]{10}", c):
                            if re.search("[0-9]{6}",h):
                                if re.search("[A-Za-z]{2,20}",a):
                                    if re.search("[A-Za-z]{2,20}",g):
                                        query = "insert into login1 values('%s','%s','%s','%s','%s','%s','%s')" % (a, b, c, d, e, g, h)

                                        i = cur.execute(query)
                                        print(i, "inserted")

                                        con.commit()
                                        con.close()
                                        cur.close()
                                        tkinter.messagebox.showinfo(title="success", message="registration successful")
                                        reset()
                                    else:
                                        tkinter.messagebox.showerror(title="ERROR", message="Father name format is wrong")
                                else:
                                    tkinter.messagebox.showerror(title="ERROR", message=" name format is wrong")

                            else:
                                tkinter.messagebox.showerror(title="ERROR", message="pincode format is wrong")

                        else:
                            tkinter.messagebox.showerror(title="ERROR", message="mobile no format is wrong")
                    else:
                        tkinter.messagebox.showerror(title="ERROR", message="email format is wrong")
                        con.commit()
                        con.close()
                        cur.close()
                except Exception as e:
                    print(e)

    # interface

    l1 = Label(obj,text="REGISTRATION FORM", font=('Times New Roman', '20'), background="#CBCBCB")
    l1.place(x=95, y=3)

    l2 = Label(obj,text="ENTER YOUR NAME", background="#CBCBCB")
    l2.place(x=100, y=50)
    l8 = Label(obj, text="ENTER FATHER'S NAME", background="#CBCBCB")
    l8.place(x=100, y=80)
    l3 = Label(obj,text="ENTER YOUR EMAIL", background="#CBCBCB")
    l3.place(x=100, y=111)
    l4 = Label(obj,text="ENTER MOBILE NO", background="#CBCBCB")
    l4.place(x=100, y=140)
    l5 = Label(obj,text="ENTER USERNAME", background="#CBCBCB")
    l5.place(x=100, y=170)
    l9 = Label(obj, text="ENTER PINCODE", background="#CBCBCB")
    l9.place(x=100, y=200)
    l6 = Label(obj,text="ENTER PASSWORD", background="#CBCBCB")
    l6.place(x=100, y=230)
    l7 = Label(obj,text="RETYPE PASSWORD", background="#CBCBCB")
    l7.place(x=100, y=260)

    e1 = Entry(obj)
    e1.place(x=250, y=50)

    e8 = Entry(obj)
    e8.place(x=250, y=80)

    e2 = Entry(obj)
    e2.place(x=250, y=110)

    e3 = Entry(obj)
    e3.place(x=250, y=140)

    e4 = Entry(obj)
    e4.place(x=250, y=170)

    e7 = Entry(obj)
    e7.place(x=250, y=200)

    e5 = Entry(obj)
    e5.place(x=250, y=230)

    e6 = Entry(obj)
    e6.place(x=250, y=260)



    b1 = Button(obj,text="SAVE", width=16, command=Save)
    b1.place(x=100, y=290)

    b2 = Button(obj,text="RESET", width=16, command=reset)
    b2.place(x=250, y=290)

    obj.mainloop()

obk= Tk()
obk.geometry("680x500+370+50")


con=pymysql.connect("localhost","root","abhi","test1")
cur=con.cursor()

lx=Label(text="WELCOME TO JECRC FOUNDATION PORTAL",font=('Times New Roman', '20'))
lx.place(x=70,y=50)

bx=Button(text="Login",width=37,command=login)
bx.place(x=70,y=420)

ba=Button(text="Register",width=37, command=register)
ba.place(x=340, y=420)

pic=PhotoImage(file='jecrc.png')
bb=Button(text="Save", image=pic, width= 500,height=300)
bb.place(x=80, y=90)

obk.mainloop()
