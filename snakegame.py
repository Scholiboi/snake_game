import time  # new
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# input()
screen = Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(llx=-300, lly=-300, urx=300, ury=300)
screen.tracer(False)  # new
screen.bgcolor("black")
screen.title("Snake Game")

# t1 = Turtle()
# t2 = Turtle()
# t3 = Turtle()
# turtles = [t1, t2, t3]
# x_coords = 0
# for tutel in turtles:
#     tutel.shape("square")
#     tutel.color("white")
#     tutel.teleport(x=x_coords,y=0)
#     x_coords -= 20

game_is_on = True
snake_head = Snake()
food_head = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake_head.up, "w")
screen.onkey(snake_head.down, "s")
screen.onkey(snake_head.left, "a")
screen.onkey(snake_head.right, "d")

while game_is_on:
    screen.update()  # new
    time.sleep(0.1)

    snake_head.move()

    if snake_head.head.distance(food_head) < 15:
        food_head.new_food()
        score.increase_score()
        score.update_score()
        snake_head.extendseg()

    if (snake_head.head.xcor() > 300 or snake_head.head.xcor() < -300 or snake_head.head.ycor() > 300 or
            snake_head.head.ycor() < -300):
        snake_head.restartgame()
        score.restart()

    for seg in snake_head.seg[2:]:
        if snake_head.head.distance(seg) <= 10:
            snake_head.move()
            snake_head.restartgame()
            score.restart()


screen.exitonclick()
