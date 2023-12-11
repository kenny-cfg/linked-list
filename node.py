class Node:
    def __init__(self, data, next_value):
        self.data = data
        self.next_value = next_value

    def next(self):
        return self.next_value
