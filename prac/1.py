from collections import deque 

class Deque:
    def __init__(self):
        self.stack = deque()
        
    def push(self, item):
        self.stack.append(item)
        
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()
        
    def display(self):
        return self.stack
    
    def is_empty(self):
        return len(self.stack) == 0

new_deque = Deque()
print(new_deque.is_empty())
new_deque.push(1)
new_deque.push(2)
new_deque.push(3)
print(new_deque.display())

print(new_deque.pop())

print(new_deque.peek())
