import re
#s='int Demo(int par1,int par2){int total = 10;printf("Hello World");total = total + l;return total;{}}int demo1(int par3,char r){print r;}'

s1='int '
s2='char '
s3='float '
s4='double '
s5='void '
argend=[]

arg=[]
argstr=""
methodstart=0
f = open('java3.txt',"r")
s=f.read() # python will convert \n to os.linesep
f.close()
beg=[]
def getmethod(s,q):
    print s
    i=[m.start()for m in re.finditer(s1,s)]
    iend=[]
    cend=[]
    fend=[]
    dend=[]
    vend=[]

    for x in range(0,len(i)):
        i[x]=i[x]+4
   
    print(i)
    iend=[]
    print iend
    for x in range(0,len(i)):
        y=i[x]
        while s[y]!=';' or s[y]!='(':
            
            
            y=y+1
            if s[y]==';' or s[y]=='(':
                break
        iend.append(y)
    print iend
    
    for x in range(0,len(i)):
        y=i[x]
        z=iend[x]
        if(s[z]=='('):
          print y
          print z
          print('naaaaaammwwww='+s[y:z])
          f = open('variable.txt',"a")
          f.write('method:'+s[y:z]+';\nreturn type:int\n') # python will convert \n to os.linesep
          f.close()
          beg.append(y-4)
          y=z+1
          while(s[z]!=')'):
              z=z+1
          argstr=s[y:z+1]
          print argstr
          argi=[m.start()for m in re.finditer(s1,s[y:z+1])]
          argc=[m.start()for m in re.finditer(s2,s[y:z+1])]
          argf=[m.start()for m in re.finditer(s3,s[y:z+1])]
          argd=[m.start()for m in re.finditer(s4,s[y:z+1])]
          while(s[z]=='{'):
              z=z+1
          
          methodstart=z+1
          f = open('variable.txt',"a")
          f.write('start:'+str(methodstart+q)+':\n')
          f.close()
          print 'kawal'+s[methodstart:]
          print 'preet'+s[methodstart+1]
          argiend=[]
          argcend=[]
          argfend=[]
          argdend=[]
          for x1 in range(0,len(argi)):
              argi[x1]=argi[x1]+4
              z1=argi[x1]
              while(argstr[z1]!=')'):
                 z1=z1+1
                 if(argstr[z1]==','):
                     argiend.append(z1)
              argiend.append(z1)
          for x1 in range(0,len(argc)):
              argc[x1]=argc[x1]+5
              z1=argc[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argcend.append(z1)
              argcend.append(z1)
          for x1 in range(0,len(argf)):
              argf[x1]=argf[x1]+6
              z1=argf[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argfend.append(z1)
              argfend.append(z1)
          for x1 in range(0,len(argd)):
              argd[x1]=argd[x1]+7
              z1=argd[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argdend.append(z1)
              argdend.append(z1)

          
          f = open('variable.txt',"a")
          f.write('arguments:\n') # python will convert \n to os.linesep
          f.close()
          for x1 in range(0,len(argi)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argi[x1]:argiend[x1]]+'-int\n') # python will convert \n to os.linesep
                 f.close()
          for x1 in range(0,len(argc)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argc[x1]:argcend[x1]]+'-char\n')
                 f.close()
          for x1 in range(0,len(argf)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argfs[x1]:argfend[x1]]+'-float\n')
                 f.close()
          for x1 in range(0,len(argd)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argdstart[x1]:argdend[x1]]+'-double\n')
                 f.close()
          count=1;
          methodend=0
          methodinside=""
          methodend=methodstart+2
          
          while(count!=0):
              
              if(s[methodend]=='}'):
                  count=count-1
              if(s[methodend]=='{'):
                  count=count+1
              
              methodend=methodend+1
              
          
          methodinside=s[methodstart:methodend]
          print "kawal+"+methodinside
          f = open('variable.txt',"a")
          f.write('inside:\n')
          f.close()
          
          import variablelist
          variablelist.getintvariable(methodinside)
          variablelist.getcharvariable(methodinside)
          variablelist.getfloatvariable(methodinside)
          variablelist.getdoublevariable(methodinside)
          f=open('variable.txt',"a")
          x=methodend-1
          f.write('end:'+str(x+q)+':\n')
          f.close()
    c=[m.start()for m in re.finditer(s2,s)]

    for x in range(0,len(c)):
        c[x]=c[x]+5
    print 'char'
    print(c)
    for x in range(0,len(c)):
        y=c[x]
        while s[y]!=';' or s[y]!='(':
            if s[y]==';' or s[y]=='(':
                break
            y=y+1
            
        cend.append(y)
    print 'charend'
    print(cend)
    for x in range(0,len(c)):
        y=c[x]
        z=cend[x]
        if(s[z]=='('):
          print(s[y:z])
          f = open('variable.txt',"a")
          f.write('method:'+s[y:z]+';\nreturn type:int\n') # python will convert \n to os.linesep
          f.close()
          beg.append(y-5)
          y=z+1
          while(s[z]!=')'):
              z=z+1
          argstr=s[y:z+1]
          print argstr
          argi=[m.start()for m in re.finditer(s1,s[y:z+1])]
          argc=[m.start()for m in re.finditer(s2,s[y:z+1])]
          argf=[m.start()for m in re.finditer(s3,s[y:z+1])]
          argd=[m.start()for m in re.finditer(s4,s[y:z+1])]
          while(s[z]=='{'):
              z=z+1
          methodstart=z+1
          f = open('variable.txt',"a")
          f.write('start:'+str(methodstart+q)+':\n')
          f.close()
          argiend=[]
          argcend=[]
          argfend=[]
          argdend=[]
          for x1 in range(0,len(argi)):
              argi[x1]=argi[x1]+4
              z1=argi[x1]
              while(argstr[z1]!=')'):
                 z1=z1+1
                 if(argstr[z1]==','):
                     argiend.append(z1)
              argiend.append(z1)
          for x1 in range(0,len(argc)):
              argc[x1]=argc[x1]+5
              z1=argc[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argcend.append(z1)
              argcend.append(z1)
          for x1 in range(0,len(argf)):
              argf[x1]=argf[x1]+6
              z1=argf[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argfend.append(z1)
              argfend.append(z1)
          for x1 in range(0,len(argd)):
              argd[x1]=argd[x1]+7
              z1=argd[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argdend.append(z1)
              argdend.append(z1)

          print s[methodstart]
          f = open('variable.txt',"a")
          f.write('arguments:\n') # python will convert \n to os.linesep
          f.close()
          for x1 in range(0,len(argi)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argi[x1]:argiend[x1]]+'-int\n') # python will convert \n to os.linesep
                 f.close()
          for x1 in range(0,len(argc)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argc[x1]:argcend[x1]]+'-char\n')
                 f.close()
          for x1 in range(0,len(argf)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argfs[x1]:argfend[x1]]+'-float\n')
                 f.close()
          for x1 in range(0,len(argd)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argdstart[x1]:argdend[x1]]+'-double\n')
                 f.close()
          count=1;
          methodend=0
          methodend=methodstart+2
          while(count!=0):
              if(s[methodend]=='}'):
                  count=count-1
              if(s[methodend]=='{'):
                  count=count+1
              methodend=methodend+1
              if(count==0):
                  break
          methodinside=""
          methodinside=s[methodstart:methodend]
          print methodinside
          f = open('variable.txt',"a")
          f.write('inside:\n')
          f.close()
          
          import variablelist
          variablelist.getintvariable(methodinside)
          variablelist.getcharvariable(methodinside)
          variablelist.getfloatvariable(methodinside)
          variablelist.getdoublevariable(methodinside)
          f=open('variable.txt',"a")
          x=methodend
          f.write('end:'+str(x+q)+':\n')
          f.close()
    fl=[m.start()for m in re.finditer(s3,s)]

    for x in range(0,len(fl)):
        fl[x]=fl[x]+6
    print(fl)
    for x in range(0,len(fl)):
        y=fl[x]
        while s[y]!=';' or s[y]!='(':
            y=y+1
            if s[y]==';' or s[y]=='(':
                break
        fend.append(y)
    for x in range(0,len(fl)):
        y=fl[x]
        z=fend[x]
        if(s[z]=='('):
          print(s[y:z])
          f = open('variable.txt',"a")
          f.write('method:'+s[y:z]+';\nreturn type:int\n') # python will convert \n to os.linesep
          f.close()
          beg.append(y-6)
          y=z+1
          while(s[z]!=')'):
              z=z+1
          argstr=s[y:z+1]
          print argstr
          argi=[m.start()for m in re.finditer(s1,s[y:z+1])]
          argc=[m.start()for m in re.finditer(s2,s[y:z+1])]
          argf=[m.start()for m in re.finditer(s3,s[y:z+1])]
          argd=[m.start()for m in re.finditer(s4,s[y:z+1])]
          while(s[z]=='{'):
              z=z+1
          methodstart=z+1
          f = open('variable.txt',"a")
          f.write('start:'+str(methodstart+q)+':\n')
          f.close()
          argiend=[]
          argcend=[]
          argfend=[]
          argdend=[]
          for x1 in range(0,len(argi)):
              argi[x1]=argi[x1]+4
              z1=argi[x1]
              while(argstr[z1]!=')'):
                 z1=z1+1
                 if(argstr[z1]==','):
                     argiend.append(z1)
              argiend.append(z1)
          for x1 in range(0,len(argc)):
              argc[x1]=argc[x1]+5
              z1=argc[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argcend.append(z1)
              argcend.append(z1)
          for x1 in range(0,len(argf)):
              argf[x1]=argf[x1]+6
              z1=argf[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argfend.append(z1)
              argfend.append(z1)
          for x1 in range(0,len(argd)):
              argd[x1]=argd[x1]+7
              z1=argd[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argdend.append(z1)
              argdend.append(z1)

          print s[methodstart]
          f = open('variable.txt',"a")
          f.write('arguments:\n') # python will convert \n to os.linesep
          f.close()
          for x1 in range(0,len(argi)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argi[x1]:argiend[x1]]+'-int\n') # python will convert \n to os.linesep
                 f.close()
          for x1 in range(0,len(argc)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argc[x1]:argcend[x1]]+'-char\n')
                 f.close()
          for x1 in range(0,len(argf)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argfs[x1]:argfend[x1]]+'-float\n')
                 f.close()
          for x1 in range(0,len(argd)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argdstart[x1]:argdend[x1]]+'-double\n')
                 f.close()
          count=1
          methodend=0
          methodend=methodstart+2
          while(count!=0):
              if(s[methodend]=='}'):
                  count=count-1
              if(s[methodend]=='{'):
                  count=count+1
              methodend=methodend+1
              if(count==0):
                  break
          methodinside=""
          methodinside=s[methodstart:methodend]
          print methodinside
          f = open('variable.txt',"a")
          f.write('insisde:\n')
          f.close()
          import variablelist
          variablelist.getintvariable(methodinside)
          variablelist.getcharvariable(methodinside)
          variablelist.getfloatvariable(methodinside)
          variablelist.getdoublevariable(methodinside)
          f=open('variable.txt',"a")
          x=methodend-1
          f.write('end:'+str(x+q)+':\n')
          f.close()
    d=[m.start()for m in re.finditer(s4,s)]

    for x in range(0,len(d)):
        d[x]=d[x]+7
    print(d)
    for x in range(0,len(d)):
        y=d[x]
        while s[y]!=';' or s[y]!='(':
            y=y+1
            if s[y]==';' or s[y]=='(':
                break
        dend.append(y)
    for x in range(0,len(d)):
        y=d[x]
        z=dend[x]
        if(s[z]=='('):
          print(s[y:z])
          f = open('variable.txt',"a")
          f.write('method:'+s[y:z]+';\nreturn type:int\n') # python will convert \n to os.linesep
          f.close()
          beg.append(y-7)
          y=z+1
          while(s[z]!=')'):
              z=z+1
          argstr=s[y:z+1]
          print argstr
          argi=[m.start()for m in re.finditer(s1,s[y:z+1])]
          argc=[m.start()for m in re.finditer(s2,s[y:z+1])]
          argf=[m.start()for m in re.finditer(s3,s[y:z+1])]
          argd=[m.start()for m in re.finditer(s4,s[y:z+1])]
          while(s[z]=='{'):
              z=z+1
          methodstart=z+1
          f = open('variable.txt',"a")
          f.write('start:'+str(methodstart+q)+':\n')
          f.close()
          argiend=[]
          argcend=[]
          argfend=[]
          argdend=[]
          for x1 in range(0,len(argi)):
              argi[x1]=argi[x1]+4
              z1=argi[x1]
              while(argstr[z1]!=')'):
                 z1=z1+1
                 if(argstr[z1]==','):
                     argiend.append(z1)
              argiend.append(z1)
          for x1 in range(0,len(argc)):
              argc[x1]=argc[x1]+5
              z1=argc[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argcend.append(z1)
              argcend.append(z1)
          for x1 in range(0,len(argf)):
              argf[x1]=argf[x1]+6
              z1=argf[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argfend.append(z1)
              argfend.append(z1)
          for x1 in range(0,len(argd)):
              argd[x1]=argd[x1]+7
              z1=argd[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argdend.append(z1)
              argdend.append(z1)

          print s[methodstart]
          f = open('variable.txt',"a")
          f.write('arguments:\n') # python will convert \n to os.linesep
          f.close()
          for x1 in range(0,len(argi)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argi[x1]:argiend[x1]]+'-int\n') # python will convert \n to os.linesep
                 f.close()
          for x1 in range(0,len(argc)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argc[x1]:argcend[x1]]+'-char\n')
                 f.close()
          for x1 in range(0,len(argf)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argfs[x1]:argfend[x1]]+'-float\n')
                 f.close()
          for x1 in range(0,len(argd)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argdstart[x1]:argdend[x1]]+'-double\n')
                 f.close()
          count=1
          methodend=0
          methodend=methodstart+2
          while(count!=0):
              if(s[methodend]=='}'):
                  count=count-1
              if(s[methodend]=='{'):
                  count=count+1
              methodend=methodend+1
              if(count==0):
                  break
          methodinside=""
          methodinside=s[methodstart:methodend]
          print methodinside
          f = open('variable.txt',"a")
          f.write('inside:\n')
          f.close()
          import variablelist
          variablelist.getintvariable(methodinside)
          variablelist.getcharvariable(methodinside)
          variablelist.getfloatvariable(methodinside)
          variablelist.getdoublevariable(methodinside)
          f=open('variable.txt',"a")
          x=methodend-1
          f.write('end:'+str(x+q)+':\n')
          f.close()
    v=[m.start()for m in re.finditer(s5,s)]

    for x in range(0,len(v)):
        v[x]=v[x]+5
    print(v)
    for x in range(0,len(v)):
        y=v[x]
        while s[y]!=';' or s[y]!='(':
            y=y+1
            if s[y]==';' or s[y]=='(':
                break
        vend.append(y)
    for x in range(0,len(v)):
        y=v[x]
        z=vend[x]
        if(s[z]=='('):
          print(s[y:z])
          f = open('variable.txt',"a")
          f.write('method:'+s[y:z]+';\nreturn type:int\n') # python will convert \n to os.linesep
          f.close()
          beg.append(y-5)
          y=z+1
          while(s[z]!=')'):
              z=z+1
          argstr=s[y:z+1]
          print argstr
          argi=[m.start()for m in re.finditer(s1,s[y:z+1])]
          argc=[m.start()for m in re.finditer(s2,s[y:z+1])]
          argf=[m.start()for m in re.finditer(s3,s[y:z+1])]
          argd=[m.start()for m in re.finditer(s4,s[y:z+1])]
          while(s[z]=='{'):
              z=z+1
          methodstart=z+1
          f = open('variable.txt',"a")
          f.write('start:'+str(methodstart+q)+':\n')
          f.close()
          argiend=[]
          argcend=[]
          argfend=[]
          argdend=[]
          for x1 in range(0,len(argi)):
              argi[x1]=argi[x1]+4
              z1=argi[x1]
              while(argstr[z1]!=')'):
                 z1=z1+1
                 if(argstr[z1]==','):
                     argiend.append(z1)
              argiend.append(z1)
          for x1 in range(0,len(argc)):
              argc[x1]=argc[x1]+5
              z1=argc[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argcend.append(z1)
              argcend.append(z1)
          for x1 in range(0,len(argf)):
              argf[x1]=argf[x1]+6
              z1=argf[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argfend.append(z1)
              argfend.append(z1)
          for x1 in range(0,len(argd)):
              argd[x1]=argd[x1]+7
              z1=argd[x1]
              while(argstr[z1]!=')'):
                  z1=z1+1
                  if(argstr[z1]==','):
                      argdend.append(z1)
              argdend.append(z1)

          print s[methodstart]
          f = open('variable.txt',"a")
          f.write('arguments:\n') # python will convert \n to os.linesep
          f.close()
          for x1 in range(0,len(argi)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argi[x1]:argiend[x1]]+'-int\n') # python will convert \n to os.linesep
                 f.close()
          for x1 in range(0,len(argc)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argc[x1]:argcend[x1]]+'-char\n')
                 f.close()
          for x1 in range(0,len(argf)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argfs[x1]:argfend[x1]]+'-float\n')
                 f.close()
          for x1 in range(0,len(argd)):
                 f = open('variable.txt',"a")
                 f.write(argstr[argdstart[x1]:argdend[x1]]+'-double\n')
                 f.close()
          count=1;
          methodend=0
          methodend=methodstart+2
          while(count!=0):
              if(s[methodend]=='}'):
                  count=count-1
              if(s[methodend]=='{'):
                  count=count+1
              methodend=methodend+1
              if(count==0):
                  break
          methodinside=""
          methodinside=s[methodstart:methodend]
          print methodinside
          f = open('variable.txt',"a")
          f.write('inside:\n')
          f.close()
          import variablelist
          variablelist.getintvariable(methodinside)
          variablelist.getcharvariable(methodinside)
          variablelist.getfloatvariable(methodinside)
          variablelist.getdoublevariable(methodinside)
          f=open('variable.txt',"a")
          x=methodend-1
          f.write('end:'+str(x+q)+':\n')
          f.close()
          x=min(beg)
          p=s[0:x]
          f=open('variable.txt',"a")
          f.write('global:\n')
          f.close()
          variablelist.getintvariable(p)
          variablelist.getcharvariable(p)
          variablelist.getfloatvariable(p)
          variablelist.getdoublevariable(p)
