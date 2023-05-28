# Copy reference the List
num1 = [10,20,30,40,50,60]
num2 = num1 # copies the reference
num2[1] = 200
num1[5] = 600
print(num1) # [10, 200, 30, 40, 50, 600]
print(num2) # [10, 200, 30, 40, 50, 600]