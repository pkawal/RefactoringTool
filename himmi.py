from Tkinter import *
import Tkinter as tk
import tkMessageBox
#this Is Function for mouse find
def find(self):
    text.tag_remove('found', '1.0', END)
    s=''
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


root = Tk()

fram = Frame(root)
Label(fram,text='Text to Replace:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Replace')
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
def replace():
    s = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    s1 = edit.get()
    idx = '1.0'
    if s1:
        while 1:
            # changed only text.search() line put on regular expression
            idx = text.search(r'\y%s\y' % s, idx, nocase=1, stopindex=END, regexp=True)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(s))
            text.delete(idx, lastidx)
            text.insert(idx, s1)
            f=text.get("1.0", END)
            text_file = open("preet.txt", "w")
            text_file.write(f)
            text_file.close()
    edit.focus_set()
#CHANGE IN THIS FUNCTION BTW COMMENT REGION FOR REPLACE
butt.config(command=replace)
root.mainloop()
