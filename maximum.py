# a={"a":34,"b":1,"c":43,"d":44}
# max=0
# for i in a:
#     if a[i]>max:
#         max=a[i]
# print(max)                              


# a=[9,[1,2,3],[4,5,[6,7,8,9,[10]]]]
# print(a[0])
# print(a[1][1])
# print(a[2][0])
# print(a[2][2][1])
# print(a[2][2][4][0])





list=[1,2,"amla","vily",2.3,2.4]
i=0
a,b,c=[],[],[]
while i<len(list):
    if type(list[i])==str:
        a.append (list[i])
    elif type(list[i])==float:
        b.append (list[i])
    elif type(list[i])==int:
        c.append (list[i])
    i=i+1
print(a)
print(b)
print(c)
