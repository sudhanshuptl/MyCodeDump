

class Queue():
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, data):
        self.queue.append(data)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(0)
        else:
            print('Queue is Empty')

    def __str__(self):
        return str(self.queue)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    print('Dequeue :',queue.dequeue())
    print(queue)