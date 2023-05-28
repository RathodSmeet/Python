# Write a program to display only those numbers from a list that satisfy the following
# conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number 
# If the number is greater than 500, then stop the loop
# 
#  GIVEN :-
# numbers = [12, 35, 150, 100, 145, 525, 500]

numbers = [12, 25, 150, 100, 145, 525, 50]

for num in numbers:
    if num % 5 == 0:
        print(num)
    elif num > 150:
        continue
    elif num > 500:
        break