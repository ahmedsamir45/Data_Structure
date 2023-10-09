class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def pre_order(root):
    if root == None :
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)


root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.right = node6


pre_order(root)
