# Recursive Function
def my_fact(num):
    if(num==1):
        return 1
    else:
        fact = num * my_fact(num-1)
        return fact
    
ans = my_fact(5)
print(ans)