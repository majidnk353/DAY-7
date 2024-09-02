x=[1,2,3,4,5,5,5]
i=0
k=0
c=[]
while(i<len(x)):
    while(k<len(x)):
        if(x[i]==x[k]):
            c.append(x[k])
            k+=1
    i+=1
print(f"the duplicate elments are:{c}")
            
