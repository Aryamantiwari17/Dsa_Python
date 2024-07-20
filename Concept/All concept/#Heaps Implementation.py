#Heaps Implementation

def max_heapify(arr,n,i):
    largest=i#pinting to the the root node
    left=2*i+1
    right=2*i+2
   #largest so far is compared with left child
    if left<n and arr[largest]<arr[left]:
       largest=left

    
    #largest is so far compared with right
    if right<n and arr[largest]<arr[right]:
       largest=right


    #change the parent
    if largest!=i:
       arr[i],arr[largest]=arr[largest],arr[i]
    
       max_heapify(arr,n,largest)
       #return arr
    


       

if __name__=="__main__":
   arr=[2,66,30,5,8,10]
   n=len(arr)

#bulisd a max heap
   for i in range(n//2-1,-1,-1): #-1 i ==-1,i iteration till -1
      max_heapify(arr,n,i)


#display

   print("max heap")
   for i in range(n):
     print(arr[i],end=" ")


