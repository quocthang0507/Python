def main(n):
    epsilon=0.0000001
    x=10
    while True:
        print (x)
        y=(x+n/x)/2
        if abs(y-x)<epsilon:
            break
        x=y
    return print(y)

main(8)