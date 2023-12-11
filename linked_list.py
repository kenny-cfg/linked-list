from node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def append(self, value):
        new_node = Node(value, None)
        if self.head_node is None:
            self.head_node = Node(value, None)
            return
        self.head_node.append(new_node)

    def length(self):
        if self.head_node is None:
            return 0
        return self.head_node.length()
