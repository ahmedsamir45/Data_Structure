class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def in_order(root):
    if root == None :
        return
    
    in_order(root.left)
    print(root.value)
    in_order(root.right)


root = TreeNode(10)
node5 = TreeNode('s')
node18 = TreeNode(18)
node3 = TreeNode(3)
node7 = TreeNode(7)



root.left = node5
root.right = node18
node5.left = node3
node5.right = node7



in_order(root)
