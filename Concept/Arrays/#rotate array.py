#rotate array
def rotate_arrat(arr,k):
    new_arr=[]
    for i in range(k%len(arr)):
        new_arr.append(arr[len(arr)-k+i])
    for i in range(len(arr)-k%len(arr)):
        new_arr.append(arr[i])
    return new_arr

arr=[6,5,1,2,4,5]
k=3
print("rotate_array--",rotate_arrat(arr,k))


#time complexuty high space low

#REVERSE ALGO

def reverse(arr,start,end):#wrong later see
    while start<end:
        print(start,end)
        arr[start],arr[end]=arr[end],arr[start]
        start=+1
        end-=1
    return arr

def reverse_rote(arr,k):
    arr=reverse(arr,0,len(arr)-1)#reverse whole sarr
    print(arr)
    arr=reverse(arr,0,k%len(arr)-1)#reverse first k terms
    print(arr)
    arr=reverse(arr,k%len(arr),len(arr)-1)#reverse first n-k elements
    print(arr)
    return arr

arr= [9,5,3,3,2,4,24,56]
k=4
print(reverse_rote(arr,k))


