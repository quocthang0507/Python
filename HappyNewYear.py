from graphics import *

def main():
    win=GraphWin("Happy Lunar New Year")
    win.setBackground("Yellow")
    viTri=Point(100,100)
    loiChuc="Chúc mừng năm mới"
    loiChuc+="\nAn khang thịnh vượng"
    loiChuc+="\nVạn sự như ý"
    loiChuc+="\nTấn tài tấn lộc"
    chucTet=Text(viTri,loiChuc)
    chucTet.setTextColor("red")
    chucTet.draw(win)
    win.getMouse()

main()