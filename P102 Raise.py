# Raise exception/keyword
num1 = int(input("Enter Num1 :"))
if num1 < 0:
    raise Exception("value less than zero")
num2 = int(input("Enter Num2 :"))
if num2 < 0:
    raise ZeroDivisionError("value is zero or less than zero")
ans = num1/num2
print(ans)
