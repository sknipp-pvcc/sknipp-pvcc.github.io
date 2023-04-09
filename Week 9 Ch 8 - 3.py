#3. Encapsulate

#fruit = "banana"
#count = 0

#for char in fruit:
#    if char == "a":
#        count += 1
#print(count)

# in a function named count_letters, and generalize it so that it accepts the string 
# and the letter as arguments. Make the function return the number of characters, 
# rather than print the answer. The caller should do the printing.



def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

string = "banana"
letter = "a"
count = count_letters(string, letter)
print(count)