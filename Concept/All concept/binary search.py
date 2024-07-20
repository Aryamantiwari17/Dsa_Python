def linear_search(num_list,num_to_find):
    num_list.sort()
    for index,element in enumerate(num_list):#a built-in function that allows you to iterate through a sequence and keep track of the index of each element
        
        if element==num_to_find:#order of n
            return index
        
    return -1

        




def binary_search(num_list,num_to_find):
    num_list.sort()
    left_index=0
    right_index=len(num_list)-1
    mid_index=0
    while left_index<right_index:
       
     mid_index=((right_index+left_index)//2 )
     mid_num=num_list[mid_index]#num_list[5]-miidle element hoga

     if mid_num==num_to_find:
        return mid_index
    
     if mid_num<num_to_find:
        left_index=mid_index+1

     else:
        right_index=mid_index-1
    return None

def recur(num_list,num_to_find,left_index,right_index):
   
   num_list.sort()
   if right_index<left_index:
      return -1
   mid_index=((right_index+left_index)//2 )
   mid_num=num_list[mid_index]#
   
   if mid_num==num_to_find:
        return mid_index
    
   if mid_num<num_to_find:
        left_index=mid_index+1

   else:
        right_index=mid_index-1
  
   return recur(num_list,num_to_find,left_index,right_index)

"""
 def find_all_occurances(num, num_to_find):
    index = binary_search(num, num_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if num[i] == num_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(num):
        if num[i] == num_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)
"""
   

   


   

      







    


if __name__=="__main__":
 num_list=[1,4,6,9,10,5,7]
 num_to_find=7
 ind=linear_search(num_list,num_to_find)
 ind=binary_search(num_list,num_to_find)
 ind=recur(num_list,num_to_find,0,len(num_list))
 #indices = find_all_occurances(num, num_to_find)
 #print(f"Indices of occurances of {num_to_find} are {indices}")
 print(f"number found at postion ", ind)





 