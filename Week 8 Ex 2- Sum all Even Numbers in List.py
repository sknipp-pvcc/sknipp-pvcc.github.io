# 2. Sum up all the even numbers in a list.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

EvenNumbers = [num for num in numbers if num % 2 == 0]

print ("Even numbers in the list: ", EvenNumbers)

print ("Sum of even numbers in list: ", sum(EvenNumbers))
