"""
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
Original List:
    head -> 2  ->  4 ->  6 ->   8 ->   10 ->   null
 Reversed List:
    null <- 2  <-  4 <-  6 <-   8 <-   10 <-  head
 

"""
from __future__ import print_function


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	
	def print_list(self):
		temp = self
		while temp is not None:
			print(temp.value, end=" ")
			temp = temp.next
		print()


def reverse(head) -> Node:
	prev, current, next_node = None, head, None
	
	while current is not None:
		next_node = current.next
		current.next = prev
		prev = current
		current = next_node
	
	return prev


def main():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(8)
	head.next.next.next.next = Node(10)
	
	print("Nodes of original LinkedList are: ", end='')
	head.print_list()
	result = reverse(head)
	print("Nodes of reversed LinkedList are: ", end='')
	result.print_list()


main()
