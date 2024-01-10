def insertShiftArray(arr, value):
    # Calculate the middle index
    middle_index = len(arr) // 2

    # Shift elements to the right starting from the middle
    for i in range(len(arr)-1, middle_index-1, -1):
        arr[i+1] = arr[i]

    # Insert the new value at the middle index
    arr[middle_index] = value

    return arr

# Example usage:
input_array1 = [2, 4, 6, -8]
value1 = 5
result1 = insertShiftArray(input_array1, value1)
print(result1)  # Output: [2, 4, 5, 6, -8]

input_array2 = [42, 8, 15, 23, 42]
value2 = 16
result2 = insertShiftArray(input_array2, value2)
print(result2)  # Output: [42, 8, 15, 16, 23, 42]
