from graphics import *

def main():
    win=GraphWin("Shapes",width=300,height=300)
    center=Point(150,150)
    circ=Circle(center,50)
    circ.setFill("red")
    circ.draw(win)
    label=Text(center,"Red Circle")
    label.draw(win)
    rect=Rectangle(Point(30,30),Point(120,100))
    rect.draw(win)
    line=Line(Point(30,30),Point(250,250))
    line.draw(win)
    oval=Oval(Point(130,200),Point(250,280))
    oval.draw(win)
    win.getMouse()
    win.close()

main()