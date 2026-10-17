"""A dependency-free birthday cake, redrawn from the supplied Turtle screenshots."""
import math
import random
import turtle as t

BG = "#101826"
COLORS = ["#ef476f", "#ffd166", "#77d6b3", "#69b7dd", "#f4f6f8"]

screen = t.Screen()
screen.setup(900, 760)
screen.bgcolor(BG)
screen.title("Happy Birthday")
screen.tracer(False)
t.hideturtle()
t.speed(0)

def ellipse(cx, cy, rx, ry, color):
    t.penup(); t.goto(cx + rx, cy); t.pendown(); t.color(color); t.begin_fill()
    for degree in range(361):
        angle = math.radians(degree)
        t.goto(cx + rx * math.cos(angle), cy + ry * math.sin(angle))
    t.end_fill()

def rectangle(x, y, width, height, color):
    t.penup(); t.goto(x, y); t.setheading(0); t.color(color); t.begin_fill(); t.pendown()
    for side in (width, height, width, height):
        t.forward(side); t.left(90)
    t.end_fill()

def layer(cx, top, rx, ry, height, side, icing):
    rectangle(cx-rx, top-height, rx*2, height, side)
    ellipse(cx, top-height, rx, ry, side)
    ellipse(cx, top, rx, ry, icing)

# Plate and cake tiers
ellipse(0, -230, 190, 36, "#a9c5d8")
ellipse(0, -215, 190, 36, "#eff6f8")
layer(0, -115, 155, 48, 105, "#73c5dc", "#ffffff")
layer(0, 10, 85, 30, 92, "#e84545", "#ff9c6b")

# Sprinkles
random.seed(12)
for _ in range(90):
    x=random.randint(-135,135); y=random.randint(-195,-95)
    if (x/150)**2 + ((y+145)/55)**2 < 1.2:
        t.penup(); t.goto(x,y); t.dot(random.randint(3,6), random.choice(COLORS))

# Candles, stripes, flames
for x in (-48,-16,16,48):
    rectangle(x-5, 15, 10, 70, "#f4f6f8")
    t.color("#69b7dd"); t.pensize(3)
    for y in range(22,82,15):
        t.penup(); t.goto(x-5,y); t.pendown(); t.goto(x+5,y+8)
    t.penup(); t.goto(x,86); t.dot(14,"#ffd166"); t.dot(6,"#ff9c6b")

# Confetti around the cake
for _ in range(100):
    x=random.randint(-400,400); y=random.randint(-250,310)
    if abs(x)>210 or y>120:
        t.penup(); t.goto(x,y); t.dot(random.randint(3,7),random.choice(COLORS))

t.penup(); t.goto(0,255); t.color("white")
t.write("Happy Birthday", align="center", font=("Arial", 42, "bold"))
t.penup(); t.goto(0,210); t.color("#ffd166")
t.write("May every wish come true", align="center", font=("Arial", 18, "normal"))
screen.update()
t.done()
