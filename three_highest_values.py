my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[]
for i in my_dict:
    a.append(my_dict[i])
    a.sort()
print(a[-3:])