import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_can_instantiate_a_linked_list(self):
        linked_list = LinkedList()

        self.assertIsNotNone(linked_list)

    def test_can_append_to_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        self.assertEqual(linked_list.length(), 3)



if __name__ == '__main__':
    unittest.main()
