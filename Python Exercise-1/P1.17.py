# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become
# 2 + 22 + 222 + 2222 + 22222 = 24690
n = 5
term = 2
sum = term
for i in range(2, n + 1):
    term = term * 10 + 2
    sum += term
    
print(sum)


# def calculate_series_sum(n):
#     term = 2
#     series_sum = term
#     for i in range(2, n + 1):
#         term = term * 10 + 2
#         series_sum += term
#     return series_sum

# # Example usage
# n = 5
# result = calculate_series_sum(n)
# print("The sum of the series up to the", n, "term is", result)
