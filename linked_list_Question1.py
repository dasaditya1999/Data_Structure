class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            node.next = self.head
            self.head = node 
    
    def insert_at_end(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            itr = self.head
            while itr:
                itr = itr.next
            node = Node(data)
            itr = node

    def insert_values(self,list):
        for i in list:
            self.insert_at_end(i)
        return

    def insert_at_any(self,data,index):
        if index<0 or index > self.ll_length():
            print('Invalid Index Position')
            return
        
        elif index == 0:
            self.insert_at_beginning(data)
            return

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data)
                    node.next = itr.next
                    itr.next = node
                count = count + 1
                itr = itr.next

    def insert_after_value(self,value,data):
        isValuePresent = False
        itr = self.head

        while itr:
            if itr.data == value:
                isValuePresent = True
                node = Node(data)
                node.next = itr.next
                itr.next = node
                return
            itr = itr.next
        if isValuePresent == False:
            print('The entered value does not exists.')
            return

    def remove_by_value(self, value):
        isValuePresent = False

        # If the length of the linkedlist is 1, set the head to None.
        if self.ll_length() == 1 and self.head.data == value:
            isValuePresent = True
            self.head = None
            return
        
        elif self.head.data == value:
            isValuePresent = True
            self.head = self.head.next
            return
        
        else:
            itr = self.head
            while itr:
                if itr.next.data == value:
                    isValuePresent = True
                    itr.next = itr.next.next
                itr = itr.next
                if itr.next.next == None:
                    if itr.next.data == value:
                        isValuePresent = True
                        itr.next = None
                    if isValuePresent == False:
                        print(f'The value {value} you are trying to remove is not present')
                    return
                
    def ll_length(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        # print(f'The length of the linkedlist is {length}')
        return length

    def print_ll(self):
        if self.head == None:
            print('The linked list is empty')
            return
        else:
            itr = self.head
            while itr:
                print(itr.data, end='>')
                itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_ll()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_ll()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_ll()
    ll.remove_by_value("figs")
    ll.print_ll()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_ll()

    # ll = LinkedList()
    # ll.insert_at_beginning(10)
    # ll.insert_at_beginning(12)
    # ll.insert_at_beginning(9)
    # ll.insert_at_beginning(72)

    # ll.insert_at_any(455,0)
    # ll.insert_at_any(99,1)
    # ll.insert_at_any(999,1)
    # ll.insert_at_any(2000,-1)
    # ll.insert_at_any(5,100)

    # ll.insert_after_value(18599,455)
    # ll.insert_after_value(2002,2000)
    # ll.insert_after_value(199,-10)

    # ll.print_ll()
    # print()

    # ll.remove_by_value(10)
    # ll.remove_by_value(455)
    # ll.remove_by_value(700)
    # ll.remove_by_value(1111)

    # ll.ll_length()

    # ll.print_ll()