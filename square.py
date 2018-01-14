import math

answer = "yY"

while True:
      num=int(input("Enter a number: "))
      print ("Square root of" , num , " == " ,(math.sqrt(num)))

      choice = ( input("Exit y/n?"))
      if choice in answer:
         break
