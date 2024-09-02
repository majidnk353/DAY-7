x=[1,2,3,4,5,6]
i=0
c=[]
l=[]
while(i<len(x)):
    if(x[i]%2==0):
        c.append(x[i])
    else:
        l.append(x[i])
    i+=1
print(f"count of even number {len(c)}")
print(f"count of odd number {len(l)}")


        
