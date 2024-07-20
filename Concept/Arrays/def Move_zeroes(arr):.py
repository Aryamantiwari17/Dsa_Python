def Move_zeroes(arr):
    l = len(arr)#length of an array
    for i in range(l):
        if arr[i] == 0:
            arr.append(0)#aappend 0

    j = 0
    c = 0
    while c < l:
        if arr[j] != 0:
            j += 1
        else:
            arr.pop(j)
            c += 1
            l -= 1
    return arr

arr = [0, 5, 0, 0, 24, 9, 0, 5, 0, 5]
print("new array", Move_zeroes(arr))
#

#"""lenn(arr) - 1: This part gives us the last index of the string arr. We subtract 1 because indices start at 0, and we want to start from the last character of the string.

#-1: This is the stopping point for the loop. It means we want to go all the way down to the first index (0). So, the loop will continue until it reaches -1."""

#-1: This is the step size. It tells the loop to move backward, one index at a time.

