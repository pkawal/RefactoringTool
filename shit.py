import re
f=open("shit.txt",'r')
s=f.read()
f.close()
global tuy
tuy=0

#s='if(da&&sff||233!e)'
#s='if(user<128 )'
s1='if'
count1=[]
condition=[]
idx=[]
idxend=[]
def getif(s):
    i=[m.start()for m in re.finditer(s1,s)]
    print i
    sur=i[0]
    
    for x in range(0,len(i)):
        i[x]=i[x]+4
    print i
    y=[]
    count=1
    for x in range(0, len(i)):
        count=1
        z=i[x]
        while(count!=0):
              
              if(s[z]==')'):
                  count=count-1
              if(s[z]=='('):
                  count=count+1
              z=z+1
        y.append(z)
    z=0
    print y
    ifinside=[]
    for x in range(0, len(y)):
        ifinside.append(s[i[x]:y[x]-1])
    #print ifinside
    s2='&&'
    s3='||'
    s4='!'
    
    for x in range(0, len(ifinside)):
        count1.append(1)
        idx.append([])
        for h in range(0, len(ifinside[x])):
            if(ifinside[x][h]=='&' and ifinside[x][h+1]=='&' or ifinside[x][h]=='|' and ifinside[x][h+1]=='|' or ifinside[x][h]=='!'):
                count1[x]=count1[x]+1
                idx[x].append(h)
    for r in range (0,len(idx)):
        for w in range (0,len(idx[0])):
            print idx[r]
            
        
                    
    print 'maaaa ki dasshhhh'
    #print idx
    print count1
    j=0
    for x in range(0, len(ifinside)):
        
        if(count1[x]>1):
            for h in range(0, len(ifinside[x])):
                j=h
                if(ifinside[x][h]=='&' and ifinside[x][h+1]=='&'  or  ifinside[x][h]=='|' and ifinside[x][h+1]=='|'):
                    m=len(ifinside[x])
                    n=idx[x]
                    str=ifinside[x]
                    condition.append(str[0:h])
                    condition.append(str[h+2:m])
                if(ifinside[x][h]=='!'):
                    m=len(ifinside[x])
                    str=ifinside[x]
                    condition.append(str[0:h])
                    condition.append(str[h+1:m])
        if(count1[x]==1):
            condition.append(ifinside[x])
    print condition
    f=open("preet.txt",'w')
    f.write("")
    f.close()
    f=open("preet.txt",'a')
    f.write(''+s[0:sur])
    #print ''+s[0:sur]
    f.close()
    tuy='a'
    s9='\n'
    surr=s[sur:]
    for x in range(0,len(condition)):
        f=open("preet.txt",'a')
        f.write( 'boolean var'+repr(x)+'='+condition[x]+';'+s9)
        f.close()
    for x in range(0,len(condition)):
        i=[m.start()for m in re.finditer(condition[x],surr)]
        print i
        for y in range(0,len(i)):
            z=i[y]
            pr=surr[0:z]+'var'+repr(x)+surr[z+len(condition[x]):]
            surr=pr
    print delattr
    f=open("preet.txt",'a')
    f.write(''+surr)
    #print ''+s[sur:]
    f.close()
    print pr


