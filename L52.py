#theauthorsaremaggiedunnandcodybrownL52
import turtle
dan = turtle.Turtle()
dan.width(5)
dan.speed(0)

mood = input("What is your mood? \n")

def draw_star(color):
    for side in range(6):
        dan.forward(100)
        dan.right(144)
        dan.color(color)

if mood == "happy":
    color = "yellow"
elif mood == "sad":
    color = "blue"
elif mood == "sleepy":
    color = "grey"
elif mood == "angry":
    color = "red"

draw_star(color)
