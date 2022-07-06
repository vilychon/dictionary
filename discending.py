# discending##


# dict={"vily":49,"themshing":39,"salu":66}
# for x in dict:
#     for k in dict:
#         if dict[x]<dict[k]:
#             dict[x],dict[k]=dict[k],dict[x]
#         if dict[k]<dict[x]:
#             dict[k],dict[x]=dict[x],dict[k]
# print(dict)


dict={"vily":50,"shangkhu":50,"katim":55}
for x in dict:
    for k in dict:
        if dict[x]<dict[k]:
            dict[x],dict[k]=dict[k],dict[x]
        if dict[k]<dict[x]:
            dict[k],dict[x]=dict[x],dict[k]
print(dict)



