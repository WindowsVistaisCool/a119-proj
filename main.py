import turtle
import time
import threading
from playsound import playsound

class PathRunner:
    def __init__(self, t, instructions: list = None):
        self.turtle = t
        self.instructions = instructions
        self.TILE_WIDTH = 50

    def runPath(self, instructions: list, delay = None, func = None, directionFunc = None):
        self.instructions = instructions
        self.run(delay, func, directionFunc)

    def run(self, delay=None, func = None, directionFunc = None):
        directionParser = {
            'u': lambda t: t.setheading(90),
            'd': lambda t: t.setheading(270),
            'l': lambda t: t.setheading(180),
            'r': lambda t: t.setheading(0),
        }
        for instruction in self.instructions:
            direction, distance = list(instruction)
            oldSpeed = self.turtle.speed()
            self.turtle.speed(0)
            directionParser[direction](self.turtle)
            if directionFunc: directionFunc(direction)
            self.turtle.speed(oldSpeed)
            self.turtle.forward(self.TILE_WIDTH * int(distance))
            if delay: time.sleep(delay)
            if func: func()

class PacmanGrid:
    def __init__(self, screen: turtle.Screen, manual = False) -> None:
        self.screen = screen
        self.drawer = turtle.Turtle()

        self.drawer.speed(0)
        self.drawer.pensize(3)
        self.drawer.pencolor('blue')
        self.drawer.hideturtle()

        if manual: return

        self._drawBorder()
        self._drawBarriers()
        self._drawDots()
    
    def goto(self, x: int, y: int):
        self.drawer.penup()
        self.drawer.goto(x, y)
        self.drawer.pendown()

    def _drawBorder(self):
        self.goto(325, 0) # initial position
        top = [
            # top of right teleport block
            'l3',
            'u1',
            'r2',
            # top right corner straights
            'u4',
            'l5',
            # top dip
            'd2',
            'l1',
            'u2',
            # top left corner straights
            'l5',
            'd4',
            # top of left teleport block
            'r2',
            'd1',
            'l3'
        ]
        bottom = [
            # bottom of left teleport block
            'r3',
            'd1',
            'l2',
            # bottom left corner straights
            'd3',
            'r4',
            # bottom intrusion
            'u1',
            'r1',
            'u1',
            'r1',
            'd1',
            'r1',
            'd1',
            # bottom right corner straights
            'r4',
            'u3',
            # bottom of right teleport block
            'l2',
            'u1',
            'r3'
        ]

        pathRunner = PathRunner(self.drawer) # create a path interpreter
        xcor = self.drawer.xcor
        ycor = self.drawer.ycor
        pathRunner.runPath(top) # draw the top of the grid
        self.goto(xcor(), ycor() - 50) # move down to create an empty space
        pathRunner.runPath(bottom) # draw the bottom of the grid
        
    def _drawBarriers(self):
        shape_t = [
            'r3',
            'd1',
            'l1',
            'd1',
            'l1',
            'u1',
            'l1',
            'u1'
        ]
        shape_block = [
            'r2',
            'd1',
            'l2',
            'u1'
        ]
        shape_l = [
            'r1',
            'd1',
            'r1',
            'd1',
            'l2',
            'u2'
        ]
        shape_l_inverted = list(map(
            lambda item: ''.join( # swap l and r
                [
                    ('r' if list(item)[0] == 'l' else 'l'), # swap first char
                    ''.join(list(item)[1:]) # append everything else into one string
                ]
            ) if list(item)[0] in ['l', 'r'] else item, # only swap if the first char is l or r
            shape_l))
        shapeLocations = {
            (-225, 200): shape_t,
            (-75, 100): shape_t,
            (75, 200): shape_t,
            (-125, 0): shape_l,
            (125, 0): shape_l_inverted,
            (-225, -150): shape_block,
            (125, -150): shape_block,
        }
        pathRunner = PathRunner(self.drawer) # create a path interpreter
        for location, shape in shapeLocations.items(): # loop through all the shapes
            self.goto(*location) # unpack coords and pass into function
            pathRunner.runPath(shape) # create the shape on the screen

    def _drawDots(self, reset = False):
        self.drawer.pencolor('orange' if not reset else 'black')
        # a list of coordinates of dots where they SHOULDNT be drawn
        skipDots = [
            (6,),
            (2, 3, 4, 6, 8, 9, 10),
            (3, 9),
            (5, 6, 7),
            (1, 2, 6, 10, 11),
            (4, 8),
            (1, 2, 4, 5, 7, 8, 10, 11),
            None,
            (2, 3, 6, 9, 10),
            (5, 6, 7)
        ]
        for i, row in enumerate(skipDots):
            for col in range(11):
                if row is not None and (col + 1) in row:
                    continue
                self.goto(-250 + (col * 50), 225 - (i * 50))
                self.drawer.dot(5)
        self.drawer.pencolor('black')

    def eatDot(self, x, y):
        self.goto(x, y)
        self.drawer.dot(5)

