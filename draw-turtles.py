import turtle

def draw_square(some_turtle):
   i = 1
   while (i <= 4):
      some_turtle.forward(100)
      some_turtle.right(90)
      i += 1

def draw_turtles():
   window = turtle.Screen()
   window.bgcolor("red")

   brad = turtle.Turtle()
   brad.shape("turtle")
   brad.color("black")
   brad.speed(2)

   for i in range (1,37):
      draw_square(brad)           
      brad.right(10)
      
   #olaf = turtle.Turtle()
   #olaf.shape("arrow")
   #olaf.color("yellow")
   #olaf.circle(50)
   
   window.exitonclick()

draw_turtles()
