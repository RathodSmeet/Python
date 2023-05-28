# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

number = int(input("Enter a number : "))

count = 0
while number != 0:
    number //= 10
    count += 1
    
print(count)