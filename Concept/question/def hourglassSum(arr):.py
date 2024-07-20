def hourglassSum(arr):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity

    # Iterate through the array to find hourglass sums
    for i in range(4):
        for j in range(4):
            # Calculate the sum of the current hourglass
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example array
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# Calculate and print the maximum hourglass sum
print(hourglassSum(arr))
