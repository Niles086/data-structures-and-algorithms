# Array Binary Search
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![whiteboard](./whiteboard3.png)

## Approach & Efficiency
The binary search algorithm is a divide-and-conquer algorithm that efficiently finds the position of a target element in a sorted array. Here's a high-level overview of the approach:

Initialize: Set the left and right boundaries of the search space based on the entire array.
Divide: Calculate the middle index of the current search space.
Conquer: Compare the element at the middle index with the search key.
If they are equal, the search is successful, and the index is returned.
If the element is less than the search key, update the left boundary to the right of the middle.
If the element is greater than the search key, update the right boundary to the left of the middle.
Repeat: Continue the process until the left boundary is greater than the right boundary.

The efficiency of binary search is notable for its time complexity, which is O(log n), where n is the number of elements in the array. This is significantly more efficient than linear search (O(n)), especially for large datasets.
## Solution
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
print(f"Index of {key1} in {arr1}: {result1}")

arr2 = [-131, -82, 0, 27, 42, 68, 179]
key2 = 42
result2 = binary_search(arr2, key2)
print(f"Index of {key2} in {arr2}: {result2}")

arr3 = [11, 22, 33, 44, 55, 66, 77]
key3 = 90
result3 = binary_search(arr3, key3)
print(f"Index of {key3} in {arr3}: {result3}")

arr4 = [1, 2, 3, 5, 6, 7]
key4 = 4
result4 = binary_search(arr4, key4)
print(f"Index of {key4} in {arr4}: {result4}")
