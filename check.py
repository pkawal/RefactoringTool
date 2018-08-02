from Tkinter import *
import Tkinter as tk
import tkMessageBox
import re
arr=[]
checklist=[]



def check1():
    ind=[]
    indend=[]
    start=[]
    arr=[]
    ind1=[]
    str2=""
    indend1=[]
    aa=[]
    f=open('variable.txt','r')
    str1=f.read()
    f.close()
    ind=[]
    ind=[m.start()for m in re.finditer('class:',str1)]
    print "preet"
    print ind
    for x in range(0,len(ind)):
        ind[x]=ind[x]+6
    for x in range(0,len(ind)):
        y=ind[x]
        while(str1[y]!=':'):
            y=y+1
        indend.append(y)
    print indend
    global start
    for x in range(0,len(ind)):
        a=str1[ind[x]:indend[x]]
        start.append(a)
    print start
    
    top = Tk()
    global top
    var=0
    var1=[]
    global var
    global var1
    for machine in start:
        var=IntVar()

        l = Checkbutton(top, text=machine, variable=var)
        l.pack()
        var1.append(var)
    
    B1 =Button(top, text ="ExtractInto a Method", command = helloCallBack)
    B1.pack()
    B2 =Button(top, text ="Abstract Method", command = helloCall)
    B2.pack()
    top.mainloop()

def helloCallBack():
    #import commonmethod
    global var1
    global arr
    global start
    arr=[]
    for x in range(0,len(var1)):
        if(var1[x].get()==1):
            arr.append(start[x])
    print arr
    start1 = [[] for i in range(len(arr))]
    f=open('variable.txt','r')
    str1=f.read()
    f.close()
    ind=[]
    indend=[]
    indend1=[]
    ind1=[]
    str2=""
    for x in range(0,len(start1)):
        y=[]
        z=[]
        y=[m.start()for m in re.finditer(arr[x],str1)]
        #print 'yyyyyyyyyyyyyyyyyyyyy\n\n\n'+str1[y[0]:]
        
        for z in range(y[0],len(str1)):
            if str1[z]=='c' and str1[z+1]=='l' and str1[z+2]=='a' and str1[z+3]=='s' and str1[z+4]=='s' and str1[z+5]=='e':
                break;
        print z
        str2=str1[y[0]:z]
        print str2
        ind1=[m.start()for m in re.finditer('method:',str2)]
        for x1 in range(0,len(ind1)):
            ind1[x1]=ind1[x1]+7
        indend1=[]
        for x1 in range(0,len(ind1)):
            y1=ind1[x1]
            while(str2[y1]!=';'):
                y1=y1+1
            indend1.append(y1)
        aa=[]
        for x1 in range(0,len(ind1)):
            a=str2[ind1[x1]:indend1[x1]]
            aa.append(a)
            
        start1[x]=aa
    print start1
    arr1=[]
    fst=[]
    fst=start1[0]
    count=0
    for x in range(0,len(fst)):
        print 'xvalue'
        print x
        for x1 in range(1,len(start1)):
            sec=start1[x1]
            print sec
            for x2 in range(0,len(sec)):
            
        
                if(fst[x]==sec[x2]):
                    count=count+1
                   
        if(count==len(start1)-1):
            arr1.append(fst[x])
            
        count=0
    print arr1
    global top
    top.destroy()
    import extractclass
    extractclass.transfer(arr,arr1)
def helloCall():
    global var1
    global arr
    arr=[]
    for x in range(0,len(var1)):
        if(var1[x].get()==1):
            arr.append(start[x])
    print arr
    start1 = [[] for i in range(len(arr))]
    f=open('variable.txt','r')
    str1=f.read()
    f.close()
    ind=[]
    indend=[]
    indend1=[]
    ind1=[]
    str2=""
    for x in range(0,len(start1)):
        y=[]
        z=[]
        y=[m.start()for m in re.finditer(arr[x],str1)]
        #print 'yyyyyyyyyyyyyyyyyyyyy\n\n\n'+str1[y[0]:]
        
        for z in range(y[0],len(str1)):
            if str1[z]=='c' and str1[z+1]=='l' and str1[z+2]=='a' and str1[z+3]=='s' and str1[z+4]=='s' and str1[z+5]=='e':
                break;
        print z
        str2=str1[y[0]:z]
        print str2
        ind1=[m.start()for m in re.finditer('method:',str2)]
        for x1 in range(0,len(ind1)):
            ind1[x1]=ind1[x1]+7
        indend1=[]
        for x1 in range(0,len(ind1)):
            y1=ind1[x1]
            while(str2[y1]!=';'):
                y1=y1+1
            indend1.append(y1)
        aa=[]
        for x1 in range(0,len(ind1)):
            a=str2[ind1[x1]:indend1[x1]]
            aa.append(a)
            
        start1[x]=aa
    print start1
    arr1=[]
    fst=[]
    fst=start1[0]
    count=0
    for x in range(0,len(fst)):
        print 'xvalue'
        print x
        for x1 in range(1,len(start1)):
            sec=start1[x1]
            print sec
            for x2 in range(0,len(sec)):
            
        
                if(fst[x]==sec[x2]):
                    count=count+1
                   
        if(count==len(start1)-1):
            arr1.append(fst[x])
            
        count=0
    print arr1
    global top
    
    top.destroy()
    import abstractthe
    abstractthe.abstracttheclass(arr,arr1)
