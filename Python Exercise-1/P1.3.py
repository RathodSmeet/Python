# Calculate the sum of all numbers from 1 to a given number
n = int(input("Enter Number: "))
sum = 0
while n > 0:
    sum += n
    n -=1
print(sum)