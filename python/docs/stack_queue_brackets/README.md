# stack_queue_brackets
<!-- Description of the challenge -->

## Whiteboard Process

![whiteboard](./whiteboard13.png)

## Approach & Efficiency
The validate_brackets function uses a stack-based approach to determine whether the brackets in the given string are balanced or not. Here's a breakdown of the approach and its efficiency:

Approach:
Initialize an empty stack to keep track of opening brackets encountered.
Define a dictionary (brackets) with mappings of opening and closing brackets.
Iterate through each character in the input string:
If the character is an opening bracket, push it onto the stack.
If the character is a closing bracket:
Pop the top element from the stack.
Check if the popped element matches the corresponding opening bracket.
If not, return False (brackets are unbalanced).
After the iteration, check if the stack is empty.
If not, return False (brackets are unbalanced).
If empty, return True (brackets are balanced).
Efficiency:
Time Complexity: The time complexity is O(n), where n is the length of the input string 's'. This is because the algorithm iterates through each character in the string once, and stack operations take constant time.
Space Complexity: The space complexity is O(n) in the worst case. In the worst scenario, all opening brackets are pushed onto the stack, and it does not decrease until the end of the string.
This approach is efficient for determining bracket balance, and its time complexity scales linearly with the size of the input string. The stack-based approach ensures that the closing brackets match the most recently opened brackets, making it a reliable method for bracket validation.






## Solution
The validate_brackets function employs a stack-based approach to check the balance of brackets in a given string. It iterates through each character, using a stack to keep track of opening brackets and ensuring that each closing bracket corresponds to the most recently opened one. The time complexity is O(n), where n is the length of the input string, making the solution linear and efficient for bracket validation.



# usage:

# Define the validate_brackets function
def validate_brackets(s):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in brackets.keys():  # Opening bracket
            stack.append(char)
        elif char in brackets.values():  # Closing bracket
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack  # The brackets are balanced if the stack is empty

# Example Usage:
input_string = "{}(){}"
result = validate_brackets(input_string)

# Display the result
print(f"Input: {input_string}")
print(f"Output: {result}")
