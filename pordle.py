#Name: Sarah Knipp
#Program Purpose: Pordle (PVCC Wordle): Word Guessing Game
#   The program chooses a random word from a file of words. The use tries to 
#   figure out the word in the fewest guessses by guessing letters in the word.
#   This program uses an input FILE, LISTS, and STRING SLICES (sections of the string)

import random
wordList = []
inFile = "animals.txt"
global wordFile

def main():
    global wordList, inFile
    playAgain = True
    while playAgain:
        printHeadings()
        printMenu()
        wordFile = open(inFile, "r") #open the file for READ
        for textLine in wordFile: # read in a line of text from the file
            for word in textLine.split(): #split the line of text into words
                wordList.append(word) #add each word to the word 
        wordFile.close()
        playGame()
        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == "n" or yesno == "N":
            playAgain = False
            print("Thank you for playing Pordle!")
            break

def printHeadings():
    print("Welcome to Pordle! The PVCC Wordle Game!")
    print("I will think of a word and you try to guess the lettes in the word.")
    print("The number of dashes indicates the number of letterrs in the word.")
    print("Get ready for a new word....")

def printMenu():
    global inFile
    print("Choose a PORDLE category:")
    print("\t1. Animals") #animals
    print("\t2. Foods") #animals
    print("\t3. Colors") #animals
    print("\t4. Flowers")#animals
    category = input("Please enter the category number: ")

    if category == "1":
        inFile = "animals.txt"
        print("This will be Animal Pordle!")
    elif category == "2":
        inFile = "foods.txt"
        print("This will be Food Pordle!")
    elif category == "3":
        inFile = "colors.txt"
        print("This will be Color Pordle!")
    elif category == "4":
        inFile = "flowers.txt"
        print("This will be Flower Pordle!")
    else: 
        quit()
        

def playGame():
    numguesses = 1
    lettersUsed = []

    wordChosen = random.choice (wordList)
    pordle = wordChosen
    for i in range (len(pordle)):
        pordle = pordle [0:i] + "_" + pordle [i + 1 :] #Use Slice to replace each letter with a '_'
    print (" ".join(pordle)) #the "join" will put a space between each underscore

    while pordle !=wordChosen: # keep asking the playuer until player guess the word
         letterGuess = input("Please enter a letter: ")
         letterGuess = letterGuess.lower()
         lettersUsed.append(letterGuess) #Add the players' letter to the list of guessed letters
         print ("Numer of guesses: " + str(numguesses))

         for i in range(len(wordChosen)): #Search throught the letters to find a match
            if wordChosen [i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle [i+1:]
                print("Used letters: ")
                print(lettersUsed)
                print(" ".join(pordle)) #Print the string with guessed letter with spaces in between
                numguesses += 1
    
    print("Well done! You guess in "+ str(numguesses-1) + " guesses!")

main()

