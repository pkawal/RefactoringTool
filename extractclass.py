from Tkinter import *
import Tkinter as tk
import tkMessageBox
import time
l=[]
cls=[]
mtd=[]
e1=0
root=0
def transfer(cls,mtd):
    print cls
    print mtd
    global root
    root=Tk()
    w=Label(root,text='SuperClass Name')
    w.pack()
    global e1
    e1=0
    e1=Entry(root)
    e1.pack()
    global l
    for x in range(0,len(mtd)):
        w=Label(root,text=mtd[x])
        w.pack()
        e=Entry(root)
        e.pack()
        l.append(e)
    B =Button(root, text ="Extract", command = lambda:hello(cls,mtd))
    B.pack()
    root.mainloop()
def hello(cls,mtd):
    global e1
    global l
    s='class '+e1.get()+'\n{\n'
    for x in range(0,len(l)):
        s=s+'returntype '+mtd[x]+'()\n{'+l[x].get()+'\n}\n'
    s=s+'}\n'
    print s
    f=open('variable.txt','r')
    str1=f.read()
    f.close()
    f=open('preet.txt','r')
    str2=f.read()
    f.close()
    for x in range(0,len(cls)):
        i=str2.find(cls[x])
        z=i+len(cls[x])
        a=str2[0:z]+' extends '+e1.get()+str2[z:]
        str2=a
        for z in range(i,len(str2)):
            if str2[z]=='c' and str2[z+1]=='l' and str2[z+2]=='a' and str2[z+3]=='s' and str2[z+4]=='s':
                break;
        i=i-6
        
        if(z<len(str2)-1):
            z=z+0
        else:
            z=z+1
        a=str2[i:z]
        z1=z
        ie=0
        ien=[]
        for z in range(0,len(mtd)):
            ie=a.index(mtd[z])-2
            if a[ie]=='t' and a[ie-1]=='n':
                ie=ie-2
            else:
                if a[ie]=='r':
                    ie=ie-3
                else:
                    if a[ie]=='e':
                        ie=ie-5
                    else:
                        if a[ie]=='t' and a[ie-1]=='a':
                            ie=ie-4
                        else:
                            if a[ie=='d']:
                                ie=ie-3
            z=ie
            while(a[z]!='{'):
                z=z+1
            z=z+2
            count=1
            while(count!=0):
                 if(a[z]=='}'):
                     count=count-1
                 if(a[z]=='{'):
                     count=count+1
                 z=z+1
            ss=a[0:ie]+a[z:]
            a=ss
        ss=str2[0:i]+a+str2[z1:]
        str2=ss
    print str2
    str2=s+str2
    f=open('preet.txt','w')
    f.write(str2)
    f.close()
    root.destroy()
