# Q14.Write a Python program to multiply all the items in a dictionary.
d={'a':2,'b':4,'c':6,'d':8}
def pro(d):
    mul=1
    for i in d:
        mul=mul*d[i]
    return mul
print(pro(d))