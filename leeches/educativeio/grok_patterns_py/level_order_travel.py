from collections import deque

"""
https://www.educative.io/courses/grokking-the-coding-interview/xV7E64m4lnz
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
                         /12\
                   /7\           /1\
                 9           10        5
                 
 Level Order Traversal: [12]
                        [7, 1]
                        [9, 10, 5]                     
"""

result = []


class TreeNode:

	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


"""
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""


def in_order(root: TreeNode):
	if root:
		in_order(root.left)
		result.append(root.val)
		in_order(root.right)


def traverse(root):
	#result = []
	# TODO: Write your code here
	if root is None:
		return result

	queue = deque()
	queue.append(root)
	while queue:
		level_size = len(queue)
		current_level = []
		for _ in range(level_size):
			current_node: TreeNode = queue.popleft()
			current_level.append(current_node.val)
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
		result.append(current_level)
	return result


def main():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(7)

	# 1) Level order traversal
	print("Level order traversal: " + str(traverse(root)))


	# 2) In-order traversal
	# in_order(root)
	# print("In order traversal: " + str(result))


#main()
