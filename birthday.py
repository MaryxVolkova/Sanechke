import turtle as t
import random

def makeHeart(size):
    t.forward(size)
    t.circle(size/2, 180)
    t.right(90)
    t.circle(size/2, 180)
    t.forward(size)
    t.left(90)

def HappyBirthdayBestie(size, length, depth):

    if depth == 0:
        return
    HappyBirthdayBestie(size*1.5, length, depth-1)
    counter = 360
    while counter > 0:
        heartColor = (
            random.randint(100, 255), 
            random.randint(100, 255), 
            random.randint(100, 255)
            )
        t.color(heartColor)
        t.fillcolor(heartColor)
        t.begin_fill()
        makeHeart(size)
        t.end_fill()
        t.left(45)
        counter = counter -45

def main():
    t.speed(0)
    t.colormode(255)

    HappyBirthdayBestie(20,0,8)
    t.goto(0, -24)
    t.color("black")
    t.write(
        "You are my best friend!",
        move=False, 
        align="center", 
        font=("Courier New", 32, "bold")
        )
    t.done()

main()
