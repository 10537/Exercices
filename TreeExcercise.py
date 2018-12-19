class Node(object):
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node")
                del node
                return None

            if not node.leftChild:
                print("Removing single right child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing single left child")
                tempNode = node.leftChild
                del node
                return tempNode
            print("Remove node two children")
            tempNode = self.getAncestor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node

    def getAncestor(self, node):
        if node.rightChild:
            return self.getAncestor(node.rightChild)
        return node

    def getMinValue(self):
        if self.root:
            return self.minValue(self.root)

    def minValue(self, node):
        if node.leftChild:
            return self.minValue(node.leftChild)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.maxValue(self.root)

    def maxValue(self, node):
        if node.rightChild:
            return self.maxValue(node.rightChild)
        return node.data

    def transverse(self):
        if self.root:
            self.inOrderTransversal(self.root)

    def inOrderTransversal(self, node):
        if node.leftChild:
            self.inOrderTransversal(node.leftChild)

        print("Node data: {}".format(node.data))

        if node.rightChild:
            self.inOrderTransversal(node.rightChild)

bts = BinaryTree();
bts.insert(10)
bts.insert(5)
bts.insert(29)
bts.insert(32)
bts.insert(27)
bts.insert(1)
bts.insert(8)
print("Máximo: ", bts.getMaxValue())
print("Minímo: ", bts.getMinValue())
bts.transverse()
bts.remove(bts.getMaxValue())
print("Remove max value")
print("Máximo: ", bts.getMaxValue())
print("Minímo: ", bts.getMinValue())
bts.transverse()
