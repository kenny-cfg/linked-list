class Node:
    def __init__(self, data, next_value):
        self.data = data
        self.next_value = next_value

    def next(self):
        return self.next_value

    def append(self, node):
        if self.next_value is None:
            self.next_value = node
        else:
            self.next_value.append(node)
