import random

secret = 'secret'
guess = ''
score = 0
wheel = [0, 100, 200, 300, 400, 500, 600,
         700, 800, 900, 1000, -100, -300, -500]
turns = 5


def welcome():
    name = input('What is your name? ')
    print('Hello {}, Now we start the game!'.format(name))


def spin():
    pos = random.randint(0, 13)
    return wheel[pos]


def showAnswer():
    printChars = ''
    for char in secret:
        if char in guess:
            printChars += char
        else:
            printChars += '_'
        printChars += ' '
    print(printChars)


def hasWon():
    for char in secret:
        if char not in guess:
            return False
    return True


def main():
    global turns, guess, score
    while turns > 0:
        t = input('\nPress Enter key to spin the wheel of fortune ')
        if t == "":
            turned = spin()
            print('You have just turned into {}'.format(turned))
            char = input(
                'You have {} turns. Try to guess a character: '.format(turns))
            if char in guess:
                turns -= 1
                showAnswer()
            else:
                guess += char
                if char in secret:
                    score += turned
                    showAnswer()
                    print('Correct! You have got {}. Your score is {}'.format(
                        turned, score))
                else:
                    print('Wrong! You don\'t get {}. Your score is {}'.format(
                        turned, score))
                    turns -= 1
                    showAnswer()
            if hasWon():
                print('Congrats! You won the game, your score is {}'.format(score))
            if turns == 0:
                print('You lose! The secret word is \'{}\''.format(secret))
        else:
            print('You don\'t spin the wheel, so the game is terminating...')
            break


if __name__ == '__main__':
    welcome()
    main()
