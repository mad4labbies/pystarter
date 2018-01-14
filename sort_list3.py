liste = [1,3,5,6,7,9]

def insert(n):
   index = len(liste) - 1
   
   print("length = " + str(len(liste)) + " index[" + str(index) + "] = " + str(liste[index])+" n = "  + str(n))

   if liste[index] <= n:
      liste.append(n)
      return
   else:
      liste.append(liste[index])
   
   while index >= 0:
      print("index[" + str(index) + "] = " + str(liste[index])+" n = "  + str(n))

      if index == 0:
         liste[index+1] = liste[index]
         liste[index] = n
         break
      elif liste[index] > n:
         liste[index+1] = liste[index]
         index = index - 1
      else:
         liste[index+1] = n
         break
      
########################################
      
insert(11)
print(liste)

insert(4)
print(liste)

insert(0)
print(liste)

insert(6)
print(liste)

   
