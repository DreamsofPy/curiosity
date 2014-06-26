"""Using two stacks recreate a queue"""
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enq(self, x):
        self.stack1.append(x)

    def deq(self):
        if not self.stack2:
            for i in xrange(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        print self.stack2.pop()
