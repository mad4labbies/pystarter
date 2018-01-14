import random

while True:
   choice = input("Press enter to draw a number ")
   number = random.randint(1,20)
   print("You got ", number)
   choice = input("Do you want to play again? (y/n)")

   if choice=='n':
      break
