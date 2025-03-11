from graphics import *
def main():
    win=GraphWin("flags",500,500)

    te=Text(Point(200,50),"choose one of the following country to show it's flag :\n [palestine , egypt or japanese]")
    te.draw(win)

    ent=Entry(Point(200,100),20)
    ent.draw(win)
    win.getMouse()

    con=ent.getText()
    print(con)


    #palestine flag
    if con=="palestine" or con=='Palestine':
        p_Rec1 = Rectangle(Point(100,240), Point(350,290))
        p_Rec1.setFill("black")
        p_Rec1.setOutline("black")
        p_Rec1.draw(win)

        p_Rec2 = Rectangle(Point(100,280), Point(350,330))
        p_Rec2.setFill("white")
        p_Rec2.setOutline("white")
        p_Rec2.draw(win)

        p_Rec3 = Rectangle(Point(100,320), Point(350,370))
        p_Rec3.setFill("green")
        p_Rec3.setOutline("green")
        p_Rec3.draw(win)

        tra=Polygon(Point(100,240), Point(100,370),Point(190,300))
        tra.setFill("red")
        tra.setOutline("red")
        tra.draw(win)
        
 

    #egypt flag
    elif con=="egypt" or con=='Egypt':
        e_Rec1 = Rectangle(Point(100,240), Point(350,290))
        e_Rec1.setFill("red")
        e_Rec1.setOutline("red")
        e_Rec1.draw(win)

        e_Rec2 = Rectangle(Point(100,280), Point(350,330))
        e_Rec2.setFill("white")
        e_Rec2.setOutline("white")
        e_Rec2.draw(win)

        e_Rec3 = Rectangle(Point(100,320), Point(350,370))
        e_Rec3.setFill("black")
        e_Rec3.setOutline("black")
        e_Rec3.draw(win)
    
#....................................................................
  

    #japanese flag
    elif con=="japanese" or con=='Japanese':
        j_Rec1 = Rectangle(Point(100,240), Point(350,370))
        j_Rec1.setFill("white")
        # e_Rec1.setOutline("white")
        j_Rec1.draw(win)

        c1=Point(225,305)
        cc1=Circle(c1,40)
        cc1.setFill("red")
        cc1.setOutline("red")
        cc1.draw(win)


    else:
        ell=Text(Point(150,240),"enter one of the followin three flags only \n egypt \n palestine \n japanese")
        ell.draw(win)




    win.getMouse()
    win.close()
main()