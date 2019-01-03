class Node(object):
    def __init__(self, data):
        self.data = data
        self.height = 0
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

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calculate_height(node.leftChild), \
        self.calculate_height(node.rightChild)) + 1
        return self.settleViolation(data, node)

    def settleViolation(self, data, node):
        balance = self.calculate_balance(node)

        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy case I")
            return self.rotateRight(node)

        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy case II")
            return self.rotateLeft(node)

        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy case III")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy case IV")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def transverse(self):
        if self.root:
            self.tranverseSort(self.root)

    def tranverseSort(self, node):
        if node.leftChild:
            self.tranverseSort(node.leftChild)

        print("{}".format(node.data))

        if node.rightChild:
            self.tranverseSort(node.rightChild)

    def removeNode(self, data, node):
        # ~ TODO: Corregir error al eliminar nodo cuando se calcula el height
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return Node
            if not node.leftChild:
                print("Removing a node with a rightChild")
                temp_node = node.rightChild
                del node
                return temp_node
            elif not node.rightChild:
                print("Removing a node with a leftChild")
                temp_node = node.leftChild
                del node
                return temp_node

            print("Removing node with two children...")
            temp_node = self.getParent(node.leftChild)
            node.data = temp_node.data
            node.leftChild = self.removeNode(temp_node.data, node.leftChild)

        if not node:
            return node

        node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
        balance = self.calculate_balance(node)

        if balance > 1 and self.calculate_balance(node.leftChild) >= 0:
            return self.rotateRight(node)

        if balance > 1 and self.calculate_balance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and self.calculate_balance(node.rightChild) <= 0:
            return self.rotateLeft(node)

        if balance < -1 and self.calculate_balance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def unlink(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)


avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)
avl.transverse()

avl.unlink(15)
avl.unlink(20)
avl.transverse()
