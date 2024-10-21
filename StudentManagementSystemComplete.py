def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        linkedin_id = linkedinval.get()
        github_id = githubval.get()
        skillset = skillsetval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'INSERT INTO studentdata1 (id, name, mobile, email, linkedin_id, github_id, skillset, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(strr, (id, name, mobile, email, linkedin_id, github_id,skillset, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', f'Id {id} Name {name} Added successfully.. Do you want to clear the form?', parent=addroot)
            if res:
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                linkedinval.set('')
                githubval.set('')
                skillsetval.set('')
        except Exception as e:
            messagebox.showerror('Notifications', f'Error: {str(e)}', parent=addroot)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False, False)

    # Labels
    idlabel = Label(addroot, text='Enter Id : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=14, anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    emaillabel.place(x=10,y=190)

    linkedinlabel = Label(addroot,text='Enter LinkedIn ID : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    linkedinlabel.place(x=10,y=250)

    githublabel = Label(addroot,text='Enter GitHub ID : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    githublabel.place(x=10,y=310)

    skillsetlabel = Label(addroot,text='Enter Skillset : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    skillsetlabel.place(x=10,y=370)

    # Entries
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    linkedinval = StringVar()
    githubval = StringVar()
    skillsetval = StringVar()

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    linkedinentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=linkedinval)
    linkedinentry.place(x=250,y=250)

    githubentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=githubval)
    githubentry.place(x=250,y=310)

    skillsetentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=skillsetval)
    skillsetentry.place(x=250,y=370)

    # Submit Button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,
                       activebackground='blue',activeforeground='white',
                       bg='white',command=submitadd)
    submitbtn.place(x=150,y=430)

    addroot.mainloop()

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        linkedin_id = linkedinval.get()
        github_id = githubval.get()
        skillset = skillsetval.get()
        if(skillset != ''):
            strr = 'select * from studentdata1 where skillset=%s'
            mycursor.execute(strr,(skillset,))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)
        elif(id != ''):
            strr = 'select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)
        elif(mobile != ''):
            strr = 'select *from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)
        elif(email != ''):
            strr = 'select *from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)
        elif(linkedin_id != ''):
            strr = 'select *from studentdata1 where linkedin_id=%s'
            mycursor.execute(strr,(linkedin_id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)
        elif(github_id != ''):
            strr = 'select *from studentdata1 where github_id=%s'
            mycursor.execute(strr,(github_id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                studenttable.insert('', END, values=vv)
        

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='firebrick1')
    searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False,False)
    
    idlabel = Label(searchroot,text='Enter Id : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    linkedinlabel = Label(searchroot,text='LinkedIn ID : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    linkedinlabel.place(x=10,y=250)

    githublabel = Label(searchroot,text='GitHub ID : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    githublabel.place(x=10,y=310)

    skillsetlabel = Label(searchroot,text='Enter skillset : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    skillsetlabel.place(x=10,y=370)

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    linkedinval = StringVar()
    githubval = StringVar()
    skillsetval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    linkedinentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=linkedinval)
    linkedinentry.place(x=250,y=250)

    githubentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=githubval)
    githubentry.place(x=250,y=310)

    skillsetentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=skillsetval)
    skillsetentry.place(x=250,y=370)


    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='white',command=search)
    submitbtn.place(x=150,y=430)

    searchroot.mainloop()

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
        studenttable.insert('', END, values=vv)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        linkedin_id = linkedinval.get()
        github_id = githubval.get()
        skillset = skillsetval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'UPDATE studentdata1 SET name=%s, mobile=%s, email=%s, linkedin_id=%s, github_id=%s, skillset=%s, date=%s, time=%s WHERE id=%s'
        mycursor.execute(strr, (name, mobile, email, linkedin_id, github_id, skillset, date, time, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='firebrick1')
    updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False,False)

    idlabel = Label(updateroot,text='Enter Id : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    linkedinlabel = Label(updateroot,text='LinkedIn ID : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    linkedinlabel.place(x=10,y=250)

    githublabel = Label(updateroot,text='GitHub ID : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    githublabel.place(x=10,y=310)

    skillsetlabel = Label(updateroot, text='Enter Skillset : ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    skillsetlabel.place(x=10, y=370)

    datelabel = Label(updateroot,text='Enter Date : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    linkedinval = StringVar()
    githubval = StringVar()
    skillsetval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    linkedinentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=linkedinval)
    linkedinentry.place(x=250,y=250)

    githubentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=githubval)
    githubentry.place(x=250,y=310)

    skillsetentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=skillsetval)
    skillsetentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)

    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='white',command=update)
    submitbtn.place(x=150,y=550)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        linkedinval.set(pp[4])
        githubval.set(pp[5])
        skillsetval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
def showstudent():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,linkedin_id,github_id,skillset,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),linkedin_id.append(pp[4]),github_id.append(pp[5]),
        skillset.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','LinkedIn ID','GitHub ID','Skillset','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,linkedin_id,github_id,skillset,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))


def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()


###################################################################################Connecttion of Database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),linkedin_id varchar(100),github_id varchar(50),skillset varchar(100),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected connected to the database ....',parent=dbroot)

        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('mana.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    #-------------------------------Connectdb Labels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #-------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #-------------------------------- Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='white',bd=5,width=20,activebackground='blue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
###########################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
import random
colors = ['white','green','blue','yellow','pink','red2','white']

##########################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='white')
root.geometry('1174x700+200+50')
root.iconbitmap('mana.ico')
root.resizable(False,False)
############################################################################################################  Frames
##---------------------------------------------------------------------------- dataentry frame

DataEntryFrame = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='OPERATIONS',width=30,font=('arial',22,'italic bold'),bg='white')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.  Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

##-----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='grey',foreground='white')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'LinkedIn ID', 'GitHub ID', 'Added Date', 'Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile No', text='Mobile No')
studenttable.heading('Email', text='Email')
studenttable.heading('LinkedIn ID', text='LinkedIn ID')
studenttable.heading('GitHub ID', text='GitHub ID')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id', width=100)
studenttable.column('Name', width=200)
studenttable.column('Mobile No', width=200)
studenttable.column('Email', width=300)
studenttable.column('LinkedIn ID', width=200)
studenttable.column('GitHub ID', width=200)
studenttable.column('Added Date', width=150)
studenttable.column('Added Time', width=150)
studenttable.pack(fill=BOTH,expand=1)

################################################################################################################  Slider
ss = 'BRIGHT BEATS'
count = 0
text = ''
##################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
############################################################################################################### clock
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()
################################################################################################################## ConnectDatabaseButton
connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',
                       activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()