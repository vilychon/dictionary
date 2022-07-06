# Q16.Write a Python program to map two lists into a dictionary.
# 

x=["mango","apple","papaya","grapes"]
y=[50,60,70,80]
a=zip(x,y)  
b={}
for i,j in a:
    if i not in b:
        a[i]=y
    else:
        pass
print(b)

# OR

# x=["mango","apple","papaya","grapes"]
# y=[50,60,70,80]
# a=dict(zip(x,y))
# print(a)



