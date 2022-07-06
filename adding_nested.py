# dic={1:{"name":"katim","age":23},
# 2:{"name":"themshing","age":21}}
# dic[1]["phone"]=12345678
# dic[2]["phone"]=12345678
# print(dic)
# # for i in dic:
# #     print("Content dic:",i)
# #     for j in dic[i]:
# # #         print(" ",j,":",dic[i][j])
# 
# 
# 

dic1={1:{"name":"katim","age":23},
2:{"name":"themshing","age":21}}
dic2={'a': 300, 'b': 200, 'd':400}
# for i in dic1:
#     for j in dic2: 
#         if j in dic1:
#              dic2[i]=dic1[i]+dic2[i]
dic1.update(dic2)
print(dic1)
