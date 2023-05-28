# Delete List
numbers = [10,20,30,40,50,60]
print(numbers)
del numbers[3] # will delete number at index 3
print(numbers) # [10, 20, 30, 50, 60]
del numbers # will delete the list
print(numbers) # will raise error,as list deleted