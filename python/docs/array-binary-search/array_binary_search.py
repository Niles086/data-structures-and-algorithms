def binary_search(sorted_array, search_key):
    left, right = 0, len(sorted_array) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_array[mid] == search_key:
            return mid  # Element found, return its index
        elif sorted_array[mid] < search_key:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Element not found

# Example usage:
arr1 = [4, 8, 15, 16, 23, 42]
key1 = 15
result1 = binary_search(arr1, key1)
print(result1)  # Output: 2

arr2 = [-131, -82, 0, 27, 42, 68, 179]
key2 = 42
result2 = binary_search(arr2, key2)
print(result2)  # Output: 4

arr3 = [11, 22, 33, 44, 55, 66, 77]
key3 = 90
result3 = binary_search(arr3, key3)
print(result3)  # Output: -1

arr4 = [1, 2, 3, 5, 6, 7]
key4 = 4
result4 = binary_search(arr4, key4)
print(result4)  # Output: -1
