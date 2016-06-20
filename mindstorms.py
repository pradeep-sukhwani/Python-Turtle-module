import turtle
import Tkinter

def draw_square(brownie):
    for i in range(1,5):
        brownie.forward(200)
        brownie.right(90)

def draw_art():
    playground = turtle.Screen()
    playground.bgcolor("Yellow")
    brownie = turtle.Turtle()
    brownie.shape("arrow")
    brownie.color("Black", "Red")
    brownie.speed(5)
    for i in range(1,37):
        draw_square(brownie)
        brownie.right(10)
    #speedy = turtle.Turtle()
    #speedy.shape("arrow")
    #speedy.color("Black", "Red")
    #speedy.circle(200)
    
    playground.exitonclick()

draw_art()