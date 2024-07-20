#merge sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    
    left=arr[:mid]
    
    right=arr[mid:]
    
    left=merge_sort(left)
    
    right=merge_sort(right)

    return merge_sort_real(left,right)
     
  


def merge_sort_real(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)

    i=j=0

    while i<len_a and j<len_b:#2 sorted 
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1#list one

        else:
            sorted_list.append(b[j])
            j+=1#list two

    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    
    while j<len_a:
        sorted_list.append(b[j])
        j+=1


    return sorted_list




if __name__=="__main__":
  #  a=[5 ,8,12,56]#sorted array
  #  b=[7,9,45,51]#sorted aray 
    arr=[10,3,15,7,8,23,98,29]
    print(merge_sort(arr))