from turtle import Screen
from HungrySnake import Snake
from Rat import Food
import time

screen = Screen()
screen.setup (width=600 , height=600)
screen.bgcolor("black")
screen.title("Hungry Snake")
screen.tracer(0)


snake = Snake()
Rat   = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(Rat)<15:
      Rat.refresh()













screen.exitonclick()
