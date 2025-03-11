from graphics import *
def main():
    win=GraphWin("noo",500,500)

    bp=Point(250,250)
    b=Circle(bp,120)
    b.setFill(color_rgb(254, 206, 62))
    b.setOutline(color_rgb(254, 206, 62))
    b.setWidth(5)
    b.draw(win)

    # p12=Point(320,270)
    # c22=Circle(p12,50)
    # c22.setFill(color_rgb(238, 108, 48))
    # c22.setOutline(color_rgb(238, 108, 48))
    # c22.draw(win)

    # p12=Point(180,310)
    # c22=Circle(p12,30)
    # c22.setFill(color_rgb(255, 230, 233))
    # c22.setOutline(color_rgb(255, 230, 233))
    # c22.draw(win)

    p22=Point(200,230)
    c32=Circle(p22,45)
    c32.setFill("white")
    c32.setOutline("white")
    c32.setWidth(3)
    c32.draw(win)

    p22=Point(300,230)
    c32=Circle(p22,45)
    c32.setFill("white")
    c32.setOutline("white")
    c32.setWidth(3)
    c32.draw(win)

    p22=Point(305,225)
    c32=Circle(p22,38)
    c32.setFill("black")
    c32.setOutline("black")
    c32.setWidth(3)
    c32.draw(win)

    p22=Point(205,225)
    c32=Circle(p22,38)
    c32.setFill("black")
    c32.setOutline("black")
    c32.setWidth(3)
    c32.draw(win)

    nn=Line(Point(225,308),Point(280,308))
    nn.setFill("black")
    nn.setWidth(9)
    nn.draw(win)

    
    









    win.getMouse()
main()

