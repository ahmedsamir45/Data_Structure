class listnode:
    def __init__(self,value,next= None):
        self.value = value
        self.next = next

def print_list(head):
    p = head
    while p != None :
        print(p.value)
        p = p.next
def append_element(head,value):
    node = listnode(value)
    if head == None :
        head = node
    
def get_element(head,index):
    if (index < 0):
        print('enter integer value')
    p= head
    i=0
    while i < index and p != None :
        p = p.next
        i += 1
    if p != None:
        print(p.value)
    else:
        print('error')
        


node1=listnode('elmaadi')
node2=listnode('dar elslam')
node3=listnode('helwan')
node4=listnode('el tahrer')
#node5=listnode('wednesday')
#node6=listnode('thursday')
node1.next=node2
node2.next=node3
node3.next=node1
node1.next=node4
#node5.next=node6
#node6.next=node1
head=node1
print('before')
print_list(head)
#append_element(head,'friday')
#print('after')
#print_list(head)


get_element(head,0)
