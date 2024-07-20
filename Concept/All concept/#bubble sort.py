#bubble sort

def buble_sort(elements):
 size=len(elements)

 for j in range(size-1):
  swapped=False#if already sorted array dont go to swapaed and check again again the elements
  
  for i in range(size-1-j):#-j to ignore the sorted elementsmeans the last emlemnts
   if elements[i]>elements[i+1]:
     tmp=elements[i]
     elements[i]=elements[i+1]
     elements[i+1]=tmp
     swapped=True

   if not swapped:
    break



if __name__=="__main__":
 elements=[13,12,15,23,22,1]
 buble_sort(elements)
 print(elements)

