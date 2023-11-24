class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data)
        if self.head == None:
            ## That means the linkedlist is empty
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def reverseLinkedlist(self):
        rev = None
        itr = self.head
        next_node = self.head
        while itr:
            next_node = itr.next
            itr.next = rev
            rev = itr
            itr = next_node
            
            if itr == None:
                self.head = rev
                return self

    def printLinkedlist(self):
        itr = self.head
        while itr:
            print(itr.data, itr.next, end='-->')
            itr = itr.next
        print('None')


##Driver Code Goes Here###
if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(14)
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(18)

    ll.printLinkedlist()

    revll = ll.reverseLinkedlist()

    revll.printLinkedlist()