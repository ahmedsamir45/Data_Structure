class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def in_order(root):
    if root == None :
        return
    
    in_order(root.left)
    print(root.value ,end='')
    in_order(root.right)


root = TreeNode('-')
node2 = TreeNode('+')
node3 = TreeNode('6))')
node4 = TreeNode('*')
node5 = TreeNode('-')
node6 = TreeNode('((3')
node7 = TreeNode('4))')
node8 = TreeNode('(7')
node9 = TreeNode('/')
node10 = TreeNode('+')
node11 = TreeNode('*')
node12 = TreeNode('2))')
node13 = TreeNode('-')
node14 = TreeNode('((9')
node15 = TreeNode('5)')
node16 = TreeNode('+')
node17 = TreeNode('3)')
node18 = TreeNode('((((3')
node19 = TreeNode('1)')



root.left = node9
root.right = node2
node9.left = node11
node9.right = node10
node11.right = node17
node11.left = node16
node16.right = node19
node16.left = node18
node10.right = node12
node10.left= node13
node13.right = node15
node13.left = node14
node2.right = node3
node2.left = node4
node4.right = node5
node4.left = node6
node5.right = node7
node5.left = node8






in_order(root)
