# a=list(map(int,input().split()))
a=input().split()
b={}
for i in a:
    if i in b:
        b[i]+=1
print(b)
for j in b:
    if b[j]==1:
        print(j)
        break
