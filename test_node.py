import unittest

from node import Node


class TestNode(unittest.TestCase):
    def test_can_instantiate_a_node_with_no_next_value(self):
        node = Node(0, None)

        self.assertIsNotNone(node)

    def test_can_instantiate_a_node_with_a_next_value(self):
        tail_node = Node(1, None)
        node = Node(0, tail_node)

        self.assertIsNotNone(node)
        self.assertIsNotNone(node.next())


if __name__ == '__main__':
    unittest.main()
