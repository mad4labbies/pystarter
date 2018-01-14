#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

def greet(name):
   """Greets the person passed as argument"""
   print("Hello," + name + ".")
   pi = 3.14
   print("Pi = ", str(pi))

# Gather our code in a main() function
def main():
    print ('Hello there', sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
   main()
   name = input("What's your name: ")
   greet(name)
