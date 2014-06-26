"""Using two stacks recreate a queue"""
class Queue:
    # Initialize two empty stacks
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # On enqueue we keep adding the values to stack 1
    def enq(self, x):
        self.stack1.append(x)

    # On dequeue we check to see if it empty, if not we pop the element for
    # stack2. Else, we pop all elements for stack1 and append them into stack2
    def deq(self):
        if not self.stack2:
            for i in xrange(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        try:
            print self.stack2.pop()
        except IndexError:
            print "No more elements in the queue"
def main():
    q = Queue()
    q.enq(1)
    q.enq(2)

    q.deq()
    q.deq()
    q.deq()

if __name__ == "__main__":
    main()
