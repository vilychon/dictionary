a="abcdcbabe"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else: 
        b[i]=1
print(b)
l=[]
for j in range(len(a)):
    if b[a[j]]==1:
        print(j)
        break


# l=[]
# for j in b:
#     l.append(b[j])
# k=0
# while k<len(l):
#     if l[k]==1:
#         print(k)
#         break
#     k+=1