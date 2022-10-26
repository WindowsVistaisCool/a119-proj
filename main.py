import turtle
import time
import asyncio

wn = turtle.Screen()
wn.addshape('./pacman.gif')
wn.addshape('./turtwig.gif')

#Avatar?
#Border?
#Powerups?
#lives?
#shape of the pacman

#movement process
#find borders and goto function to the other side
#when pacman travels (x) distance, draw dot on xcor - 20

# gridDrawer = turtle.Turtle()
# gridDrawer.fillcolor("blue")
# gridDrawer.pencolor("blue")

pacman = turtle.Turtle(shape='./pacman.gif')

async def flipper():
    wn.addshape('./f1.gif')
    wn.addshape('./f2.gif')
    wn.addshape('./f3.gif')
    wn.addshape('./f4.gif')
    
    while True:
        await asyncio.sleep(0.25)
        

async def move():
    while True:
        await asyncio.sleep(0.05)
        pacman.forward(250)
        pacman.rt(90)

async def main():
    flipperTask = asyncio.create_task(flipper())
    moveTask = asyncio.create_task(move())

    pacman.speed(7)
    pacman.penup()
    pacman.fillcolor("yellow")
    pacman.pencolor("yellow")
    pacman.goto(-125, 125)
    wn.screensize(750, 750, 'black')

    await moveTask
    await flipperTask

    wn.mainloop()

asyncio.run(main())
