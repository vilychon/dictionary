# d={1:4,5:6,7:8}
# for x,y in d.items():
#     print(x,y)



# d={1:4,5:6,7:8}
# # b=d.items()
# # print(b)
# a=d.values()
# print(a)


a=[{"a":7},{"a":5}]
b=[]
for i in a:
    for j in i.values():
        if j not in b:
            b.append(j)
print(b)
