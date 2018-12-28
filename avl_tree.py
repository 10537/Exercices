class node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class AVL(object):
    def __init__(self):
        self.root = None

    def calculate_height(self, node):
        if not node:
            return -1

        return node.height

    # ~ if it returns value > 1 it means it is a left heavy tree --> right rotation
    # ~ if it returns value < 1 it means it is a right heavy tree --> left rotation
    def calculate_balance(self, node):
        if not node:
            return 0
        return self.calculate_height(node.leftChild) - \
        self.calculate_height(node.rightChild)

    def rotateRight(self, node):
        print("Rotating to the right on node", node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calculate_height(node.leftChild), \
        self.calculate_height(node.rightChild) + 1)

        tempLeftChild.height = max(self.calculate_height(tempLeftChild.leftChild), \
        self.calculate_height(tempLeftChild.rightChild) + 1)

        return tempLeftChild

    def rotateLeft(self, node):
        print("Rotating to the right on node", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calculate_height(node.leftChild), \
        self.calculate_height(node.rightChild)) + 1

        tempRightChild.height = max(self.calculate_height(tempRightChild.leftChild), \
        self.calculate_height(tempRightChild.rightChild)) + 1

        return tempRightChild

    def insert(self,data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calculate_height(node.leftChild), \
        self.calculate_height(node.rightChild)) + 1
        return self.settleViolation(data, node)
