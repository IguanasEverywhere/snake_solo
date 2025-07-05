from turtle import Turtle, Screen
from tkinter import messagebox
import random

screen = Screen()
screen.screensize(800, 800)
screen.setup(800, 800)
screen.listen()

snake_blocks = []

direction = ""

def change_direction_left():
  global direction
  if direction!= "r":
    direction = "l"

def change_direction_up():
  global direction
  if direction != "d":
    direction = "u"

def change_direction_right():
  global direction
  if direction != "l":
    direction = "r"

def change_direction_down():
  global direction
  if direction != "u":
    direction = "d"

def move_snake():
  if direction == "l":
    move_left()
  if direction == "r":
    move_right()
  if direction == "u":
    move_up()
  if direction == "d":
    move_down()
  screen.ontimer(move_snake, 100)


def move_left():
  last_pos = len(snake_blocks) - 1
  snake_blocks.insert(0, snake_blocks[last_pos])
  snake_blocks.pop()
  snake_blocks[0].setpos(snake_blocks[1].xcor() - 20, snake_blocks[1].ycor())
  check_status()


def move_right():
  last_pos = len(snake_blocks) - 1
  snake_blocks.insert(0, snake_blocks[last_pos])
  snake_blocks.pop()
  snake_blocks[0].setpos(snake_blocks[1].xcor() + 20, snake_blocks[1].ycor())
  check_status()

def move_down():
  last_pos = len(snake_blocks) - 1
  snake_blocks.insert(0, snake_blocks[last_pos])
  snake_blocks.pop()
  snake_blocks[0].setpos(snake_blocks[1].xcor(), snake_blocks[1].ycor() - 20)
  check_status()


def move_up():
  last_pos = len(snake_blocks) - 1
  snake_blocks.insert(0, snake_blocks[last_pos])
  snake_blocks.pop()
  snake_blocks[0].setpos(snake_blocks[1].xcor(), snake_blocks[1].ycor() + 20)
  check_status()


def grow_body():
  new_block = Turtle(visible=False)
  new_block.shape("square")
  new_block.shapesize(outline=2)
  new_block.penup()
  new_block.speed(0)
  new_block.setpos(snake_blocks[len(snake_blocks)-1].xcor(), snake_blocks[len(snake_blocks)-1].ycor())
  snake_blocks.append(new_block)
  new_block.color("blue", "green")
  new_block.st()

def game_over(loss_reason):
  screen.bgcolor("red")
  play_again = messagebox.askyesno("Game over!", f"You hit {loss_reason}! Play again?")
  if not play_again:
      screen.bye()
  else:
    pass
    # we'll need to have a way of resetting everything back to initial states here

def check_status():
  if ((snake_blocks[0].xcor() <= -400) or
      (snake_blocks[0].xcor() >= 400) or
      (snake_blocks[0].ycor() <= -400) or
      (snake_blocks[0].ycor() >= 400)):
    game_over("a wall")

  for block in snake_blocks[1:]:
    if block.pos() == snake_blocks[0].pos():
      game_over("yourself")

  if snake_blocks[0].pos() == apple.pos():
    grow_body()
    place_apple()

def place_apple():
  random_x = random.randint(0, 380)
  random_y = random.randint(0, 380)

  while random_x % 20 != 0:
    random_x -= 1
  while random_y % 20 != 0:
    random_y -= 1

  apple.setpos(random_x, random_y)


head = Turtle()
head.shape("square")
head.color("green", "red")
head.shapesize(outline=2)
head.penup()
head.speed(0)


mid = Turtle()
mid.shape("square")
mid.color("blue", "yellow")
mid.shapesize(outline=2)
mid.penup()
mid.setpos(20, 0)
mid.speed(0)


tail = Turtle()
tail.shape("square")
tail.color("blue", "orange")
tail.shapesize(outline=2)
tail.penup()
tail.setpos(40, 0)
tail.speed(0)

apple = Turtle()
apple.shape("square")
apple.color("brown", "brown")
apple.shapesize(outline=2)
apple.penup()
apple.speed(0)
place_apple()

snake_blocks.append(head)
snake_blocks.append(mid)
snake_blocks.append(tail)

screen.onkey(change_direction_left, "a")
screen.onkey(change_direction_up, "w")
screen.onkey(change_direction_right, "d")
screen.onkey(change_direction_down, "s")
screen.onkey(grow_body, "l")

move_snake()

screen.mainloop()