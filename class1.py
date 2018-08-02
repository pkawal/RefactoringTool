import re
s6='class '

f= open('shit.txt',"r")
s=f.read()
f.close()
iend=[]

def getclass(s):
  d=[m.start()for m in re.finditer(s6,s)]
  i=[]
  istart=[]
  iistart=[]
  for y in range (0,len(d)):
    d[y]=d[y]+6
    print 'd[y]'
    print d[y]
  for z in range (0,len(d)):
    w=d[z]
    while(s[w]!='{'):
      w=w+1
    print s[d[z]:w]
    istart.append(w)
    i=[m.start()for m in re.finditer(' extends ',s[d[z]:w])]
    if(len(i)>0):
       print i
       
       iistart.append(d[z]+i[0])
    else:
       iistart.append(w-1)
    
  f=open('variable.txt',"w")
  f.write("")
  f.close()
  
  
  for q in range (0,len(d)):
    a=istart[q]+1
    count =1
    while(count!=0):
      if(s[a]=='{'):
        count =count+1
      if(s[a]=='}'):
        count=count-1
      a=a+1
    iend.append(a)
  a=""
  b=""
  
  
 
  for e in range (0,len(d)):
    f=open('variable.txt',"a")
    f.write('class:'+ s[d[e]:(iistart[e])]+':\n')
    f.close()
    f=open('variable.txt',"a")
    import methodlist
    methodlist.getmethod(s[istart[e]+1:iend[e]-1],istart[e]+1)
    f.close()
    f=open('variable.txt',"a")
    f.write('classend\n')
    f.close()
    #print 'class:'+ s[d[e]:(iistart[e])]+':\n'
    #print 'method'+s[istart[e]+1:iend[e]-1]
getclass(s)

