import random


def main():
    min = 1  # The minimum value of random
    max = 99    # The maximum value of random
    times = 5   # Number of turns
    i = 0   # Current number of turns
    secret = random.randint(min, max)   # Generate random number
    n = 0   # The number user guessed
    print('You have {} turns to guess the secret number'.format(5))
    while i < times and n != secret:
        i += 1
        n = int(input("Enter a integer from {} to {}: ".format(min, max)))
        if n < secret:
            print('The value must be greater')
        elif n > secret:
            print('The value must be less')
        else:
            print('You guessed it. Congrats!')
        if i == times:
            print('You lose! The secret number was {}'.format(secret))


if __name__ == '__main__':
    main()
