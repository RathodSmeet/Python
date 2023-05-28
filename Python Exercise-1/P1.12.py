# Display Fibonacci series up to 10 terms
 
n = 10
n1 = 0  
n2 = 1  
count = 0  
if n == 1:  
    print(n1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n:  
        print(n1)  
        temp = n1 + n2  
        n1 = n2  
        n2 = temp  
        count += 1  