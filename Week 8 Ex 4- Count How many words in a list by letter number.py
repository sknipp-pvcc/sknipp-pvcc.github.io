#4. Count how many words in a list have length 5.

word = ["fire", "play", "grade", "cow", "sodas", "there", "ghost", "cabin"]

def word_count(list, length):
    count = 0
    for word in list:
        if len(word) == length:
            count = count + 1
    return count

word_count(word,5)
