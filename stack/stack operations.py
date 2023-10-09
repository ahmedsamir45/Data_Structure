class stack :
    def __init__(self,limit=10):
        self.s = []
        self.limit = limit
        
        # insest a new element to end the stack
    def push(self,value):
        self.s.append(value)
        print('stack after push ',self.s)
        
        # remove the last elenent
    def pop(self):
        if self.isempty():
            print('error')
        else:
            self.s.pop()

    def isempty(self):
        if len(self.s) ==0:
            return True
        else:
            return False

    def top(self):
        if self.isempty():
            print('error')
            return None
        else:
            return self.s[-1]


            
stack = stack()
stack.push(10)
stack.push(5)
stack.push(1)
print(stack.top())
print(stack.isempty())


