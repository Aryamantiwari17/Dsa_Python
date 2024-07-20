from array import array

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  #  left half
        merge_sort(right_half)  #  right half

        i = j = k = 0

        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

       
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


num_elements = int(input("Enter the number of elements in the array: "))


user_input = input(f"Enter {num_elements} elements of the array separated by spaces: ")
arr = array('i', map(int, user_input.split()))

merge_sort(arr)
print("Sorted array:", arr)
