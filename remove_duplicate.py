# remove duplicate   #output 90 & 120
a=[6,1,3,5,6,3,2] 
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
# j=0
# t=1
# while j<len(b)-1:
#     t=b[j]*t
#     j=j+1
# print(t)
j=0
t=1
sum=0
while j<len(b)-1:
    t=t*b[j]
    j=j+1
    sum=sum+t
print(t)
print(sum)






    



