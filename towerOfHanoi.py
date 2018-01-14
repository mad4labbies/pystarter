def towerOfHanoi(s, d, e, n, i):
   i += 1
   print ("Iteration: ",i)
   if (n <= 0):
      return
   towerOfHanoi(s,e,d, n-1,i)
   print (str(i)+": Move Disk-",n," From ", s , " TO ", d)
   towerOfHanoi(e,d,s,n-1,i)

#=================

towerOfHanoi('s','d','e',4, 0)
