from turtle import Turtle, Screen
from tkinter import messagebox
import random
from collections import deque

screen = Screen()
screen.screensize(800, 800)
screen.setup(800, 800)
screen.listen()

snake_blocks = []

direction = ""

accept_input = True

# moves_queue = deque()

def change_direction_left():
  global accept_input
  if accept_input:
    global direction
    if direction!= "r":
      direction = "l"
      accept_input = False

def change_direction_up():
  global accept_input
  if accept_input:
    global direction
    if direction != "d":
      direction = "u"
      accept_input = False

def change_direction_right():
  global accept_input
  if accept_input:
    global direction
    if direction != "l":
      direction = "r"
    accept_input = False

def change_direction_down():
  global accept_input
  if accept_input:
    global direction
    if direction != "u":
      direction = "d"
      accept_input = False


def move_snake():
  global accept_input
  last_pos = len(snake_blocks) - 1
  snake_blocks.insert(0, snake_blocks[last_pos])
  snake_blocks.pop()
  if direction == "l":
    snake_blocks[0].setpos(snake_blocks[1].xcor() - 20, snake_blocks[1].ycor())
  if direction == "r":
    snake_blocks[0].setpos(snake_blocks[1].xcor() + 20, snake_blocks[1].ycor())
  if direction == "u":
    snake_blocks[0].setpos(snake_blocks[1].xcor(), snake_blocks[1].ycor() + 20)
  if direction == "d":
    snake_blocks[0].setpos(snake_blocks[1].xcor(), snake_blocks[1].ycor() - 20)

  check_status()
  accept_input = True

  screen.ontimer(move_snake, 50)


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