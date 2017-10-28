class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
                currentNode.value = val
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)
                currentNode.value = val

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def print_data(self):
        return self.print_node(self.root)

    def print_node(self, current_node):
        print current_node.val
        if current_node.leftChild is not None and current_node.rightChild is not None:
            self.print_node(current_node.leftChild)
            self.print_node(current_node.rightChild)
            return
        elif current_node.leftChild is not None:
            self.print_node(current_node.rightChild)
            return
        elif current_node.rightChild is not None:
            self.print_node(current_node.leftChild)
            return


b = BST()
b.setRoot(20)
b.insert(35)
b.insert(13)
b.print_data()