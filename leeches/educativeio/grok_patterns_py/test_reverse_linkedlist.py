from reverse_linkedlist import *


def test_reverse():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(8)
	head.next.next.next.next = Node(10)
	new_head = reverse(head)
	
	expected_values = [10, 8, 6, 4, 2]
	current_node = new_head
	for index in range(len(expected_values)):
		assert current_node.value == expected_values[index]
		current_node = current_node.next
