from graphics import *
def main():
    win=GraphWin("flower",500,500)
    
    te=Text(Point(200,70),"enter a one number from [3,4,5] ")
    te.draw(win)

    ent=Entry(Point(200,100),5)
    ent.draw(win)
    win.getMouse()

    con=ent.getText()
    print(con)


    if con=="5":
      #head
      pp=Point(225,300)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(208, 93, 160))
      p.draw(win)
      
      #2th right
      pp=Point(245,350)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(208, 93, 160))
      p.draw(win)
      
      #2th left
      pp=Point(205,350)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)
      
      #shado left
      pp=Point(197,331)
      p=Circle(pp,22)
      p.setFill(color_rgb(185, 69, 130))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)

      

        #shado right
      pp=Point(252,332)
      p=Circle(pp,22)
      p.setFill(color_rgb(185, 69, 130))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)

      
      #1th left
      pp=Point(200,320)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)
      
      #1th right
      pp=Point(250,320)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(208, 93, 160))
      p.draw(win)

      #center
      pp=Point(225,325)
      p=Circle(pp,20)
      p.setFill("#FDF996")
      p.setOutline("#CFAB0F")#CFAB0F
      p.draw(win)

    elif con=="4":
       
       #2th right
      pp=Point(250,350)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)
      
      #2th left
      pp=Point(200,350)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)

      #shado left
      pp=Point(199,312)
      p=Circle(pp,22)
      p.setFill(color_rgb(185, 69, 130))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)

      

        #shado right
      pp=Point(252,312)
      p=Circle(pp,22)
      p.setFill(color_rgb(185, 69, 130))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)
      
      #1th right
      pp=Point(253,300)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(230, 89, 165))
      p.draw(win)
      
      #1th left
      pp=Point(197,300)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)
      
      

      #center
      pp=Point(225,325)
      p=Circle(pp,20)
      p.setFill("#FDF996")
      p.setOutline("#CFAB0F")#CFAB0F
      p.draw(win)
       
    elif con=="3":
      
      
      #2th right
      pp=Point(245,340)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(208, 93, 160))
      p.draw(win)

      #shado right
      pp=Point(220,347)
      p=Circle(pp,15)
      p.setFill(color_rgb(185, 69, 130))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)

      
      
      #2th left
      pp=Point(205,340)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)
      
      #shado left
      pp=Point(212,312)
      p=Circle(pp,15)
      p.setFill(color_rgb(185, 69, 130))
      p.setOutline(color_rgb(185, 69, 130))
      p.draw(win)

      
      
       #head
      pp=Point(225,300)
      p=Circle(pp,30)
      p.setFill(color_rgb(230, 89, 165))
      p.setOutline(color_rgb(208, 93, 160))
      p.draw(win)

      #center
      pp=Point(225,325)
      p=Circle(pp,17)
      p.setFill("#FDF996")
      p.setOutline("#CFAB0F")#CFAB0F
      p.draw(win)


    else:
       tt=Text(Point(200,325),"not found , there is only 3,4,5")
       tt.draw(win)
       
       
      








    win.getMouse()
    win.close()
main()