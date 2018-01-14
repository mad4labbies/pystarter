def sumArray(array):
   newArray = [[]]
   newArray[0] = array[0]
   
   endArray = len(array) - 1 
   k = 1
   
   while k <= endArray:
      i = 0
      endNewArray = len(newArray) - 1
      #print("k=",k,"endNewArray=",endNewArray)
      while i <= endNewArray:
         
         if array[k][0] == newArray[i][0]:
            #print ("newArray[",i,"][0]  = ", newArray[i][0])
            #print ("   array[",k,"][0]  = ", array[k][0])
            
            newArray[i][1] = newArray[i][1] + array[k][1]
            #print ("newArray[",i,"][1]  = ", newArray[i][1])
            break
         
         elif i == endNewArray:
            newArray.append(array[k])
            
         i +=1         
      k += 1         
         
   return newArray
      
##########

ar = [[211,4]]
print ("Array = ",ar)
print ("newArray = ",sumArray(ar))

ar = [[211,4],[262,3],[211,5],[216,6],[262,8],[211,10],[216,9],[232,5]]
print ("Array = ",ar)
print ("newArray = ",sumArray(ar))

