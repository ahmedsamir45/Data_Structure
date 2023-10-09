class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self,value):
        s=self.q.append(value)
    def dequeue (self):
        self.q.pop(0)
    def front(self):
        return self.q[0]
        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)

size = 10
count=0
while count < size :
    print(queue.front())
    queue.dequeue()
    count+=1
