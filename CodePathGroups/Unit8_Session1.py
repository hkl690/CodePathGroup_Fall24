class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right




from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")

print_tree(root)

def right_vine(root):
    rightvine = []
    current = root

    while current:
        rightvine.append(current.val)
        if current.right:
            current = current.right
        else:
            break
    return rightvine

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

def rec_right_vine(root):
    if root is None:
        return []
    else:
        return [root.val] + rec_right_vine(root.right)


ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

def count_leaves(root):
    if root is None:
        return 0

    # if the node is a leaf, return 1
    if root.left is None and root.right is None:
        return 1

    left_leaves = count_leaves(root.left)
    right_leaves = count_leaves(root.right)

    return left_leaves + left_leaves

oak1 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")), TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(count_leaves(oak1))
print(count_leaves(oak2))