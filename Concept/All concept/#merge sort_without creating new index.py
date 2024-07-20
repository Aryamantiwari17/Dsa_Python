#merge sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    
    left=arr[:mid]
    
    right=arr[mid:]
    
    merge_sort(left)
    
    merge_sort(right)

    merge_sort_real(left,right,arr)
     
  


def merge_sort_real(a,b,arr):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)

    i=j=k=0

    while i<len_a and j<len_b:#2 sorted 
        if a[i]<=b[j]:
            arr[k]=a[i]
            
            i+=1#list one

        else:
            arr[k]=b[j]
            j+=1#list two
        k+=1

    while i<len_a:
        arr[k]=a[i]
        i+=1
        k+=1
    
    while j<len_a:
        arr[k]=b[j]
        j+=1
        k+=1


    return sorted_list




if __name__=="__main__":
  #  a=[5 ,8,12,56]#sorted array
  #  b=[7,9,45,51]#sorted aray 
    arr=[10,3,15,7,8,23,98,29]
    for arr in test_cases:

     merge_sort(arr)
     print(arr)