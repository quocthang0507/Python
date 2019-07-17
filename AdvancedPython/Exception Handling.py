def func1():
    try:
        file = open("data.txt", "w")
        file.write("Write this line into file")
    except IOError:
        print("Error: Can't find the file")
    else:
        print('OK')
        file.close()


def func2():
    try:
        file = open("data.txt", "w")
        try:
            file.write("...")
        finally:
            print('Closing file')
            file.close()
    except IOError:
        print('Error')


def func3():
    try:
        a = 10
        print(a)
        raise NameError('Hello')
    except NameError as e:
        print('Exception occurs')
        print(e)


if __name__ == "__main__":
    func3()
