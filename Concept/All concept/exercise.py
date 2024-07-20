def bubble_sort(elements, key):
    size = len(elements)

    for j in range(size - 1):
        swapped = False  # If already sorted array, don't go to swap and check again

        for i in range(size - 1 - j):  # -j to ignore the sorted elements means the last elements
            a = elements[i][key]
            b = elements[i + 1][key]

            if a > b:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    bubble_sort(elements, key="transaction_amount")
    print(elements)
