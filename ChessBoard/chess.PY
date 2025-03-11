from graphics import *
def main():
    win=GraphWin("chess",400,400)
    sq=win.getWidth() //8
    print(sq)

    for r in range(8):
        for c in range(8):
            x1=r*sq
            y1=c*sq
            x2=x1+sq
            y2=y1+sq

            if (r+c)%2==0:
                color="#EEEBCC"

            else:
                color="#9A7D5D"

            square=Rectangle(Point(x1,y1),Point(x2,y2))
            square.setFill(color)
            square.setOutline(color)
            square.draw(win)

    win.getMouse()
    win.close()
main()