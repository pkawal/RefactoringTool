import re
s1='int '
s2='char '
s3='float '
s4='double '
#s='int a;int d; int abc=10; int s , d; int q=10,w=12;char x;char w,r; float e=10.33; double i=99;'
#str=list('int a;int d; int abc=10; int s , d; int q=10,w=12;char x;char w,r; float e=10.33; double i=99;')

s='{int cat,mat;'
iend=[]
cend=[]
fend=[]
dend=[]
var=""
def getintvariable(s):
    print s
    str=list(s)
    i=[m.start()for m in re.finditer(s1,s)]
    var=""
    print i
    for x in range(0,len(i)):
        i[x]=i[x]+4
    print(i)
    iend=[]
    for x in range(0,len(i)):
        y=i[x]
        while(s[y]!=';'):
            y=y+1
            print y
        iend.append(y)
    print(iend)
    for x in range(0,len(i)):
        y=i[x]
        z=iend[x]
        for x1 in range(y,z+1):
        
            if str[x1]!=';'and str[x1]!=' ' and str[x1]!='=' and str[x1]!=',':
                var=var+str[x1]
            if str[x1]==';'or str[x1]==' ' or str[x1]=='=' or str[x1]==',':
                var=var.strip()
           
                if var.isdigit()==0 and var:
                    f = open('variable.txt',"a")
                    f.write(var+'-int\n') # python will convert \n to os.linesep
                    f.close()
                    print(var)
            
                var=""
                if(str[x1]==';'):
                    break
    
def getcharvariable(s):
    var=""
    c=[m.start()for m in re.finditer(s2,s)]
    str=list(s)
    for x in range(0,len(c)):
        c[x]=c[x]+5
    print(c)
    for x in range(0,len(c)):
        y=c[x]
        while(s[y]!=';'):
            y=y+1
        cend.append(y)
    print(cend)
    for x in range(0,len(c)):
        y=c[x]
        z=cend[x]
        for x1 in range(y,z+1):
        
            if str[x1]!=';'and str[x1]!=' ' and str[x1]!='=' and str[x1]!=',':
                var=var+str[x1]
            if str[x1]==';'or str[x1]==' ' or str[x1]=='=' or str[x1]==',':
                var=var.strip()
           
                if var.isdigit()==0 and var and var[0]!="'":
                    f = open('variable.txt',"a")
                    f.write(var+'-char\n') # python will convert \n to os.linesep
                    f.close()
                    print(var)
            
                var=""
                if(str[x1]==';'):
                    break
    
def getfloatvariable(s):
    var=""
    fl=[m.start()for m in re.finditer(s3,s)]
    str=list(s)
    for x in range(0,len(fl)):
        fl[x]=fl[x]+6
    print(fl)
    for x in range(0,len(fl)):
        y=fl[x]
        while(s[y]!=';'):
            y=y+1
        fend.append(y)
    print(fend)
    for x in range(0,len(fl)):
        y=fl[x]
        z=fend[x]
        for x1 in range(y,z+1):
        
            if str[x1]!=';'and str[x1]!=' ' and str[x1]!='=' and str[x1]!=',':
                var=var+str[x1]
            if str[x1]==';'or str[x1]==' ' or str[x1]=='=' or str[x1]==',':
                var=var.strip()
        
                if var.isdigit()==0 and var and re.match("^\d+?\.\d+?$", var) is None:
                    f1 = open('variable.txt',"a")
                    f1.write(var+'-float\n') # python will convert \n to os.linesep
                    f1.close()
                    print(var)
                var=""
                if(str[x1]==';'):
                    break
def getdoublevariable(s):
    d=[m.start()for m in re.finditer(s4,s)]
    var=""

    str=list(s)
    for x in range(0,len(d)):
        d[x]=d[x]+7
    print(d)
    for x in range(0,len(d)):
        y=d[x]
        while(s[y]!=';'):
            y=y+1
        dend.append(y)
    print(dend)
    for x in range(0,len(d)):
        y=d[x]
        z=dend[x]
        for x1 in range(y,z+1):
        
            if str[x1]!=';'and str[x1]!=' ' and str[x1]!='=' and str[x1]!=',':
                var=var+str[x1]
            if str[x1]==';'or str[x1]==' ' or str[x1]=='=' or str[x1]==',':
                var=var.strip()
        
                if var.isdigit()==0 and var and re.match("^\d+?\.\d+?$", var) is None:
                    f1 = open('variable.txt',"a")
                    f1.write(var+'-double\n') # python will convert \n to os.linesep
                    f1.close()
                    print(var)
                var=""
                if(str[x1]==';'):
                    break
