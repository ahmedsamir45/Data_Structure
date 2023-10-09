def findMaxUsingLevelOrder(root):
    if root is None:
            return
    q = Queue()
    q.enQueue(root)
    node = None
    maxElement = 0
    while not q.isEmpty():
            node = q.deQueue()
            if maxElement  < node.getData():
                    maxElement = node.getData()
            if node.left is not None:
                    q.enQueue(node.left)
            if node.right is not None:
                    q.enQueue(node.right)
print(maxElement)
