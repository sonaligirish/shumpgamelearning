import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.fillcolor("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Main game loop
while True:
    wn.update()

wn.mainloop()