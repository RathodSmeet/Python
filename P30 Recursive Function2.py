# Recursive Function
def my_sum(num):
    if num < 10 :
        return num
    else:
        s = (num%10) * my_sum(num//10)
        return s
    
ans = my_sum(1234)
print(ans)