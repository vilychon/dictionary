# dict1={"name":"Rju","marks":56}
# a=input("enter the number:")
# if a in dict1:
#     print("exits")
# else:
#     print("not exist")


# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# for i in dic1:
#     if i in dic2:
#        dic2[i]=dic1[i]+dic2[i]
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d1:
    if i in d2:
        d2[i]=d1[i]+d2[i]
d1.update(d2)
print(d1)



