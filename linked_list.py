from node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def append(self, value):
        if self.head_node is None:
            self.head_node = Node(value, None)
        current_node = self.head_node
        while True:
            if current_node.next() is None:
                current_node.next_value = Node(value, None)
                return
            current_node = current_node.next()

    def length(self):
        length_so_far = 0
        current_node = self.head_node
        while current_node is not None:
            length_so_far += 1
            current_node = current_node.next()
        return length_so_far - 1
