# Challenge Title
<!-- Description of the challenge -->

## Whiteboard Process
[White Board Link](https://arrayreverse.invisionapp.com/freehand/Untitled-iQThI5jMZ)
![whiteboard](./whiteboard.png)

## Approach & Efficiency
My code for the reverse-array function uses a straightforward iterative approach to reverse an array. It initializes an empty list to store the reversed elements and iterates through the original array in reverse order, appending each element to the new list. The time complexity of this approach is O(n), where n is the length of the input array. The space complexity is also O(n) because a new list is created to store the reversed elements.

## Solution
simply navigate to the folder and run the code python array-reverse.py

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
