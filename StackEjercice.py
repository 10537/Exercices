# ~ Stack used LIFO -> Last In First Out
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data = self.stack[-1]
        return data

    def sizeStack(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
print("Pushed in stack: 1")
stack.push(2)
print("Pushed in stack: 2")
stack.push(3)
print("Pushed in stack: 3")
print("Len:", stack.sizeStack())
print("Popped:", stack.pop())
print("len:", stack.sizeStack())
print("Peek:", stack.peek())
print("len:", stack.sizeStack())
