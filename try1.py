from Tkinter import *
import Tkinter as tk
import tkMessageBox
#this Is Function for mouse find
returntype=""
ind=[]
def find(self):
    
    text.tag_remove('found', '1.0', END)
    s=''
    global s
    global qqq
    s = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    try:
      s = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    except:
      tkMessageBox.showinfo("Error", "Please select Text")
    if s:
        idx = '1.0'
        while 1:
     # changed only text.search() line put on regular expression

            idx = text.search(r'\y%s\y' % s, idx, nocase=1, stopindex=END, regexp=True)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(s))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        text.tag_config('found', foreground='red')
        f=open('preet.txt','r')
        str1=f.read()
        f.close()
        global ind
        ind=[m.start()for m in re.finditer(s+'=',str1)]
        print ind
        if(len(ind)>1.1):
            tkMessageBox.showinfo("Error", "Not a Temporary Variable")
            text.tag_config('found', foreground='black')
        else:
            x=ind[0]
            while(str1[x]!=';'):
                x=x+1
            qqq=s    
            s=' '+str1[ind[0]:x+1]
            
            print s
            import declaredvariablelist
            declaredvariablelist.getintvariable(s)
            declaredvariablelist.getcharvariable(s)
            declaredvariablelist.getfloatvariable(s)
            declaredvariablelist.getdoublevariable(s)
            import returntypr
            global returntype
            returntype=returntypr.getreturntype(s)
            print returntype
            import undeclaredvariablelist
            undeclaredvariablelist.getundeclared(s)
            print returntype
            if returntype=='no':
                tkMessageBox.showinfo('Error','Invalid selection')
            if returntype=='empty':
                import alagreturn
                returntype=alagreturn.func(s)
        
    
        #returntype=alagreturn.decidereturn(var)
    
root = Tk()

fram = Frame(root)
Label(fram,text='Method Name:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Extract')
butt.pack(side=RIGHT)
fram.pack(side=TOP)
a=""
with open("preet.txt", "r") as f:
  for line in f:
    a=a+line
 
text = Text(root)
text.insert('1.0',a)
text.pack(side=BOTTOM)
text.bind("<ButtonRelease-1>", find)
#Below function will be used for replace
#Change IN THIS FUNCTION BTW COMMENT REGION FOR REPLACE
def replace(returntype):
    s1 = edit.get()
    global qqq
    global s
    f=open('extractmethod.txt','r')
    s2=f.read()
    f.close()
    baby='returntype:'+returntype+'\nname:'+s1+'\narguments:\n'+s2
    tkMessageBox.showinfo('Method Details','mynameiskhan\n'+baby)
    import extractmethod1
    extractmethod1.extract(s,s1)
    f=open('preet.txt','r')
    s2=f.read()
    f.close()
    ind1=[]
    index=0
    print qqq
    ind1=[m.start()for m in re.finditer(qqq,s2)]
    ind=[]
    ind=[m.start()for m in re.finditer(qqq+'=',s2)]
    print ind1
    print ind
    baby=""
    print 'nswdbxiwheyrfuerygfvyebfveyfvuy'
    x=0
    
    while(x<len(ind1)):
        if(ind1[x]>ind[1]):
            baby=s2[0:ind1[x]]+s1+'()'+s2[ind1[x]+len(qqq):]
            s2=baby
        x=x+1
        break
    print s2
    root.destroy()
    
#CHANGE IN THIS FUNCTION BTW COMMENT REGION FOR REPLACE
butt.config(command= lambda: replace(returntype))
root.mainloop()
    
