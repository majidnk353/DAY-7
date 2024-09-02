#2 largest no of list
x=[1,2,3,4,5]
i=0
max=0
while i<len(x):
    if(x[i]>max):
        max=x[i]
    i+=1
print(f"the largest number in the list:{max}")   

