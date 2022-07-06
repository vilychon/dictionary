ID={1:{"name":"katim","age":23},
2:{"name":"themshing","age":"21"}}
for i in ID:
    print("Person ID:",i)
    for j in ID[i]:
        print(" ",j,":",ID[i][j])
# 
# a=[]
# for i in ID:
#     for j in ID[i]:
#         a.append(ID[i][j])
# print(a[0])

# for i in ID.values():
#     x= i["name"]
#     print(x)
#     break


# for i in ID:
    # print(i.value())

# print(ID[1]["name"])