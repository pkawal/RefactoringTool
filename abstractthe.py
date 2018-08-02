import re
from Tkinter import *
import Tkinter as tk
import tkMessageBox
s="demo"
s2 ="extends "
s3=[]
s8="class "
e=0
root=0
def abstracttheclass(s3,arr):
    global root
    root=Tk()
    w=Label(root,text='SuperClass Name')
    w.pack()
    global e
    e=Entry(root)
    e.pack()
    B =Button(root, text ="Create", command = lambda:hello(s3,arr))
    B.pack()
    root.mainloop()
def hello(s3,arr):
    s=""
    for x in range(0,len(arr)):
        s='abstract returntype '+arr[x]+'();\n'+s 
    global e
    a=e.get()
    f=open('preet.txt',"r")
    s1=f.read()
    f.close()
    f=open('preet.txt',"w")
    f.write("")
    f.close()
    print (s3)
    e=[o.start()for o in re.finditer(s8,s1)]
    for t in range(0,len(s3)):
        d=[m.start()for m in re.finditer(s3[t],s1)]
        
        print d[0]
        d[0]=d[0]+len(s3[t])
        print d[0]
        y=s1[0:d[0]]
        s1=y+' extends '+a+' '+s1[d[0]:]
    
    f= open('preet.txt',"a")
    f.write(s1)
    f.close()
    f=open('preet.txt',"a")
    f.write('public abstract class '+a+'{ '+'\n'+s+'}')
    f.close()
    global root
    root.destroy()
