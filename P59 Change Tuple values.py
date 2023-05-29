# Change Tuple values
tpl1 = (10,20,30,40,50,60)
lst1 = list(tpl1)
lst1[0] = 100
tpl1 = tuple(lst1)
print(tpl1)