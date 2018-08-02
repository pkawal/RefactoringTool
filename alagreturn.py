from Tkinter import *
import tkSimpleDialog
def func(ss):
        print 'in alag return'
        global ab
        ab=[]
        ind=[]
        indend=[]
        end=[]
        f=open('extractmethod.txt','r')
        s=f.read()
        f.close()
        x=0
        var=""
        while(x<len(s)-1):
                while(s[x]!='-'):
                    var=var+s[x]
                    x=x+1
                print var
                ab.append(var)
                var=""
                if(s[x+1]=='i'):
                    x=x+5
                else:
                    if(s[x+1]=='c'):
                        x=x+6
                    else:
                        if(s[x+1]=='f'):
                            x=x+7
                        else:
                            if(s[x+1]=='d'):
                                x=x+8
        print ab
        f=open('variable.txt','r')
        index=f.read()
        f.close()
        f=open('preet.txt','r')
        str=f.read()
        f.close()
        i=str.find(ss)
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
        i=i+len(ss)
        f = open('extractmethod.txt',"r")
        var=f.read() # python will convert \n to os.l
        f.close()
        ab=[]
        a=""
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
    
        print ab
        y=i
        print y
        while(not(y in end)):
                y=y+1
                print y
                if(y<1):
                        break
    
        print y
    
        z=len(ab)-1
    
        while(z>=0):
                c=[m.start()for m in re.finditer(ab[z],str[i:y])]
                if(len(c)==0):
                    ab.remove(ab[z])
                z=z-1
        
        
        print 'knfkjawekfufitwuiswkigtfueubgeugtfuguetiriugteiuhbrtfeyiteuuugt4rieugt4riegt4regitgrdfhhbhbr'
        print ab
        if(len(ab)<1):
                return 'void'
        x=len(ss)-1
        var=""
        while(ss[x]!='='):
            x=x-1
        while(ss[x]!=';'):
            var=var+ss[x]
            x=x-1
        
        var=var[::-1]
        print var
        x=len(var)
        print 'knfkjawekfufitwuiswkigtfueubgeugtfuguetiriugteiuhbrtfeyiteuuugt4rieugt4riegt4regitgrdfhhbhbr'
        print var[0:x-1]
        preet=re.sub('\s+',' ',var[0:x-1])
        i=s.find(preet)
        
        print i
        i=i+len(preet)+1
        print s[i]
        f=open('returnvariable.txt','w')
        f.write(preet)
        if(s[i]=='i'):
            f.write('-int')
            f.close
            s='int'
        else:
            if(s[i]=='c'):
                 f.write('-char')
                 f.close
                 s= 'char'
            
            else:
                 if(s[i]=='f'):
                     f.write('-float')
                     f.close
                     s='float'
            
                 else:
                     if(s[i]=='d'):
                         f.write('-double')
                         f.close
                         s='double'
                         
        print s 
        return s   
