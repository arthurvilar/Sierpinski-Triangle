import turtle
import random  
from random import uniform

# initial turtle configurations
tommy = turtle.Turtle()
tommy.color("black")
tommy.speed(5000)
tommy.pensize(0.1)
tommy.penup()

initial_points = [(0, 0), (400, 0), (200, 346)]

# draw 3 initial points
for points in initial_points:
  tommy.goto(points)
  tommy.dot()

# first iteration uses a randon distance
main_point = random.choice(initial_points)
last_point = random.choice(initial_points)

while last_point == main_point:
  last_point = random.choice(initial_points)

u = random.uniform(0, 1)
posX = ((1 - u)*main_point[0]) + (u*last_point[0])
posY = ((1 - u)*main_point[1]) + (u*last_point[1])

tommy.goto((posX, posY))
tommy.dot()

# the other iterations use half the distance of the last point to the main point
for i in range(25000):
  main_point = random.choice(initial_points)
  
  posX = 0.5 * (main_point[0] + last_point[0])
  posY = 0.5 * (main_point[1] + last_point[1])
  
  last_point = (posX, posY)

  tommy.goto(last_point)
  tommy.dot()
  
tommy.goto(500,500)