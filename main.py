import turtle
import time
import threading
import asyncio
from playsound import playsound
from grid import main as gridMain

wn = turtle.Screen()

async def asyncShapeShift(t, screen):
    screen.addshape('./1n.gif')
    screen.addshape('./2n.gif')
    screen.addshape('./3n.gif')
    screen.addshape('./4n.gif')
    shapes = ('./1n.gif', './2n.gif', './3n.gif', './4n.gif')
    while True:
        for shape in shapes:
            await asyncio.sleep(0.05)
            t.shape(shape)

async def move(pacman):
    return
    while True:
        await asyncio.sleep(0.25)
        fw = lambda: pacman.forward(25)
        for _ in range(4): fw()

        

# Asyncio main loop to allow for async tasks to be created
async def main():
    gridMain(wn) # Draw the grid

    pacman = turtle.Turtle() # Create pacman object

    # Create tasks/threads
    soundThread = threading.Thread(target=lambda: playsound('./theme.mp3'), daemon=True) # Thread for sound (so it can run independently of turtle)
    shapeShiftTask = asyncio.create_task(asyncShapeShift(pacman, wn)) # async task to allow the turtle to open and close its mouth
    moveTask = asyncio.create_task(move(pacman))

    # soundThread.start()

    # config pacman
    pacman.speed(0)
    pacman.penup()
    pacman.fillcolor("yellow")
    pacman.pencolor("yellow")
    pacman.goto(-25, -25)

    wn.screensize(750, 750, 'black')

    # start async tasks
    await shapeShiftTask
    await moveTask

    wn.mainloop()
#teleport
'''
if pacman coordinates equal teleportation dot
    pacman goto coordinates of first teleport dot
'''
if __name__ == '__main__': asyncio.run(main()) # Run main turtle loop
