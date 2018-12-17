class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def remove(self, value):

        if self.head == None:
            return None

        self.size = self.size - 1

        actualNode = self.head
        prevNode = None

        while actualNode.data != value:
                prevNode = actualNode
                actualNode = actualNode.nextNode

        if prevNode is None:
            self.head = actualNode.nextNode
        else:
            prevNode.nextNode = actualNode.nextNode

    def insertToStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size_list(self):
        return self.size

    def insertToEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def transverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{actualData}".format(actualData=actualNode.data))
            actualNode = actualNode.nextNode

linkedlist = LinkedList()
linkedlist.insertToStart(20)
linkedlist.insertToStart(34)
linkedlist.insertToStart(67)
linkedlist.insertToEnd(90)

linkedlist.transverseList()
print(linkedlist.size_list())

linkedlist.remove(34)
linkedlist.remove(90)

linkedlist.transverseList()
print(linkedlist.size_list())
