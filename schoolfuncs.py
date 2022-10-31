import typing

# Adds color to the terminal and other QoL funcs
class termFuncs:
    @staticmethod
    def clearColor() -> None: print("\033[0m", end='')

    @staticmethod
    def printError(message: str) -> None: print(f"\033[91m[ERROR] \033[93m{message}\033[0m")

    @staticmethod
    def getInt(prompt: str, errorCallback: callable = lambda: print("Please enter an integer!"), *, loop: bool = True) -> typing.Optional[int]:
        if loop:
            while True:
                try:
                    value = int(input(prompt))
                    break
                except: errorCallback()
            return value
        try:
            value = int(input(prompt))
            return value
        except: errorCallback()

# Functions to make life easier in turtle
class turtleFuncs:
    @staticmethod
    def goto(t, coordinates: (int, int) = (0, 0), *, keepPenUp: bool = False) -> None: # takes in coordinates and moves pen up and down after moving
        t.penup()
        t.goto(coordinates)
        t.pendown()
        if not keepPenUp: t.pendown()

    @staticmethod
    def square(t, length: int = 10) -> None: # draws a simple square
        for _ in range(4):
            t.rt(90)
            t.forward(length)