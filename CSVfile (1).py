import tkinter as Tk
from tkinter import*
import csv
from datetime import time
from datetime import*
import datetime
import uuid
g=[]
def insert():
    a=Name_field.get()
    a=a.split(",")
    b=MobileNumber_field.get()
    b=b.split(",")
    c=Email_field.get()
    c=c.split(",")
    d=Institution_field.get()
    d=d.split(",")
    
    
    ts=datetime.datetime.now()
    
    u=uuid.uuid1()
    e=[*a,*b,*c,*d,ts,u]
    g.append(e)
    with open("poorna.csv", 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(e)
def search():
    s=search_field.get()
    print(s)
    for i in  range (len(g)):
        if g[i][0]==s:
            print(g[i])
        Name1=Label(root,text="Name")
        Name1.grid(row=7,column=0)
        Name_field1=Label(root,text=g[i][0])
        Name_field1.grid(row=7, column=1)
        MobileNumber1=Label(root,text="MobileNumber")
        Email1=Label(root,text="Email")
        Institution1=Label(root,text="Institution")


        MobileNumber1.grid(row=8,column=0)
        Email1.grid(row=9,column=0)
        Institution1.grid(row=10,column=0)


        MobileNumber_field1=Label(root,text=g[i][1])
        Email_field1=Label(root,text=g[i][2])
        Institution_field1=Label(root,text=g[i][3])
        MobileNumber_field1.grid(row=8, column=1)
        Email_field1.grid(row=9, column=1)
        Institution_field1.grid(row=10,column=1)
    
    
j=open("poorna.csv", "w")
if __name__=="__main__":
    root=tkinter.Tk()
       
    root.title("Registration Form")
   
    root.geometry("500x500")
   
    Name=Label(root,text="Name")
    Name.grid(row=0,column=0)
    Name_field=Entry(root)
    Name_field.grid(row=0, column=1)
    MobileNumber=Label(root,text="MobileNumber")
    Email=Label(root,text="Email")
    Institution=Label(root,text="Institution")
   
    
    MobileNumber.grid(row=1,column=0)
    Email.grid(row=2,column=0)
    Institution.grid(row=3,column=0)
   
   
    MobileNumber_field=Entry(root)
    Email_field=Entry(root)
    Institution_field=Entry(root)
    f= ['Name','Mobile number','Email','Institution','Time','UUID']
    with open("poorna.csv", 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(f)
    search1=Label(root,text="search")
    search1.grid(row=5,column=0)
    search=Button(root,text="search",command=search)
    search.grid(row=6,column=1)
    search_field=Entry(root)
    search_field.grid(row=5,column=1)
   
    
     
    MobileNumber_field.grid(row=1, column=1)
    Email_field.grid(row=2, column=1)
    Institution_field.grid(row=3,column=1)
    
   
   
    submit = Button(root, text="Submit", fg="Black", 
                           bg="Red", command=insert) 
    submit.grid(row=4, column=1) 
   
    root.mainloop()

