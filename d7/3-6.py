x=[1,-2,3,-5,0]
i=0
c=[]
n=[]
while(i<len(x)):
    if(x[i]>=0):
        c.append(x[i])
    else:
        n.append(x[i])
    i+=1    
print(f"positive integers are:{c}")
print(f"negative integers are:{n}")
    
    
