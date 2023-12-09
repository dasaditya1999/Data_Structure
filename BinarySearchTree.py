class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        # self.inOrderArr = []
    
    def addChild(self,data):
        
        # '''Check if the new data is already existing in the BST'''
        if data == self.data:
            return
        
        # ''''Check if the new data is greater than the root node''''
        elif data > self.data:
            if self.right == None:
                newNode = BinarySearchTreeNode(data)
                self.right = newNode
            else:
                self.right.addChild(data)            

        # '''Check if the new data is less than the root node'''
        else:
            if self.left == None:
                newNode = BinarySearchTreeNode(data)
                self.left = newNode
            else:
                self.left.addChild(data)

    def inOrder(self):
        elements = []

        #Checking with the left node
        if self.left:
            elements += self.left.inOrder()
        
        #Appending the root node of every sub-tree/tree
        elements.append(self.data)

        #Checking with the right node
        if self.right:
            elements += self.right.inOrder()
        
        return elements

    def preOrder(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.preOrder()
        
        if self.right:
            elements += self.right.preOrder()

        return elements

    def postOrder(self):
        elements = []

        if self.left:
            elements += self.left.postOrder()

        if self.right:
            elements += self.right.postOrder()
        
        elements.append(self.data)

        return elements

    def printBinraySearchTree(self, order):
        # '''Traverse in the user defined format, i.e. Inorder, PreOrder, 
        # PostOrder'''

        if order == 'inorder':
            return self.inOrder()
        elif order == 'preorder':
            return self.preOrder()
        else:
            return self.postOrder()

if __name__ == '__main__':
    rootNode = BinarySearchTreeNode(30)
    rootNode.addChild(20)
    rootNode.addChild(10)
    rootNode.addChild(40)
    rootNode.addChild(50)
    rootNode.addChild(100)

    print('Print the BST in Inorder')
    print(rootNode.printBinraySearchTree('inorder'))

    print('Print the BST in PreOrder')
    print(rootNode.printBinraySearchTree('preorder'))

    print('Print the BST in PostOrder')
    print(rootNode.printBinraySearchTree('postorder'))