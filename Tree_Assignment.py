class Tree:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append((child))

    def getLevel(self):
        level = 0
        itr = self.parent
        while itr:
            level = level + 1
            itr = itr.parent
        return level

    def printTree(self):
        spaces = ' '* self.getLevel()
        prefix = spaces + '|--' if self.parent else ""
        print(prefix, self.name, '(',self.designation,')')
        if self.children:
            for i in self.children:
                i.printTree()


if __name__ == '__main__':
    #Initializing the tree
    tree = Tree('Aditya','CEO')

    #Initializing the sub tree
    cto = Tree('Chinmay','CTO')
    #Adding nested child nodes
    infra = Tree('Vishwa','Infra Head')
    infra.add_child(Tree('Dhaval','Cloud Manager'))
    infra.add_child(Tree('Abhijit','App Manager'))
    cto.add_child(infra)

    #Initializing the sub tree
    hr = Tree('Gels','HR Head')
    #Adding nested child nodes
    hr.add_child(Tree('Peter','Recruitement Manager'))
    hr.add_child(Tree('Waqas','Policy Manager'))

    #Adding Sub trees to the Root node
    tree.add_child(cto)
    tree.add_child(hr)

    tree.printTree()

