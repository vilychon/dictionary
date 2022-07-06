# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dic1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dic2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
for i in dic1:
    if i in dic2:
       dic2[i]=dic1[i]
dic1.update(dic2)
print(dic1)

