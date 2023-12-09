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
            level = level + 1
            itr = itr.parent
        return level

    def printTree(self):
        prefix = ' ' * self.getLevel()
        print(prefix,self.data)
        if self.children:
            for i in self.children:
                i.printTree()


if __name__=='__main__':
    rootNode = Tree('Global')

    # Sub Tree
    india = Tree('India')

    gujurat = Tree('Gujurat')
    gujurat.add_child(Tree('Ahemdabad'))
    gujurat.add_child(Tree('Baroda'))
    india.add_child(gujurat)

    karnataka = Tree('Karnataka')
    karnataka.add_child(Tree('Bengaluru'))
    karnataka.add_child(Tree('Mysore'))
    india.add_child(karnataka)

    odisha = Tree('Odisha')
    odisha.add_child(Tree('Bhubaneswar'))
    odisha.add_child(Tree('Puri'))
    india.add_child(odisha)

    rootNode.add_child(india)

    # Sub Tree
    usa = Tree('USA')

    newjersey = Tree('New Jersey')
    newjersey.add_child(Tree('Priceton'))
    newjersey.add_child(Tree('Trenton'))

    california = Tree('California')
    california.add_child(Tree('San Fransisco'))
    california.add_child(Tree('Mountain View'))
    california.add_child(Tree('Palo Alto'))

    usa.add_child(newjersey)
    usa.add_child(california)

    rootNode.add_child(usa)

    rootNode.printTree()