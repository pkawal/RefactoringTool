import re
def getundeclared(s):
    print 'in undeclared'
    ab=[]
    str1=""
    var=""  
    ab1=[]
    a=[]
    temp=""
    x=0
    ind=[]
    indend=[]
    start=[]
    tempt=s
    while x<len(s):
        if s[x]=='\s' or s[x]=='+' or s[x]=='-' or s[x]=='*' or s[x]==';' or s[x]=='=' or s[x]==' ':
            
            str1=s[0:x+1]
            print "preet"+str1
            temp=s[x:x+1]
            print temp
            str1=str1+temp
            print str1
            y=x+1
            while y!=len(s):
                str1=str1+s[y]
                y=y+1
            s=str1
            x=x+2
            print str1
        x=x+1
    print s
    a=re.findall(r'((\s|\+|\-|\;|\*|\\|\)|\=)\w+(\s|\+|\-|\;|\*|\\|\=))', s)
    print a
    for x in range(0,len(a)):
        str1=a[x][0]
        if(str1[1:-1].isdigit()==0):
           ab.append(str1[1:-1])
    ab=list(set(ab))
    print ab
    f = open('extractmethod.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    if not str1:
        preet(ab,tempt)
        return 
    x=0
    print str1
    while(x<len(str1)-1):
        while(str1[x]!='-'):
            var=var+str1[x]
            x=x+1
        print var
        if var in ab:
            ab.remove(var)
        var=""
        if(str1[x+1]=='i'):
            x=x+5
        else:
            if(str1[x+1]=='c'):
                x=x+6
            else:
                if(str1[x+1]=='f'):
                    x=x+7
                else:
                    if(str1[x+1]=='d'):
                        x=x+8
    print ab
    f = open('variable.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    ind=[m.start()for m in re.finditer('start:',str1)]
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
    for x in range(0,len(ind)):
        a=str1[ind[x]:indend[x]]
        print a
        start.append(int(a))
    print start
    #yahan theek
    f = open('preet.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    print temp
    i=str1.index(tempt)
    print 'index of selection'
    print i
    while(not(i in start)):
        i=i-1
    print 'start index'
    
    print i
    ind=[]
    f = open('variable.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    
    ind=[m.start()for m in re.finditer(str(i),str1)]
    i=ind[0]
    print i
    while(ind[0]<len(str1)):
        if str1[ind[0]]=='e' and str1[ind[0]+1]=='n' and str1[ind[0]+2]=='d':
            break
        ind[0]=ind[0]+1
        print ind[0]
    print 'preet'
    print i
    print ind[0]
    temp=str1[i:ind[0]]
    f=open('extractmethod.txt','w')
    f.write("")
    f.close()
    f=open('extractmethod.txt','a')
    print ab
    print temp
    for x in range(0,len(ab)):
        f.write(ab[x])
        i=temp.index(ab[x])
        print i
        i=i+len(ab[x])
        if(temp[i+1]=='i'):
            f.write('-int\n')
        else:
            if(temp[i+1]=='c'):
                f.write('-char\n')
            else:
                if(temp[i+1]=='f'):
                    f.write('float\n')
                else:
                    if(temp[i+1]=='d'):
                        f.write('double\n')
        
    f.close()
def preet(ab,tempt):
    ind=[]
    indend=[]
    a=""
    str1=""
    temp=""
    start=[]
    f = open('variable.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    ind=[m.start()for m in re.finditer('start:',str1)]
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
    for x in range(0,len(ind)):
        a=str1[ind[x]:indend[x]]
        print a
        start.append(int(a))
    print start
    #yahan theek
    f = open('preet.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    
    i=str1.index(tempt)
    print 'index of selection'
    print i
    while(not(i in start)):
        i=i-1
    print 'start index'
    
    print i
    ind=[]
    f = open('variable.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    
    ind=[m.start()for m in re.finditer(str(i),str1)]
    i=ind[0]
    print i
    while(ind[0]<len(str1)):
        if str1[ind[0]]=='e' and str1[ind[0]+1]=='n' and str1[ind[0]+2]=='d':
            break
        ind[0]=ind[0]+1
        print ind[0]
    print 'preet'
    print i
    print ind[0]
    temp=str1[i:ind[0]]
    f=open('extractmethod.txt','w')
    f.write("")
    f.close()
    f=open('extractmethod.txt','a')
    print ab
    print temp
    for x in range(0,len(ab)):
        f.write(ab[x])
        i=temp.index(ab[x])
        print i
        i=i+len(ab[x])
        if(temp[i+1]=='i'):
            f.write('-int\n')
        else:
            if(temp[i+1]=='c'):
                f.write('-char\n')
            else:
                if(temp[i+1]=='f'):
                    f.write('-float\n')
                else:
                    if(temp[i+1]=='d'):
                        f.write('-double\n')
        
    f.close()
