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
