# Q19.
# Write a Python program to remove duplicates from Dictionary. = {'id1': 
dic = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
a = []
res = dict()
for key, val in dic.items():
    if val not in a:
        a.append(val)
        res[key] = val
print("dic: " + str(res))