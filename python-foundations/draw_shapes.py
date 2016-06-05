import turtle

def drawing_turtles():
    window = turtle.Screen()
    window.bgcolor('purple')

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()

def draw_square():
    toby = turtle.Turtle()
    toby.shape('turtle')
    toby.color('white')
    for i in range(4):
        toby.forward(100)
        toby.right(90)

def draw_circle():
    betsy = turtle.Turtle()
    betsy.shape('circle')
    betsy.color('pink')
    betsy.circle(100)

def draw_triangle():
    ella = turtle.Turtle()
    ella.shape('triangle')
    ella.color('green')
    for i in range(3):
        ella.right(120)
        ella.forward(100)

drawing_turtles()
