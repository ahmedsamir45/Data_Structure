class node :
    def __init__(self,data = None):
        self.data = data
        self.next = None

class slinkedlist:
    
    def __init__(self):
        self.head = None
        
    
            
    def atbegining(self,data_in):
        newnode = node(data_in)
        newnode.next = self.head
        self.head = newnode

    def removenode(self,removekey):
        headval = self.head
        if headval is not None:
            if headval.data == removekey:
                self.head = headval.next
                headval = None
                return

        while headval is not None:
            if headval.data==removekey:
                break
            prev=headval
            headval=headval.next
            
        if headval==None:
            return
        
        prev.next=headval.next
        headval=None
        
    def listprint(self):
        printval = self.head
        while printval != None :
            print(printval.data)
            printval = printval.next

list1 = slinkedlist()
dec = list1.atbegining('dec')
nov = list1.atbegining('nov')
oct1 = list1.atbegining('oct')
sep = list1.atbegining('sep')
list1.removenode('dec')
list1.listprint()






            
