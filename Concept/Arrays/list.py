#list
#find duplicate aaray
#brut force
def logic_duplicate(arr):
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i]==arr[j]:
             return True
    return False

arr=[0,2,7,3,4,5,1,0]
print(logic_duplicate(arr))

#hard code:

#next logic
