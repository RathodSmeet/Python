# Write a program to print the following start pattern using the for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 5
for i in range(1, n + 1):
    print("* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i)