import random
wordList = ['apple', 'desperaux', 'Brzeczyszczykiewicz', 'cheese', 'plant', 'dinosaur',]
gameWord = wordList[random.randint(0,len(wordList)-1)]
gameLetters = []
gameLetters.extend(gameWord) #splits the gameword into letters

gameScoreLetters = []
for i in range(len(gameWord)):
    gameScoreLetters.append("_")

userGuess = ''
userGuessedLetters = []
guesses = 6

while userGuess != gameWord and guesses > 0:
    print(gameWord) #testing remove after
    print(f"\n game word is {gameScoreLetters} and you have {guesses} left")
    userInput = int(input("1.guess a letter\n2.guess a word\n pick 1 or 2: "))
    if userInput == 1:
        print("you chose 1") #testing
        break
    elif userInput == 2:
        print("you chose 2") #testing
        break
    else:
        userInput = int(input("1.guess a letter\n2.guess a word\n pick 1 or 2: "))