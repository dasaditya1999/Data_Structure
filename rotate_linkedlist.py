class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def rotatelinkedlist(self,rotation):
        for i in range(0,rotation):
            itr = self.head
            while itr:
                if itr.next.next == None:
                    lastNode = itr.next
                    itr.next = None
                    lastNode.next = self.head
                    self.head = lastNode
                itr = itr.next
        return self

    def printlinkedlist(self):
        itr = self.head
        while itr:
            print(itr.value)
            itr = itr.next

#Driver Code
if __name__=='__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(4)
    ll.insert_at_begining(3)
    ll.insert_at_begining(2)
    ll.insert_at_begining(1)
    

    print('Before rotating the linkedlist')
    ll.printlinkedlist()

    ll = ll.rotatelinkedlist(2)

    print('After Rotating the Linkedlist')
    ll.printlinkedlist()
    



