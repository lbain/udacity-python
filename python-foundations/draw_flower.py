import turtle


def draw_flower():
    window = turtle.Screen()
    window.bgcolor('white')

    toby = turtle.Turtle()
    toby.speed(2)
    toby.shape('triangle')

    toby.color('purple')
    for i in range(6):
        toby.begin_fill()
        toby.circle(50)
        toby.end_fill()
        toby.right(60)

    toby.color("yellow")
    toby.right(90)
    toby.forward(20)
    toby.left(90)
    toby.begin_fill()
    toby.circle(20)
    toby.end_fill()

    toby.right(90)
    toby.color('purple')
    toby.forward(80)
    toby.color('green')
    toby.forward(100)

    window.exitonclick()

draw_flower()
