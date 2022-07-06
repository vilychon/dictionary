i=1
a=[]
b=[]
while i<=3:
    keys=input("enter the name:")
    value=int(input("enter the marks:"))
    a.append(keys)
    b.append(value)
    j=0
    c={}
    while j<len(a):
        c[a[j]]=b[j]
        j+=1
    i+=1
print(c)