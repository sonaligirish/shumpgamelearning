from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=0.65, height=0.65, startx=700, starty=0)
sonali = Turtle()
sonali.pen()
for i in range(4):
    sonali.forward(100)
    sonali.left(90)

sonali.reset()
for i in range (8):
    sonali.forward(100)
    sonali.left(225)

for i in range (5):
    print(i)

sonali.reset()
sonali.speed(0)
for i in range(50):
    sonali.circle(i * 3)
    sonali.left(10)

sonali.reset()
sonali.speed(0)
sonali.color("red")
sonali.width(4)
for i in range(20):
    sonali.circle(i*3, 180)
    sonali.right(45)

sonali.reset()
sonali.speed(0)
sonali.color("pink")
sonali.width(5)
for i in range(100):
    sonali.forward(i*2)
    sonali.circle(1*2, 90)
    sonali.right(20)

sonali.reset()
sonali.speed(0)
sonali.color("blue")
sonali.width(6)
for i in range(60):
    sonali.forward(i*3)
    sonali.circle(1*2, 70)
    sonali.left(30)


sonali.reset()
sonali.speed(0)
sonali.color("green")
sonali.width(7)
for i in range(60):
    sonali.circle(i*3)
    sonali.circle(1*2, 30)
    sonali.left(30)


sonali.reset()
sonali.speed(0)
sonali.color("yellow")
sonali.width(4)
for i in range(50):
    sonali.forward(i*3)
    sonali.left(1*2, 30)
    sonali.circle(30)
