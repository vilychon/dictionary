ID={1:{"name":"katim","age":23},
2:{"name":"themshing","age":"21"}}
a=[]
for i in ID:
    for j in ID[i]:
        a.append(ID[i][j])
print(a[0])



# for i in ID.values():
#     x= i["name"]
#     print(x)
#     break



# print(ID[1]["name"])
