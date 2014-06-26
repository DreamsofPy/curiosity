"""Two stacks queue"""

class Queue(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, obj):
        self.s1.push(obj)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())

        return self.s2.pop()


class Stack(object):
    def __init__(self):
        self._list = []

    def push(self, obj):
        self._list.append(obj)

    def pop(self):
        return self._list.pop()

    def __len__(self):
        return len(self._list)


def main():
    stack = Stack()

    for i in range(10):
        stack.push(i)

    print 'Testing stack'
    for expected in range(9, 0, -1):
        actual = stack.pop()

        print 'Expected: {}'.format(expected)
        print 'Actual: {}'.format(actual)
        assert actual == expected

    q = Queue()

    for i in range(10):
        q.enqueue(i)

    print 'Testing queue'
    for expected in range(10):
        actual = q.dequeue()

        print 'Expected: {}'.format(expected)
        print 'Actual: {}'.format(actual)
        assert actual == expected

    print 'Success!'


if __name__ == '__main__':
    main()
