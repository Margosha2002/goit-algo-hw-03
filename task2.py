import turtle
import time

size = 300
n = int(input("Enter Recursion Level: "))


def koch_curve(size: int, n: int):
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size=size / 3, n=n - 1)
        turtle.left(angle=60)
        koch_curve(size=size / 3, n=n - 1)
        turtle.right(angle=120)
        koch_curve(size=size / 3, n=n - 1)
        turtle.left(angle=60)
        koch_curve(size=size / 3, n=n - 1)


def koch_snow(size: int, n: int):
    koch_curve(size=size, n=n)
    turtle.right(angle=120)
    koch_curve(size=size, n=n)
    turtle.right(angle=120)
    koch_curve(size=size, n=n)


koch_snow(size=size, n=n)
time.sleep(100)
