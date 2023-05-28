""""Print the following pattern
1
12
123
1234
12345
"""
i=1
while i <=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j +=1
    print()
    i +=1
else :
    print("End of loop")