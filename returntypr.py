import re
def getreturntype(s):
    print 'in returntype'
    end=[]
    indend=[]
    ab=[]

    f=open('preet.txt','r')
    str=f.read()
    f.close()
    
    f=open('variable.txt','r')
    index=f.read()
    f.close()
    print str
    #s=str[144:160]
    print s
    i=str.find(s)
    print i
    
    ind=[m.start()for m in re.finditer('end:',index)]
    for x in range(0,len(ind)):
        ind[x]=ind[x]+4
    for x in range(0,len(ind)):
        y=ind[x]
        while(index[y]!=':'):
            y=y+1
        indend.append(y)
    for x in range(0,len(ind)):
        a=index[ind[x]:indend[x]]
        end.append(int(a))
    print end
    print i
    print str[i]
    i=i+len(s)
    print i
    print str[i]
    f = open('extractmethod.txt',"r")
    var=f.read() # python will convert \n to os.l
    f.close()
    x=0
    print "kawal"+var
    a=''
    if not var:
        return 'empty'
    while(x<len(var)-1):
        while(var[x]!='-'):
            a=a+var[x]
            x=x+1
            print a
        ab.append(a)
        a=""
        if(var[x+1]=='i'):
            x=x+5
        else:
            if(var[x+1]=='c'):
                x=x+6
            else:
                if(var[x+1]=='f'):
                    x=x+7
                else:
                    if(var[x+1]=='d'):
                        x=x+8
    print "kkkkkk"
    print ab
    indend=[]
    y=i
    print y
    while(not(y in end)):
        y=y+1
        print y
    
    print y
    
    z=len(ab)-1
    
    print ab
    while(z>=0):
        c=[m.start()for m in re.finditer(ab[z],str[i:y])]
        if(len(c)==0):
            ab.remove(ab[z])
        z=z-1
        
    
    print 'preet preet preet .....................................................................................'
    print ab
    if(len(ab)>1):
        return 'no'
    else:
        print 'returntype:'
        if(len(ab)==0):
            return 'empty'
        c=[m.start()for m in re.finditer(ab[0],var)]
        x=c[0]+len(ab[0])+1
        f=open('returnvariable.txt','a')
        f.write(ab[0])
        if var[x]=='i':
            f.write('-int')
            f.close
            return 'int'
        else:
            if var[x]=='c':
                f.write('-int')
                f.close
                return 'char'
            else:
                if var[x]=='f':
                    f.write('-int')
                    f.close
                    return 'float'
                else:
                    if var[x]=='d':
                        f.write('-int')
                        f.close
                        return 'double'
            
        
#getreturntype('cat=5+rat+pat;')
