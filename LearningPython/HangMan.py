from random import randint

def GetRandomWord():
    return words[randint(0, len(words) - 1)]

def PrintHangman(misses):
    if (misses == 1):
        print('  ____')
        print(' |    |')
        print(' |    ')
        print(' |    ')
        print(' |    ')
        print(' |    ')
        print('_|_    ')
    elif (misses == 2):
        print('  ____')
        print(' |    |')
        print(' |    O')
        print(' |    ')
        print(' |    ')
        print(' |    ')
        print('_|_    ')
    elif (misses == 3):
        print('  ____')
        print(' |    |')
        print(' |    O')
        print(' |   \|/')
        print(' |    ')
        print(' |    ')
        print('_|_    ')
    elif (misses == 4):
        print('  ____')
        print(' |    |')
        print(' |    O')
        print(' |   \|/')
        print(' |    |')
        print(' |    ')
        print('_|_    ')
    elif (misses == 5):
        print('  ____')
        print(' |    |')
        print(' |    O')
        print(' |   \\|/')
        print(' |    |')
        print(' |    /\\')
        print('_|_    ')
        print()

def StartGame():
    tries = 5
    guessedLetters = 0
    misses = 0
    randomWord = GetRandomWord()

    field = []
    for ch in randomWord:
        field.append('-')
        print('-', end="")
    print()

    while(tries > 0 and guessedLetters != len(randomWord)):
        letter = input('Enter letter:')
        if(len(letter) > 1):
            tries -= 1
            print('Please enter single character!')
            continue

        guessOnMove = False
        for i in range(0, len(randomWord)):
            if randomWord[i] == letter:
                guessedLetters += 1
                guessOnMove = True
                field[i] = letter

        if(guessOnMove):
            print('Great!')
        else:
            print('Bad luck')
            tries -= 1
            PrintHangman(5 - tries)

        for ch in field:
            print(ch, end="")
        print()

        print('Tries left: ', tries)

    if(tries == 0):
        print('Game over')
    else:
        print('You have won!')

def Simulate(number):
    wins = 0
    for i in range(0, number):
        vocabulary = []

        commonLetters = ['a', 'e', 'i', 'o', 'u']

        tries = 5
        guessedLetters = {}
        randomWord = GetRandomWord()

        for word in words: # Can be changed to all existing words
            if len(word) == len(randomWord):
                vocabulary.append(word)

        while(tries > 0 and len(guessedLetters) < len(randomWord)):
            letter = ''
            # First letter should be guessed randomly from vowels
            if(len(guessedLetters) == 0):
                letter = commonLetters[randint(0, len(commonLetters) - 1)]
                commonLetters.remove(letter)
            else:
                # Clean up vocabulary of unwanted words
                for word in vocabulary:
                    for i in guessedLetters:
                        if(guessedLetters[i] != word[i]):
                            vocabulary.remove(word)
                            break

                # Make a wild guess from remaining words
                randomWordGuess = vocabulary[randint(0, len(vocabulary) - 1)]

                # Take unused letter from the wild guess
                for l in randomWordGuess:
                    found = False
                    for g in guessedLetters:
                        if l == guessedLetters[g]:
                            found = True
                    if(not found):
                        letter = l
                
            if len(letter) != 1:
                continue

            guessOnMove = False
            for i in range(0, len(randomWord)):
                if randomWord[i] == letter:
                    guessedLetters[i] = letter
                    guessOnMove = True
            
            if(not guessOnMove):
                tries -= 1

        if(tries > 0):
            wins += 1

    return wins / number * 100


words = []
with open('words.txt') as f:
   for line in f.readlines():
       words.append(line)

#StartGame()

print(Simulate(100), '%')