import turtle

def main(wn: turtle.Screen):
    gridDrawer = turtle.Turtle()

    wn.screensize(500, 550, "black")

    gridDrawer.pencolor("gray")
    gridDrawer.width(1)
    gridDrawer.speed(100)

    # draw grid lines
    # latgridy = 250

    # for x in range(12):
    #     gridDrawer.penup()
    #     gridDrawer.goto(-250,latgridy)
    #     gridDrawer.pendown()
    #     gridDrawer.goto(250,latgridy)
    #     latgridy = latgridy - 50

    # longridx = -250

    # for x in range(11):
    #     gridDrawer.penup()
    #     gridDrawer.goto(longridx,250)
    #     gridDrawer.pendown()
    #     gridDrawer.goto(longridx,-300)
    #     longridx = longridx + 50

    # draw border
    gridDrawer.pencolor("blue")
    gridDrawer.width(3)
    gridDrawer.penup()
    gridDrawer.goto(-250,250)
    gridDrawer.pendown()
    gridDrawer.goto(250,250)
    gridDrawer.goto(250,-300)
    gridDrawer.goto(-250,-300)
    gridDrawer.goto(-250,-50)
    gridDrawer.penup()
    gridDrawer.goto(-250, 50)
    gridDrawer.pendown()
    gridDrawer.goto(-250, 250)

    # draw top barriers
    gridDrawer.penup()
    gridDrawer.goto(-200,200)
    gridDrawer.pendown()
    gridDrawer.goto(-100,200)
    gridDrawer.goto(-100,150)
    gridDrawer.goto(-200,150)
    gridDrawer.goto(-200,200)

    gridDrawer.penup()
    gridDrawer.goto(-50,200)
    gridDrawer.pendown()
    gridDrawer.goto(50,200)
    gridDrawer.goto(50,150)
    gridDrawer.goto(-50,150)
    gridDrawer.goto(-50,200)

    gridDrawer.penup()
    gridDrawer.goto(100,200)
    gridDrawer.pendown()
    gridDrawer.goto(200,200)
    gridDrawer.goto(200,150)
    gridDrawer.goto(100,150)
    gridDrawer.goto(100,200)

    # draw bottom barriers
    gridDrawer.penup()
    gridDrawer.goto(-200,-250)
    gridDrawer.pendown()
    gridDrawer.goto(-100,-250)
    gridDrawer.goto(-100,-200)
    gridDrawer.goto(-200,-200)
    gridDrawer.goto(-200,-250)

    gridDrawer.penup()
    gridDrawer.goto(-50,-250)
    gridDrawer.pendown()
    gridDrawer.goto(50,-250)
    gridDrawer.goto(50,-200)
    gridDrawer.goto(-50,-200)
    gridDrawer.goto(-50,-250)

    gridDrawer.penup()
    gridDrawer.goto(100,-250)
    gridDrawer.pendown()
    gridDrawer.goto(200,-250)
    gridDrawer.goto(200,-200)
    gridDrawer.goto(100,-200)
    gridDrawer.goto(100,-250)

    # draw left barriers

    gridDrawer.penup()
    gridDrawer.goto(-250,100)
    gridDrawer.pendown()
    gridDrawer.goto(-150,100)
    gridDrawer.goto(-150,0)
    gridDrawer.goto(-250,0)
    gridDrawer.goto(-250,0)

    gridDrawer.penup()
    gridDrawer.goto(-250,-50)
    gridDrawer.pendown()
    gridDrawer.goto(-150,-50)
    gridDrawer.goto(-150,-150)
    gridDrawer.goto(-250,-150)
    gridDrawer.goto(-250,-50)

    # draw left barriers

    gridDrawer.penup()
    gridDrawer.goto(250,100)
    gridDrawer.pendown()
    gridDrawer.goto(150,100)
    gridDrawer.goto(150,0)
    gridDrawer.goto(250,0)
    gridDrawer.goto(250,0)

    gridDrawer.penup()
    gridDrawer.goto(250,-50)
    gridDrawer.pendown()
    gridDrawer.goto(150,-50)
    gridDrawer.goto(150,-150)
    gridDrawer.goto(250,-150)
    gridDrawer.goto(250,-50)

    # draw upper middle barier
    gridDrawer.penup()
    gridDrawer.goto(-100,0)
    gridDrawer.pendown()
    gridDrawer.goto(-100,100)
    gridDrawer.goto(100,100)
    gridDrawer.goto(100,0)
    gridDrawer.goto(50,0)
    gridDrawer.goto(50,50)
    gridDrawer.goto(-50,50)
    gridDrawer.goto(-50,0)
    gridDrawer.goto(-100,0)

    # draw upper middle barier
    gridDrawer.penup()
    gridDrawer.goto(-100,-50)
    gridDrawer.pendown()
    gridDrawer.goto(-100,-150)
    gridDrawer.goto(100,-150)
    gridDrawer.goto(100,-50)
    gridDrawer.goto(50,-50)
    gridDrawer.goto(50,-100)
    gridDrawer.goto(-50,-100)
    gridDrawer.goto(-50,-50)
    gridDrawer.goto(-100,-50)

if __name__ == '__main__':
    wn = turtle.Screen()
    main(wn)
    wn.exitonclick()