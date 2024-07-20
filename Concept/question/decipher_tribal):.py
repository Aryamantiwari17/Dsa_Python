def decipher_tribal_affiliation(n):
    # Check if n is a Power of Two
    power_of_two = 1
    while power_of_two < n:
        power_of_two *= 2
    if power_of_two == n:
        return 2

    # Check if n is a Power of Three
    power_of_three = 1
    while power_of_three < n:
        power_of_three *= 3
    if power_of_three == n:
        return 3

    # If n is not aligned with any tribe
    return False

# Test the magical artifact
integer_to_test = 16  # You can change this value to test different integers
result = decipher_tribal_affiliation(integer_to_test)

if result:
    print(f"The integer {integer_to_test} belongs to the Powers of {result}.")
else:
    print(f"The integer {integer_to_test} is not aligned with any tribe.")
