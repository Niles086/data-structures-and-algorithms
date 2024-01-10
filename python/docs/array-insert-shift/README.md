# array-insert-shift
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process
![whiteboard](./whiteboard2.png)

## Approach & Efficiency
Calculating the middle index of the array.
Shifting elements to the right starting from the last index and moving towards the middle index.
Inserting the new value at the calculated middle index.
This approach modifies the input array in-place without using any built-in methods.

The loop that shifts elements to the right iterates at most n/2 times, where n is the length of the array. Therefore, the time complexity is O(n).
## Solution
<!-- Show how to run your code, and examples of it in action -->