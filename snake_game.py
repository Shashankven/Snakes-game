# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

from tkinter import *
import random

game_width=700
game_height=700
speed=50 #how often speed updates
space_size=50
body_parts=16
snake_color="#00FF00"
food_color="#FF0000"
background_color="#000000"

class Snake:
  def __init__(self):
    self.body_size=body_parts
    self.coordinates=[]
    self.squares=[]

    for i in range(0,body_parts):
      self.coordinates.append([0,0])

    for x,y in self.coordinates:
      square=canvas.create_rectangle(x,y,x+space_size,y+space_size, fill=snake_color, tag="snake")
      self.squares.append(square)

class Food:
  def __init__(self):
    x=random.randint(0,(game_width//space_size)-1)*space_size 
    y=random.randint(0,(game_height//space_size)-1)*space_size

    self.coordinates = [x,y]

    canvas.create_oval(x,y,x+space_size,y+space_size,fill=food_color,tag="food")
    
def Next_turn(snake, food):
  x,y=snake.coordinates[0] #head of snake
  if direction=='up':
    y-=space_size
  elif direction=='down':
    y+=space_size
  elif direction=='left':
    x-=space_size
  elif direction=='right':
    x+=space_size

  snake.coordinates.insert(0,(x,y))
  square=canvas.create_rectangle(x,y,x+space_size,y+space_size, fill=snake_color)

  snake.squares.insert(0, square)

  if x==food.coordinates[0] and y==food.coordinates[1]:
    global score
    score+=1
    label.config(text="Score:{}".format(score))
    canvas.delete("food")
    food=Food()

  else:
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
  
  if Check_collisions(snake):
    Game_over()
    return

  window.after(speed,Next_turn,snake,food )


def Change_direction(new_direction):
  global direction

  if new_direction=='left':
    if direction != 'right':
      direction=new_direction
  elif new_direction=='right':
    if direction != 'left':
      direction=new_direction
  elif new_direction=='up':
    if direction != 'down':
      direction=new_direction
  elif new_direction=='down':
    if direction != 'up':
      direction=new_direction

def Check_collisions(snake):
  x,y=snake.coordinates[0]
  if x<0 or x>=game_width or y<0 or y>=game_height:
    print("Game over")
    return True
  for body_part in snake.coordinates[1:]:
    if x==body_part[0] and y==body_part[1]:
      print("Game Over")
      return True
  return False

def Game_over():
  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2, font=('consolas',70),text="GAME OVER",fill="red",tag="gameover")


window=Tk()
window.title('Snek Game')
window.resizable(False,False)

score=0
direction='down'

label=Label(window, text="Score:{}".format(score),font=('consolas',40))
label.pack()

canvas=Canvas(window,bg=background_color, height=game_height, width=game_width)
canvas.pack()

window.bind('<Left>', lambda event: Change_direction('left'))
window.bind('<Right>', lambda event: Change_direction('right'))
window.bind('<Up>', lambda event: Change_direction('up'))
window.bind('<Down>', lambda event: Change_direction('down'))

snake=Snake()
food=Food()

Next_turn(snake,food)

window.mainloop()