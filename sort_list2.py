liste = [1,3,5,6,7,9]

def insert(n):
   j = len(liste)
   last = len(liste) - 1
   
   i = last - 1

   while j >= 0:
      if liste[last] == n:
         break
      elif liste[last] < n:
        liste.append(n)
        break
      elif liste[i] > n:
         print("last = " + str(last) + " i = " + str(i) + "insert = "  + str(n))
         liste[last] = liste[i]
         liste[i] = n
         i = i-1
         last = i - 1
         j = j - 1
         break

insert(8)
print(liste)


   
