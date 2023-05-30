# Removes the items in this set that are also included 
# in another, specified set
set1 = {10,20,30,40}
set2 = {30,40,50,60,70}
set1.difference_update(set2)
print(set1)
