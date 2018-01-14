def factor(n):
   if (n == 0) or (n == 1):
      return 1
   else:
      return n * factor(n-1)

##########

def fibonacci(n):
   print ("Enter Fib : " + str(n))
   if (n == 0):
      return 0
   elif (n == 1):
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)

##########
   
def countChar(text,ch):
   cnt =0

   for c in s:
      if c == ch:
         cnt = cnt +1
   return cnt

##########

n=5
print ("factorial of " + str(n) + " = " + str(factor(n)))

n=8
print ("fibonacci of " + str(n) + " = " + str(fibonacci(n)))

s = "some text"
c = 'e'

print ( "'" + s + "' contains '" + c + "': " + str(countChar(s,c)) + " times")
