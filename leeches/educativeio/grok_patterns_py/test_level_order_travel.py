from level_order_travel import *


def test_traverse():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Level order traversal: " + str(traverse(root)))

    assert [[1], [2, 3], [4, 5, 6, 7]] == traverse(root)

