import random

SECRET_LEN = 3
MAX_GUESSES = 10
CHARACTERS = '0123456789ABC'

def main():
    """MasterMind"""
    print('''Find a SECRET_LEN-length of unique characters of {}.
    clue:
    When i say...
          Piko      one character is correct, but in the wrong position
          Fermio    one character is correct, and in the right position
          Bagel     none of the characters are correct
          
    exanoke:
          secret is 592, if You write 296 the clue will be:
          Fermi Piko.
    '''.format(CHARACTERS))

    while True:
        secretNum = getSecretNum()
        guessNum = 1
        while guessNum <= MAX_GUESSES:
            guess = ''
            while not correctInput(guess):
                print("Attempt nr: {}".format(guessNum))
                guess = input('> ')
            
            if checkGuess(guess, secretNum):
                break
            
            guessNum += 1


        print("Do You want to try again? yes/no")
        if not input('> ').lower().startswith('y'):
            break
    print("Thank You for game.")

def getSecretNum():
    """Prepare number to guess, with length of NUM_LEN"""
    #Make a list and shuffle it
    acceptableNumbers = list(CHARACTERS)
    random.shuffle(acceptableNumbers)

    #Make a secretNum
    preparedNum = ''
    for i in range(SECRET_LEN):
        preparedNum += str(acceptableNumbers[i])

    return preparedNum

def checkGuess(guess, secretNum):
    """"""
    if guess == secretNum:
        print("Correct guess!")
        return True
    else:
        clues = []
        for i in range(len(secretNum)):
            if guess[i] == secretNum[i]:
                clues.append('Fermi')
            elif guess[i] in secretNum:
                clues.append('Piko')            
        if len(clues) == 0:
            clues.append('Bajgel')

    clues.sort()
    print(clues)



def correctInput(guess):
    """Check correct input"""
    #guess = input('> ')
    validation = set(guess)
    #check = 0
    if validation.issubset(CHARACTERS) and len(guess) == SECRET_LEN:
        #print("<correct input> {}".format(check))
        #check += 1
        return True
    else:
        #print("<wrong input> {}".format(check))
        #check += 1
        return False


if __name__ == '__main__':
    main()