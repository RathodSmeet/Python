# Passing unknown numbers of arguments
# Arbitary arguments
def my_sum(*numbers):
    tot = 0 
    for i in numbers:
        tot += i
    return tot

ans = my_sum()
print(ans)
ans = my_sum(1)
print(ans)
ans=my_sum(1,2,3,4,5,6,7,8,9,10)
print(ans)