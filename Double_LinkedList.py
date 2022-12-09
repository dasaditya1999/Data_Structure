class Node:
    def __init__(self, prev=None, data=None, nxt=None):
        self.prev = prev
        self.data = data
        self.nxt = nxt

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def length_of_dll(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.nxt
        return count
    
    def print_doubly_linkedlist(self):
        print("Displaying the doubly linkedlist from the head")
        itr = self.head
        while itr:
            # print('| ', itr.prev, ' | ', itr.data, ' | ', itr.nxt, ' | ', '<----->', end = '')
            print(itr.data, "--->", end = '')
            itr = itr.nxt
        print()
        
    def print_doubly_linkedlist_from_tail(self):
        print("Displaying the doubly linkedlist from the tail")
        itr = self.tail
        while itr:
            print(itr.data, '<---->', end = '')
            itr = itr.prev
        print('\n')
        
    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(prev = None, data=data, nxt=None)
            self.head = node
            return
        node = Node(prev = None, data = data, nxt = None)
        node.nxt = self.head
        self.head.prev = node
        self.head = node
        
    def insert_at_end(self, data):
        itr = self.head
        
        while itr:
            if itr.nxt == None:
                break
            itr = itr.nxt
        node = Node(prev = itr, data=data, nxt=None)
        itr.nxt = node
        node.prev = itr
        self.tail = node
        
    def insert_at_any(self, data, index_pos):
        
        # finding the length of doubly linkedlist
        len_doubly_ll = self.length_of_dll()
        
        # for the first position entry
        if index_pos == 0:
            # print('Entering element at the beeginning')
            self.insert_at_begining(data)
            return
        
        # For the last position entry
        elif index_pos == len_doubly_ll-1:
            # print('Entering element at the end')
            self.insert_at_end(data)
        
        # Entry at any middle position of 
        else:
            # print('Entering element to the middle of dll')
            counter1 = 0
            index_pos = index_pos - 1
            itr = self.head
            while itr:
                if index_pos == counter1:
                    break
                counter1 = counter1 + 1
                itr = itr.nxt
            node = Node(prev = itr, data = data, nxt = itr.nxt)
            itr.nxt.prev = node
            itr.nxt = node
            
    def delete_at_beginning(self):
        self.head = self.head.nxt
        self.head.prev = None
        
    def delete_at_end(self):
        self.tail.prev.nxt = None
        self.tail = self.tail.prev
        
    def delete_at_any(self, position):
        # Finding the length of the linkedlist
        len_doubly_ll = self.length_of_dll()
        
        # Deleting at the beginning
        if position == 0:
            self.delete_at_beginning()
        
        # Deleting at the end
        elif position == len_doubly_ll-1:
            self.delete_at_end()
        
        # Deleting at any position
        else:
            counter2 = 0
            position = position - 1
            
            itr = self.head
            while itr:
                if position == counter2:
                    break
                counter2 += 1
                itr = itr.nxt
            itr.nxt = itr.nxt.nxt
            # itr.nxt.nxt.prev = itr
            itr.nxt.prev = itr
    
    # Bubble sorting of double linklist
    def sort_dll(self):
        itr1 = self.head
        while itr1:
            itr2 = self.head
            while itr2:
                temp_data = itr1.data
                if temp_data < itr2.data:
                    # swap
                    temp = itr2.data
                    itr2.data = itr1.data
                    itr1.data = temp
                itr2 = itr2.nxt
            itr1 = itr1.nxt
            
#################### Driving Code ###############
if __name__ == '__main__':
    dblinklst = DoublyLinkedList()
    dblinklst.insert_at_begining(12)
    dblinklst.insert_at_begining(94)
    dblinklst.insert_at_begining(167)

    dblinklst.insert_at_end(202)
    dblinklst.insert_at_end(303)
    dblinklst.insert_at_end(403)
    dblinklst.insert_at_end(505)

    dblinklst.insert_at_any(9999, 1)
    dblinklst.insert_at_any(8888, 4)
    # print('Linkedlist without deleting the element')
    # dblinklst.print_doubly_linkedlist()

    dblinklst.delete_at_beginning()
    dblinklst.delete_at_end()
    # print('Linkedlist after deleting two elements')
    # dblinklst.print_doubly_linkedlist()

    dblinklst.delete_at_any(3)
    # print('Linkedlist after deleting 3rd element')
    dblinklst.print_doubly_linkedlist()
    dblinklst.print_doubly_linkedlist_from_tail()

    # Sorting the doubly linkedlist
    dblinklst.sort_dll()
    print("Printing the Sorted Linkedlist")
    dblinklst.print_doubly_linkedlist()
    dblinklst.print_doubly_linkedlist_from_tail()