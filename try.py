listy = [[] for i in range(4)]
listy[0] = ['aa']
listy[1]=['bb','dd','cc','aa']
listy[2]=['bb','cc','dd','aa']
listy[3]=['bb','aa']

arr=[]
fst=[]
fst=listy[0]
count=0
for x in range(0,len(fst)):
    for x1 in range(1,len(listy)):
        sec=listy[x1]
        
        for x2 in range(0,len(sec)):
            
        
            if(fst[x]==sec[x2]):
                count=count+1
               
    if(count==len(listy)-1):
        arr.append(fst[x])
        
    count=0
print arr
start1 = [[] for i in range(len(start))]
    for x in range(0,len(ind)):
        y=indend[x]
        if(x<len(indend)-1):
            z=ind[x+1]-6
        else:
            z=len(str1)
        str2=str1[y:z]
        ind1=[m.start()for m in re.finditer('method:',str2)]
        for x1 in range(0,len(ind1)):
            ind1[x1]=ind1[x1]+7
        indend1=[]
        for x1 in range(0,len(ind1)):
            y1=ind1[x1]
            while(str2[y1]!=';'):
                y1=y1+1
            indend1.append(y1)
        aa=[]
        for x1 in range(0,len(ind1)):
            a=str2[ind1[x1]:indend1[x1]]
            aa.append(a)
            print aa
        start1[x]=aa
    print start1
    
