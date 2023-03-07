#3. Sum up all the negative numbers in a list.

numbers = [-5, -4, -3, -2,-1,0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sum_neg = 0

for num in numbers:
    if num < 0:
        sum_neg += num
        
print(sum_neg)
