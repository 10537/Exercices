# Queue used FIFO -> First In First Out
class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(10)
print("Enqueued: 10")
queue.enqueue(20)
print("Enqueued: 20")
queue.enqueue(30)
print("Enqueued: 30")
print("Queue Size:", queue.sizeQueue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print("Queue Size:", queue.sizeQueue())
print("Peek Queue: ", queue.peek())
