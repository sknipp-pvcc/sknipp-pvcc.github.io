#6. Write a function which is given an exam mark, and it returns a string — the grade for
#that mark — according to this scheme:
#
#Mark       Grade
#>= 75      First
#[70-75)    Upper Second
#[60-70)    Second
#[50-60)    Third
#[45-50)    F1 Supp
#[40-45)    F2
#< 40       F3
#
#The square and round brackets denote closed and open intervals. A closed interval in-
#cludes the number, and open interval excludes it. So 39.99999 gets grade F3, but 40 gets
#grade F2. Assume
#
#xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
#Test your function by printing the mark and the grade for all the elements in this list.

# use this list of numbers in your code (yes, a for loop :)

xs = [83,75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for grade in xs:
    if grade >= 75:
        print("First")

    elif grade >= 70 and grade < 75:
        print("Upper Second")

    elif grade >= 60 and grade < 70:
        print ('Second')

    elif grade >= 50 and grade < 60:
        print ('Third')

    elif grade >= 45 and grade < 50:
        print ('F3')

    elif grade >= 40 and grade < 45:
        print ('F2')

    elif grade < 40:
        print ('F3')
        

    




