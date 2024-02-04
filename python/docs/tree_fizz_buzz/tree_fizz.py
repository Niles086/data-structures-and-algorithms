class KaryNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

# Create a sample k-ary tree
# Replace the values and structure with your actual tree
root = KaryNode(15, [
    KaryNode(9, [KaryNode(3), KaryNode(6)]),
    KaryNode(10, [KaryNode(2), KaryNode(5)])
])

# Define the fizz_buzz_tree function

def fizz_buzz_tree(root):
    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    def fizz_buzz_recursive(node):
        node.value = fizz_buzz(node.value)
        for child in node.children:
            fizz_buzz_recursive(child)

    new_root = KaryNode(fizz_buzz(root.value), [fizz_buzz_tree(child) for child in root.children])
    fizz_buzz_recursive(new_root)
    return new_root

# Apply the fizz_buzz_tree function
new_tree = fizz_buzz_tree(root)

# Now 'new_tree' contains the transformed k-ary tree based on the FizzBuzz rules
