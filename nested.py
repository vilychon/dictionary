list1=["one","two","three","four"]
list2=[1,2,3,4]
l={}
c={}
i=0
while i<len(list1):
    l[list1[i]]=list2[i]
    i=i+1
print(l)
c['numbers']=l
print(c)