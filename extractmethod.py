from Tkinter import *
import Tkinter as tk
import tkMessageBox
#this Is Function for mouse find
returntype=""
def find(self):
    
    text.tag_remove('found', '1.0', END)
    s=''
    global s
    s = text.get(tk.SEL_FIRST, tk.SEL_LAST)
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
    
    global s
    f=open('extractmethod.txt','r')
    s2=f.read()
    f.close()
    baby='returntype:'+returntype+'\nname:'+s1+'\narguments:\n'+s2
    tkMessageBox.showinfo('Method Details','mynameiskhan\n'+baby)
    import extractmethod1
    extractmethod1.extract(s,s1)
    root.destroy()
    
#CHANGE IN THIS FUNCTION BTW COMMENT REGION FOR REPLACE
butt.config(command= lambda: replace(returntype))
root.mainloop()
