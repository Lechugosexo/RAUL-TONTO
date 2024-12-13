import turtle
import time
import random

# Variables básicas
delay = 0.1
score = 0
high_score = 0

# Configurar ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# La serpiente
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# La comida
food = turtle.Turtle()
colors = random.choice(['red', 'blue', 'green'])
shapes = random.choice(['square', 'circle', 'triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# El texto del score
segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score: 0", align="center", font=("Arial", 24, "bold"))

# Funciones del movimiento de la serpiente
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Configurar el control del teclado
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

# Bucle principal del juego
while True:
    wn.update()

    # Colisiones con los límites de la ventana
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.3)
        head.goto(0, 0)
        head.direction = "stop"

        # Reiniciar la serpiente
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])

        # Eliminar los segmentos de la serpiente
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reiniciar la puntuación y el juego
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    # Colisión con la comida
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        score += 10
        if score > high_score:
            high_score = score

        # Actualizar el texto del score
        pen.clear()
        pen.write("Score : {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

        # Crear un nuevo segmento para la serpiente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        # Reducir el delay para hacer el juego más rápido
        delay -= 0.001

    # Mover los segmentos de la serpiente
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Colisión con la propia serpiente
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Reiniciar el juego
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    time.sleep(delay)
