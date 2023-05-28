# Reverse a given integer number
# Given:
# 76542
# Expected output:
# 24567

number = 76542
rev = 0  
  
while (number > 0):  
    rem = number % 10  
    rev = (rev * 10) + rem 
    number = number // 10  
  
print(rev)