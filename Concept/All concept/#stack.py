#stack
 #list collection.deque
from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    
    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):#fetching 1 st value of stack wt changing the stack
        print(self.container[-1])
    
    def is_empty(self):
        if (len(self.container)==0):
            print("empty")
        else:
          print("list has elements")    
    def size(self):
        return(len(self.container))

    def rev(self):
       return self.container.reverse()
    
    def display(self):
        print(self.container)
    

def less(ch1,ch2):
      match_dict={
          ')':'(',
          ']':'[',
          '}' : '{'
        }
      return match_dict[ch1] == ch2
    
def is_balanced(s):
        stack=Stack()
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.push(ch)

            if ch==')' or ch=='}' or ch==']':
                if stack.size() == 0 :
                    return False
                if not less(ch, stack.pop()):
                    return False
        return stack.size() == 0
                
      


    
if __name__=="__main__":
  #  s=Stack()
   # s.push(1)
  #  s.push(2)
  #  s.display()
    #s.pop()
  #  s.is_empty()
  #  s.peek()
   # s.display()
  #  s.size()
  #  s.rev()
 #   s.display(
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


    
    