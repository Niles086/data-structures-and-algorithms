def reverseArray(arr):
    # Initialize an empty list to store the reversed elements

    reversed_arr = []

    # Iterate through the original array in reverse order

    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])

    return reversed_arr


# usage:

original_array = [1, 2, 3, 4, 5]

reversed_array = reverseArray(original_array)


print("Original Array:", original_array)

print("Reversed Array:", reversed_array)
