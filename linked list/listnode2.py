class node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None
class slinkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    def atbegining(self,newdata):
      newnode = node(newdata)
      newnode.nextval = self.headval
      self.headval = newnode


      
list1=slinkedlist()

list1.headval=node('mon')
e2=node('tue')
e3=node('wed')
list1.headval.nextval=e2
e2.nextval=e3
list1.atbegining('sun')
list1.listprint()




