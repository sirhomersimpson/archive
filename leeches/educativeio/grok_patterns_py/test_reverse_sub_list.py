from reverse_sub_list import *


def test_reverse_sub_list():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	new_head = reverse_sub_list(head, 2, 4)
	
	expected_values = [1, 4, 3, 2, 5]
	current_node = new_head
	for index in range(len(expected_values)):
		assert current_node.value == expected_values[index]
		current_node = current_node.next

