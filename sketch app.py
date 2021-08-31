from turtle import Turtle, Screen
import turtle

tim = Turtle()

screen = Screen()

#move_forward will move the turtle forward by some steps in this case by 10 steps. 
def move_forward():
    tim.forward(10)

#move_right will move the turtle in right direction by some angle in this case by 10 degree. 
def turn_right():
    tim.right(10)

#move_left will move the turtle in left direction by some angle in this case by 10 degree. 
def turn_left():
    tim.left(10)

#move_backward will move the turtle backward by some steps in this case by 10 steps. 
def move_backward():
    tim.backward(10)

# 
def clear():
    tim.reset()
    

screen.listen()
screen.onkeypress(fun=move_forward,key="w")
screen.onkeypress(fun=turn_right,key="d")
screen.onkeypress(fun=turn_left,key="a")
screen.onkeypress(fun=move_backward,key="s")
screen.onkeypress(fun=clear,key="c")

screen.exitonclick()
