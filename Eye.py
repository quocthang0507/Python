from graphics import *

def main():
    win=GraphWin("Eyes")
    leftEye=Circle(Point(80,50),5)
    leftEye.setFill("yellow")
    leftEye.setOutline("red")
    leftEye.draw(win)

    # rightEye=Circle(Point(100,50),5)
    # rightEye.setFill("yellow")
    # rightEye.setOutline("red")
    # rightEye.draw(win)

    rightEye=leftEye.clone()
    rightEye.move(20,0)
    rightEye.draw(win)

    win.getMouse()
    win.close()

main()