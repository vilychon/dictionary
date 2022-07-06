# dic={"a":[4,3,2,8,9],"b":[6,12,18,7]}
# e={}
# for j in dic:
#     x=dic[j]
#     i=-1
#     b=[]
#     while i>-len(x):
#         b.append(x[i])
#         i=i-1
#     e[j]=b
# print(e)

dic={"a":[4,3,2,8,9] ,"b":[6,12,18,7]}
e={}
for j in dic:
    x=dic[j]
    i=-1
    b=[]
    while i>-len(x):
        b.append(x[i])
        i=i-1
    e[j]=b
print(e)

    