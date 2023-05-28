#Default parameter
def my_function(base,power=2):
    ans = 1
    for i in range(power):
        ans *= base
    return ans

ans = my_function(5)
print(ans)