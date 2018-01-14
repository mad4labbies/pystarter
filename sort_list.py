list = [1,3,5,6,7,9]

def insert(n):
   print("last "+ str(list[-1]))
   if list[-1] == n:
      print(str(list[-1]) + " == " + str(n))
      return
   elif list[-1] < n:
      print(str(list[-1]) + " < " + str(n))
      list.append(n)
      return
   else:
      print("insert = "  + str(n))
      list.append(n)
      list.sort()

insert(11)
print(list)

   
