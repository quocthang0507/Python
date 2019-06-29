import time  # importing the time module

word = 'secret'  # here we set the secret
guesses = ''    # creates an variable with an empty value
turns = 10    # determine the number of turns


def welcome():
    name = input('What is your name? ')  # welcoming the user
    print('Hello, {}. Time to play hangman!\n'.format(name))


def loadGame():
    time.sleep(1)   # wair for 1 second
    print('Start guessing...')
    time.sleep(1)


def showChars():
    printChars = ''
    for char in word:
        if char in guesses:
            printChars += char
        else:
            printChars += '_'
        printChars += ' '
    print(printChars)


def hasWon():
    for char in word:
        if char not in guesses:
            return False
    return True


def main():
    global turns, guesses
    while turns > 0:
        char = input(
            'You have {} turns. Try to guess a character: '.format(turns))
        if char in guesses:
            turns -= 1
            showChars()
        else:
            guesses += char
            if char in word:
                showChars()
            else:
                print('Wrong!')
                turns -= 1
                showChars()
        if hasWon():
            print('You won!')
            break
        if turns == 0:
            print('You lose! The secret word is \'{}\''.format(word))


if __name__ == '__main__':
    welcome()
    loadGame()
    main()
