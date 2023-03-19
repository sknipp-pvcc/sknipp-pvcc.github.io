# 4. Now rewrite the count_letters function so that instead of traversing the
# string, it repeatedly calls the butiln find method, with the optional third
# parameter to locate new occurrences of the letter being counted.

string = "bananas"
letter = "a"

def count_letters(string, letter):
    count = 0
    start = 0
    while True:
        idx = string.find(letter, start, len(string))
        if idx == -1:
            break
        count += 1
        start = idx + 1
    return count


count_letters(string, letter)