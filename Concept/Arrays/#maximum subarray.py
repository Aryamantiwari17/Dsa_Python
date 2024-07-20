#maximum subarray
def brut_force_max_subarray(array):
    maximum=0#maximum =0
    if len(array)==0:
        return None
    for i in range (len(array)):#every element for array le rhe hai
        c_sum=0#sum =0
        for j in range(i,len(array)):#create ek subarray
            c_sum+=array[j]
            maximum=max(maximum,c_sum)
    return maximum

array=[-2,1,-3,4,-1,2,1,-5,4]
print(brut_force_max_subarray(array))

#algo kadane_to find largest sub array:


def kadanes_max_subarray(array):
    if len(array) == 0:
        return None
    
    max_ending_here = max_so_far = array[0]
    for i in range(1,len(array)):
        maxarray = max(array[i], maxarray+array[i])
        maximum = max(maxarray, maximum)
    return maximum

print(kadanes_max_subarray(array))

