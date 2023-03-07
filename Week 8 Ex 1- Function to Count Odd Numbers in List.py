#1. Write a function to count how many odd numbers are in a list.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

CountOdd = 0
CountEven = 0

for value in numbers:
    if not value % 2: #if not the category divisible by two
        CountEven+=1  #then count as even
    else:
        CountOdd+=1 #Addition Assignment (original value plus whatever number follows)

print("Number of odd numbers :", CountOdd)