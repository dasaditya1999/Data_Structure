class Tree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        itr = self.parent
        while itr:
            print('check',itr.data)
            level = level + 1
            itr = itr.parent
        return level
    
    def printTree(self):
        level = self.getLevel()
        spaces = ' '*level*2
        prefix = spaces + '|--' if self.parent else ""
        print(prefix,self.data)
        if self.children:
            for i in self.children:
                i.printTree()

def buildTree():
    #Root Node
    tree = Tree('Corporate')

    #Branch Node
    Software = Tree('Software Engineering')
    #Leaf Node
    Software.add_child(Tree('Front End Dev'))
    Software.add_child(Tree('Back End Dev'))
    Software.add_child(Tree('Full Stack Dev'))
    Software.add_child(Tree('Data Analyst'))
    Software.add_child(Tree('Data Scientist'))
    Software.add_child(Tree('AI Engineering'))

    #Branch Node
    bpo = Tree('Production Operations')
    #Leaf Node
    bpo.add_child(Tree('Chat Agent'))
    bpo.add_child(Tree('Team Lead'))
    bpo.add_child(Tree('Trainer'))

    #Branch Node
    ites = Tree('IT Infrastructure')
    #Leaf Node
    ites.add_child(Tree('Hardware Engineer'))
    ites.add_child(Tree('Troubleshoot Specialist'))
    ites.add_child(Tree('Team Lead'))

    #Branch Node
    sales = Tree('Sales')
    #Leaf Node
    sales.add_child(Tree('Account Manager'))
    sales.add_child(Tree('Key Sales Executive'))
    sales.add_child(Tree('Field Sales Representative'))
    sales.add_child(Tree('Customer Engineer'))

    tree.add_child(Software)
    tree.add_child(bpo)
    tree.add_child(ites)
    tree.add_child(sales)

    print('The Tree is:')
    tree.printTree()

if __name__=='__main__':
    buildTree()
