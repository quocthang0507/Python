from graphics import *

def main():
    win=GraphWin("Click'n type",400,400)
    message=Text(Point(200,10),"Test your keyboard")
    message.draw(win)
    while True:
        pt=win.getMouse()
        key=win.getKey()
        label=Text(pt,key)
        label.draw(win)

main()
