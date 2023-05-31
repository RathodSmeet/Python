#  Try Except
try :
    num1 = int(input("Enter Num1 : "))
    num2 = int(input("Enter Num2 : "))
    ans = num1/num2
    print(ans)
except ZeroDivisionError:
    print("Second value can not be zero")
except ValueError:
    print("Not a valid input")
except :
    print("Any other error")

else:
    print("All Good")