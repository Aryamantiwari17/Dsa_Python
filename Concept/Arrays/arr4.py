def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[z] = array[z], array[i]
            z += 1
    return array
array=[9,0,7,6,0,7]
print(swap_move(array))