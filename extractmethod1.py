import re
def extract(s,name):
    indend=[]
    start=[]
    f = open('variable.txt',"r")
    str1=f.read() # python will convert \n to os.l
    f.close()
    ind=[m.start()for m in re.finditer('end:',str1)]
    
    print ind
    for x in range(0,len(ind)):
        ind[x]=ind[x]+4
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
    
    index=0
    i=[]
    while index < len(str1):
        index = str1.find(s, index)
        if index == -1:
            break
        i.append(index)
        index += len(s)
    
    print 'index of selection'
    print i
    f=open('returnvariable.txt','r')
    ret=f.read()
    f.close()
    x=0
    while(len(i)):
        if ret:
            while(ret[x]!='-'):
               x=x+1
            pet=str1[0:i[0]]+ret[0:x]+'='+name+'();'+str1[i[0]+len(s):]
            str1=pet
        else:
            pet=str1[0:i[0]]+name+'();'+str1[i[0]+len(s):]
            str1=pet
        index=0
        i=[]
        while index < len(str1):
            index = str1.find(s, index)
            if index == -1:
                break
            i.append(index)
            index += len(s)
    
    a=str1
    str1=pet
    print str1
    print start
    print i
    i=str1.find(s)
    while(not(i in start)):
        i=i-1
        print i
        if i<1:
            break
    f = open('preet.txt',"r")
    preet=f.read() # python will convert \n to os.l
    f.close()
    if(i<1):
        i=0
        while(preet[i]!='{'):
            i=i+1
        i=i+1
    print i
    print str1[i]
    f=open('returnvariable.txt','r')
    ret=f.read()
    f.close()
    x=0
    f=open('extractmethod.txt','r')
    arg=f.read()
    f.close()
    var=""
    ab=[]
    ab1=[]
    while(x<len(arg)-1):
            while(arg[x]!='-'):
                var=var+arg[x]
                x=x+1
            print var

            if(arg[x+1]=='i'):
                ab.append('int')
                ab1.append(var)
                var=""
                x=x+5
            else:
                  if(arg[x+1]=='c'):
                    ab.append('char')
                    ab1.append(var)
                    var=""
                    x=x+6
                  else:
                    if(arg[x+1]=='f'):
                        ab.append('float')
                        ab1.append(var)
                        var=""
                        x=x+7
                    else:
                        if(arg[x+1]=='d'):
                            ab.append('double')
                            ab1.append(var)
                            var=""
                            x=x+8
    print ab
    print ab1
    x=0
    
    pet=""
    for x in range(0,len(ab)):
        pet=ab[x]+' '+ab1[x]+','+pet
    if ret:
        while(ret[x]!='-'):
           x=x+1
        met='\n'+ret[x+1:]+' '+name+'('+pet[0:len(pet)-1]+')\n{\n'+s+'\nreturn '+ret[0:x]+';\n}'
        print met
    else:
        met='\nvoid '+name+'('+pet[0:len(pet)-1]+')\n{\n'+s+'\n}\n'
        print met
    pet=str1[0:i+1]+met+str1[i+1:]
    print pet
    f = open('preet.txt',"w")
    f.write(pet) # python will convert \n to os.l
    f.close()
