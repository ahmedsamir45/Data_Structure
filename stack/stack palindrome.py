again = 'y'
while again == 'y':
    class stack :
        def __init__(self , limit = 10):
            self.stk = []
            self.limit = limit

        def push(self,item):
            if len(self.stk)>= self.limit:
                print('stack overflow')
            else:
                self.stk.append(item)
            print('stack after push ',self.stk)
            
        def pop(self):
                if len(self.stk)<=0:
                    print('stack under flow')
                else:
                    return self.stk.pop()
                
    def palindrome(ipt,length):
        p = False
        s = stack()
        for c in ipt:
            s.push(c)
        for c in ipt:
            if c==s.pop():
                p = True
            else:
                p = False
        return p
    
    x = input('enter your palindrome : ')
    if (palindrome(x,len(x))):
        print(' string is palindrome : ')
    else:
        print('string is not palindrome :')
    again = input(' enter y to repeat again')                                
