"""Reverse those words, son."""


def reverse_words(str):
    """Accept a parameter and reverses each word in the string."""

    class Node(object):
        """Creates a node object."""

        def __init__(self, data, below=None):
            """Constructor function."""
            self.data = data
            self.below = below

    class Stack(object):
        """Creates a stack."""

        def __init__(self):
            """Constructor."""
            self.top = None
            self.size = 0

        def push(self, data):
            """Add a node with given data to the stack."""
            new_node = Node(data)
            if not self.top:
                self.top = new_node
            else:
                new_node.below = self.top
                self.top = new_node

        def pop(self):
            """Remove the top of the stack and returns the value."""
            if not self.top:
                raise IndexError()
            temp = self.top.data
            self.top = self.top.below
            return temp

    train = Stack()
    ret_word = ""

    for i in str:
        train.push(i)

    while train.top:
        ret_word += train.pop()
