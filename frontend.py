from tkinter import *
from datetime import*
import backend

def get_selected_row(e):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[7])

def get_selected_row1(e):
    global selected_tuple
    index=list2.curselection()[0]
    selected_tuple=list2.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[7])

def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),isbn_text.get(),issue.get(),student_number.get(),issue_date.get(),due_date.get()):
        list1.insert(END,row)
def penalty_list():
    list2.delete(0,END)
    day=str(datetime.date(datetime.now())).split('-')
    print(day)
    for row in backend.view():
        penalty=row;
        penalty=penalty[7].split('-')
        if(penalty[0]!=''):
          for i in range(0,3):
            penalty[i]=int(penalty[i])
            day[i]=int(day[i])
          if((penalty[0]<day[2] and penalty[1]<=day[1] and penalty[2]<=day[0])or(penalty[1]<day[1] and penalty[2]<=day[0])or(penalty[2]<day[0])):
            list2.insert(END,row)
            print(day[0],day[1],day[2])

def add_command():
    if(title_text.get()==''):
       e1.insert(END,'--')
    if(author_text.get()==''):
       e2.insert(END,'--')
    if(isbn_text.get()==''):
       e3.insert(END,'--')
    if(issue.get()=='' or issue.get()=='no' or issue.get()=='NO'):
       e4.delete(0,END)
       e5.delete(0,END)
       e6.delete(0,END)
       e7.delete(0,END)
       e4.insert(END,'no')
       e5.insert(END,'--')
       e6.insert(END,'--')
       e7.insert(END,'--')
    if(issue.get()!='' and issue.get()!='no' and issue.get()!='NO' and issue.get()!='yes' and issue.get()!='YES'):
       override("Wrong input !!!")
    if(student_number.get()=='' or (student_number.get()=='--' and (issue.get()=='yes' or issue.get()=='YES'))):
       override("student number can't be Empty")
       return
    if(issue_date.get()=='' or (issue_date.get()=='--' and (issue.get()=='yes' or issue.get()=='YES'))):
       override("issue date can't be Empty")
       return
    if(due_date.get()=='' or (due_date.get()=='--' and (issue.get()=='yes' or issue.get()=='YES'))):
       override("due date can't be Empty")
       return
    backend.insert(title_text.get(),author_text.get(),isbn_text.get(),issue.get(),student_number.get(),issue_date.get(),due_date.get())
    view_command()
    penalty_list()
    l9.config(text=backend.count())

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    penalty_list()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    l9.config(text=backend.count())

def update_command():
    if(title_text.get()==''):
       e1.insert(END,'--')
    if(author_text.get()==''):
       e2.insert(END,'--')
    if(isbn_text.get()==''):
       e3.insert(END,'--')
    if(issue.get()=='' or issue.get()=='no' or issue.get()=='NO'):
       e4.delete(0,END)
       e5.delete(0,END)
       e6.delete(0,END)
       e7.delete(0,END)
       e4.insert(END,'no')
       e5.insert(END,'--')
       e6.insert(END,'--')
       e7.insert(END,'--')
    if(issue.get()!='' and issue.get()!='no' and issue.get()!='NO' and issue.get()!='yes' and issue.get()!='YES'):
       override("Wrong input !!!")
       return
    if(student_number.get()=='' or (student_number.get()=='--' and (issue.get()=='yes' or issue.get()=='YES'))):
       override("student number can't be Empty")
       return
    if(issue_date.get()=='' or (issue_date.get()=='--' and (issue.get()=='yes' or issue.get()=='YES'))):
       override("issue date can't be Empty")
       return
    if(due_date.get()=='' or (due_date.get()=='--' and (issue.get()=='yes' or issue.get()=='YES'))):
       override("due date can't be Empty")
       return
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),isbn_text.get(),issue.get(),student_number.get(),issue_date.get(),due_date.get())
    view_command()
    penalty_list()

def override(a):
    win=Tk()
    win.wm_title("Alert")
    positionRight = int(window.winfo_reqwidth()/2)
    positionDown = int(window.winfo_reqheight()/2)
    win.geometry("+{}+{}".format(positionRight, positionDown))
    l1=Label(win,text=a)
    l1.pack()
    b1=Button(win,text="OK", width=12,command=win.destroy)
    b1.pack()
    win.mainloop()

window=Tk()

window.wm_title("Library Management System")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="ISBN")
l3.grid(row=1,column=0)

l4=Label(window,text="Issued ?")
l4.grid(row=1,column=2)

l5=Label(window,text="Student Number")
l5.grid(row=2,column=0)

l6=Label(window,text="Date of issue")
l6.grid(row=2,column=2)

l7=Label(window,text="Due Date")
l7.grid(row=3,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

isbn_text=StringVar()
e3=Entry(window,textvariable=isbn_text)
e3.grid(row=1,column=1)

issue=StringVar()
e4=Entry(window,textvariable=issue)
e4.grid(row=1,column=3)

student_number=StringVar()
e5=Entry(window,textvariable=student_number)
e5.grid(row=2,column=1)

issue_date=StringVar()
e6=Entry(window,textvariable=issue_date)
e6.grid(row=2,column=3)

due_date=StringVar()
e7=Entry(window,textvariable=due_date)
e7.grid(row=3,column=1)

list1=Listbox(window, height=6,width=35)
list1.grid(row=4,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=4,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=4,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=5,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=6,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=7,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=8,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=9,column=3)

b7=Button(window,text="Clear all", width=12,command=clear_all)
b7.grid(row=10,column=3)

l9=Label(window,text="Books Available :",font='Helvetica 12 bold')
l9.grid(row=9,column=0)

l9=Label(window,text=backend.count(),font='Helvetica 12 bold')
l9.grid(row=9,column=1)

l8=Label(window,text="Penalty List Notification :",font='Helvetica 14 bold')
l8.grid(row=12,column=1,columnspan=2)

list2=Listbox(window, height=6,width=55)
list2.grid(row=14,column=0,rowspan=10,columnspan=10)
list2.bind('<<ListboxSelect>>',get_selected_row1)

view_command()

penalty_list()

window.mainloop()
