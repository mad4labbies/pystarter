full_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#sub_list=[5,6,7,8]
sub_list=[9,10,12]

def reverse_search_sub(sublist,numbers):
   n_length = len(numbers)
   s_length = len(sublist)

   outer_i = n_length
   
   while outer_i >= 0:
      inner_i = s_length
      num_index = n_length - 1
      sub_index = s_length - 1

      while inner_i >= 0:
        if numbers[num_index] == sublist[sub_index]:
           num_index -= 1
           sub_index -= 1
           inner_i -= 1
        else:
            num_index -= 1
            sub_index -= 1
            print ("sublist not included")
        print ("inner_i : " + str(inner_i))
      outer_i -= 1
      print ("outer_i : " + str(outer_i))

######################

def isSubset(sub_list,full_list):
   full_length = len(full_list)
   sub_length = len(sub_list)
   sub_end = sub_length - 1
   last_index = full_length - sub_length + 1
   
   outer_i = 0
   num_index = 0
   sub_index = 0

   while outer_i < last_index:
      while sub_index < sub_length:
        if sub_list[sub_index] == full_list[num_index]:
           print("subListNumber: " +str(sub_list[sub_index]) + " found in full_list["+str(num_index)+"]")
           if sub_index == sub_end:
              print("subList found starting at fullListIndex[" +str(num_index-sub_length+1)+"]")
              return(num_index-sub_length+1)

           num_index += 1
           sub_index += 1
        else:
           print("number = " +str(sub_list[sub_index]) + " not found")
           break
        
      outer_i += 1
      num_index = outer_i
      sub_index = 0
      print ("outer_i : " + str(outer_i) + " num_index : " + str(num_index))
   print ("sublist not found")
######################

#reverse_search_sub(sub_list,full_list)
isSubset(sub_list,full_list)
      
   
