from turtle import Turtle, Screen
import turtle

tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def move_backward():
    tim.backward(10)

def clear():
    tim.reset()
    

screen.listen()
screen.onkeypress(fun=move_forward,key="w")
screen.onkeypress(fun=turn_right,key="d")
screen.onkeypress(fun=turn_left,key="a")
screen.onkeypress(fun=move_backward,key="s")
screen.onkeypress(fun=clear,key="c")

screen.exitonclick()