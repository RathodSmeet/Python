# Write a program to display all prime numbers within a range

start = int(input ("Enter Lowest Value: "))  
end = int(input ("Enter Upper Value: "))  
  
print ("The Prime Numbers in the range are : ")  
for n in range (start, end + 1):  
    if n > 1:  
        for i in range (2, n):  
            if (n % i) == 0:  
                break  
        else:  
            print (n)