# 5. Assign to a variable in your program a triple-quoted string that contains 
# your favourite paragraph of text — perhaps a poem, a speech, instructions to 
# bake a cake, some inspirational verses, etc.
# 
# Write a function which removes all punctuation from the string, breaks the 
# string into a list of words, and counts the number of words in your text 
# that contain the letter “e”.
# 
# Your program should print an analysis of the text like this:
# 
#     Your text contains 243 words, of which 109 (44.8%) contain an "e".


import string

def count_things():
    quote = """I see practical enlightenment as becoming comfortable with the idea that some suffering is always inevitable—that no matter what you do, life is comprised of failures, loss, regrets, and even death. Because once you become comfortable with all the shit that life throws at you (and it will throw a lot of shit, trust me), you become invincible in a sort of low-level spiritual way. After all, the only way to overcome pain is to first learn how to bear it."""
   
    location = " -The Subtle Art of Not Giving a F*ck by Mark Manson"

    translator = str.maketrans("", "", string.punctuation)
    quote_no_punct = quote.translate(translator)

    words = quote_no_punct.split()
    num_total_words = len(words)

    num_e_words = 0
    for word in words:
        if 'e' in word:
            num_e_words += 1


    percent_e_words = num_e_words / num_total_words * 100

    print(quote + location)
    print(f"Total number of words: {num_total_words}")
    print(f"Number of words with 'e': {num_e_words}")
    print(f"Percentage of words with 'e': {percent_e_words:.2f}%")

count_things()
