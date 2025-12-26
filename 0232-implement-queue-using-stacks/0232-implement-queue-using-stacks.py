class MyQueue(object):

    def __init__(self):
        self.in_stack=[]    #used to push values
        self.out_stack=[]   #used to pop values

    def push(self, x):
        self.in_stack.append(x)
        
    def pop(self):
        self.move_if_needed()
        return self.out_stack.pop()

    def peek(self):
        self.move_if_needed()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack
        
    def move_if_needed(self):
        if not self.out-stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()