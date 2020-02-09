# https://www.geeksforgeeks.org/multithreading-python-set-1/
import threading


def print_cube(num):
    print('Cube: {}'.format(num * num * num))


def print_square(num):
    print('Square: {}'.format(num * num))


if __name__ == "__main__":
    # creating new threads
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting new threads
    t1.start()
    t2.start()

    # wait until threads are completely executed
    t1.join()
    t2.join()

    # both threads completely executed
    print('Done!')
