def duplicate(arr):
    try:
        arr.sort()
        for i in range(len(arr)):
            if arr[i] == arr[i+1]:
                return True  # Return True if duplicate found

        return False  # Return False if no duplicate found

    except ValueError:
        print("Error: Please enter a valid array")


arr_1 = []   
n = int(input("Enter the size of the array: "))
for i in range(n):
    ele = int(input("Enter element {}: ".format(i+1)))
    arr_1.append(ele)    

if duplicate(arr_1):
    print("Duplicate found")
else:
    print("No duplicate found")

    ##n your original code, you were trying to access arr[i + 1] inside the loop. If the loop went up to len(arr), when i was 
#equal to len(arr) - 1 (which is 4 in this case), arr[i + 1] would be equivalent to arr[5], and there is no element at index 5 in the array. 
#This would cause an "index out of range" error because you're trying to access an element that doesn't exist.\