wn = turtle.Screen()

def changeCameraCenter(screen, y):
    screen.getcanvas().yview_moveto(y)
    screen.update()

wn.screensize(750, 2000, 'black') # Initialize screen pararmeters
playfunnySound = lambda: threading.Thread(target=playsound('./funny.mp3')).start()

# Draw the title
titleDrawer = turtle.Turtle(visible=False)
titleDrawer.pencolor('white')
titleDrawer.speed(0)
titleDrawer.penup()
titleDrawer.goto(-225, 800)
titleDrawer.write('Pacman! (The Animation)', font=('Calibri', 34, 'bold'))
titleDrawer.rt(90)
titleDrawer.fd(100)
# Loading text to display while grid is drawing
titleDrawer.write('Now Loading...', font=('Calibri', 16, 'italic'))
titleDrawer.lt(90)
titleDrawer.pensize(100)

changeCameraCenter(wn, -1) # Focus camera to top of screen

def drawTitleText(text, formatting = 'normal'):
    titleDrawer.pencolor('black')
    titleDrawer.pendown()
    titleDrawer.fd(750)
    titleDrawer.back(750)
    titleDrawer.pencolor('white')
    titleDrawer.write(text, font=('Calibri', 16, formatting))

def resetAnimation():
    wn.onkey(lambda: None, 'space') # de-register keyevent
    drawTitleText('Clearing old pacman food...', 'italic')
    grid._drawDots(True) # make all of them black again
    drawTitleText('Placing new pacman food...', 'italic')
    grid._drawDots()
    drawTitleText('Press SPACE to begin!', 'italic')
    playfunnySound()
    wn.onkey(startAnimation, key='space') # register key event on space after ready
    wn.listen()

grid = PacmanGrid(wn, manual = True) # Draw the grid in the background while the user is focused on title
drawTitleText('Drawing borders...', 'italic')
grid._drawBorder()
playfunnySound()
drawTitleText('Drawing objects...', 'italic')
grid._drawBarriers()
playfunnySound()
drawTitleText('Drawing pacman food...', 'italic')
grid._drawDots()

drawTitleText('Press SPACE to begin!', 'italic')
playfunnySound()

playGameTrack = lambda: threading.Thread(
    target=lambda: playsound('./theme.mp3'), # callable to start the sound
    daemon=True # daemon to make sure the sound stops when the turtle window is closed
).start() # Thread for sound (so it can run independently of turtle)

wn.addshape('./1n.gif')
wn.addshape('./2n.gif')
wn.addshape('./3n.gif')
wn.addshape('./4n.gif')

shapeMap = {
    'r': lambda: pacman.shape('./1n.gif'),
    'd': lambda: pacman.shape('./2n.gif'),
    'l': lambda: pacman.shape('./3n.gif'),
    'u': lambda: pacman.shape('./4n.gif')
}

pacman = turtle.Turtle(shape='./1n.gif') # Create pacman object
pacman.penup()
pacman.speed(1)

def startAnimation():
    drawTitleText('Teleporting pacman...', 'italic')
    wn.onkey(lambda: None, 'space') # de-register keyevent
    if pacman.xcor() != 0:
        print("hey")
        pacman.goto(0, 0) # useful after first run to sync music with movement
    playGameTrack() # Start the audio track
    pacman.goto(-300, -25) # move to starting posistion on grid
    changeCameraCenter(wn, 0.375) # move camera back to center
    time.sleep(0.75) # wait for audio to start playing

    lastDirection = 'l'
    def directionFunc(direction): # function that runs each step of the path
        nonlocal lastDirection
        if direction != lastDirection: shapeMap[direction]() # change pacman's shape to face the correct direction
        lastDirection = direction
    pathRunner = PathRunner(pacman)
    pathRunner.runPath(
        ['r1', 'r1', 'r1', 'd1', 'd1', 'l1', 'l1', 'd1', 'd1', 'r1', 'r1', 'r1', 'u1', 'u1', 'r1', 'r1', 'u1', 'u1', 'l1', 'u1', 'l1', 'u1', 'l1', 'l1', 'l1', 'u1', 'u1', 'u1', 'r1', 'r1', 'r1', 'r1', 'd1', 'd1', 'r1', 'r1', 'r1', 'd1', 'r1', 'd1', 'd1', 'r1', 'r1', 'r4'],
        delay=0.19,
        func=lambda: grid.eatDot(pacman.xcor(), pacman.ycor()), # eat the dot at the current location
        directionFunc=directionFunc
    )
    drawTitleText('Thanks for watching! Press SPACE to replay!', 'italic')
    changeCameraCenter(wn, -1)
    wn.onkey(resetAnimation, key='space')
    wn.listen()

wn.onkey(startAnimation, key='space') # register key event on space
wn.listen() # focus TurtleScreen so that the keyevent can be listened to

wn.mainloop() # run the main loop to keep the screen window active
