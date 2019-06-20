import time  # importing the time module

word = 'secret'  # here we set the secret
guesses = ''    # creates an variable with an empty value
turns = 10    # determine the number of turns


def welcome():
    name = input('What is your name? ')  # welcoming the user
    print('Hello, '+name+'. Time to play hangman!\n')


def loadgame():
    time.sleep(1)   # wair for 1 second
    print('Start guessing...')
    time.sleep(0.5)


def main():
    global turns, guesses
    # create a while loop
    # check if the turns are more than zero
    while turns > 0:
        failed = 0
        # for every character in secret word
        for char in word:
            # see if the character is in the players guess
            if char in guesses:
                print(char)  # print then out the character
            else:
                print('_')  # if not found, print a dash
                failed += 1  # and increase the failed counter with one
        # if failed is equal to zero
        # print you won
        if failed == 0:
            print('You won!')
            break   # exit the script
        # ask the user o guess a character
        guess = input('Guess a character: ')
        # set the players guess to guesses
        guesses += guess
        # if the guess is not found in the secret word
        if guess not in word:
            # turns counter decreases with 1
            turns -= 1
            # and print wrong
            print('Wrong!')
            # how may turns are left
            print('You have {} more guesses'.format(turns))
            # if the turns are equal to zero
            if turns == 0:
                # print You lose
                print('You lose!')


if __name__ == '__main__':
    welcome()
    loadgame()
    main()
