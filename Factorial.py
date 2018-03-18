from graphics import *

def factorial(n):
    x=1
    for i in range(n,1,-1):
        x=x*i
    return x

def main():
    win=GraphWin("Factorial",200,200)
    message=Text(Point(70,25),"Nhập n = ")
    message.draw(win)
    inputText=Entry(Point(135,25),5)
    inputText.setText("10")
    inputText.draw(win)
    button=Text(Point(90,60),"Tính")
    button.draw(win)
    Rectangle(Point(70,45),Point(115,75)).draw(win)
    outputText=Text(Point(40,95),"Kết quả:")
    outputText.draw(win)
    win.getMouse()
    x=factorial(int(inputText.getText()))
    outputText=Text(Point(100,95),x)
    outputText.draw(win)
    win.getMouse()
    win.close()

main()
