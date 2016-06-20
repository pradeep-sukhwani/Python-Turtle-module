import turtle
import Tkinter

def draw_square():
    brownie = turtle.Turtle()
    brownie.color("Red")
    brownie.speed(5)
    brownie.shape("arrow")
    for i in range(1,5):
        brownie.forward(200)
        brownie.right(90)

def draw_circle():
    speedy = turtle.Turtle()
    speedy.color("Black")
    speedy.speed(5)
    speedy.shape("arrow")
    speedy.circle(100)

def draw_triangle():
    flippy = turtle.Turtle()
    flippy.color("Orange")
    flippy.speed(5)
    flippy.shape("arrow")
    for i in range(1,4):
        flippy.forward(300)
        flippy.left(120)

def artibutes():
    playground = turtle.Screen()
    playground.bgcolor("Yellow")
    draw_square()
    draw_circle()
    draw_triangle()
    playground.exitonclick()

artibutes()