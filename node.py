from typing import Optional


class Node[T]:
    def __init__(self, data: T, next_value: Optional):
        self.data = data
        self.next_value = next_value

    def next(self) -> T:
        return self.next_value

    def append(self, node) -> None:
        if self.next_value is None:
            self.next_value = node
        else:
            self.next_value.append(node)

    def length(self) -> int:
        if self.next_value is None:
            return 1
        return 1 + self.next_value.length()
