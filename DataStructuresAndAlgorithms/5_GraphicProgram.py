import Polymorphism
import turtle
from Polymorphism import *


class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for c in self.items:
            yield c


def main():
    # filename = input("Please enter drawing filename: ")

    filename = 'D:\\OneDrive\\Thang\\HOCTAP\\TU HOC\\Python\\DataStructuresAndAlgorithms\\5_Records.txt'

    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, "r")

    graphicCommands = PyList()

    command = file.readline().strip()

    while command != "":
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)
        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)
        elif command == "endfill":
            cmd = EndFillCommand()
        elif command == "penup":
            cmd = PenUpCommand()
        elif command == "pendown":
            cmd = PenDownCommand()
        else:
            raise RuntimeError("Unknows Command: "+command)
        graphicCommands.append(cmd)
        command = file.readline().strip()
    for cmd in graphicCommands:
        cmd.draw(t)
    file.close()
    t.ht()
    screen.exitonclick()
    print('Program Execution Completed')


if __name__ == "__main__":
    main()
