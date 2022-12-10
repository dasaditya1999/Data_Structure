class Node:
    
    # Constructore for initializing a Node
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt
        
class CircularLinkedlist:
    
    # Constructor for initializing linkedlist
    def __init__(self):
        self.head = None
    
    # Printing the circular linkedlist
    def print_circularll(self):
        itr = self.head
        print('head address', itr, '\n')
        while itr:
            print(itr.data, '|', itr.nxt, '--> ', end= '')
            itr = itr.nxt
            if itr == self.head:
                break
        print()
    
    # Length of circular linkedlist
    def length_circularll(self):
        itr = self.head
        length = 0
        while itr:
            length = length + 1
            itr = itr.nxt
            if itr == self.head or itr == None:
                return length
            
    # Inserting element at the beginning        
    def insert_element_beginning(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data, self.head)
            self.head = node
            itr = self.head
            node_addresses = []
            while itr:
                node_addresses.append(itr)
                if itr.nxt == None:
                    itr.nxt = self.head
                    return
                elif itr.nxt in node_addresses:
                    itr.nxt = self.head
                    return
                itr = itr.nxt
    
    # Inserting element at the end
    def insert_element_end(self, data):
        itr = self.head
        while itr:
            if itr.nxt == self.head:
                node = Node(data, self.head)
                itr.nxt = node
                return
            itr = itr.nxt
    
    # Inserting element at any position
    def insert_element_at_any(self, data, position):
        
        # Length of the circular linkedlist
        length_ll = self.length_circularll()
        
        if position == 0:
            self.insert_element_beginning(data)
        elif position == length_ll:
            self.insert_element_end(data)
        else:
            counter = 0
            stop_position =  position - 1
            
            itr = self.head
            
            while itr:
                if counter == stop_position:
                    break
                counter += 1
                itr = itr.nxt
            
            # Create a node
            node = Node(data, itr.nxt)
            itr.nxt = node
            
    # deleting element at the beginning
    def delete_element_beginning(self):
        node_addresses = []
        itr = self.head
        while itr:
            node_addresses.append(itr)
            if itr.nxt in node_addresses:
                break
            itr = itr.nxt
            
        temp_address = self.head.nxt
        self.head.nxt = None
        self.head = temp_address
        itr.nxt = self.head # Storing the new head node address in the tail node #
    
    # deleting element at the end
    def delete_element_end(self):
        itr = self.head
        
        while itr:
            if itr.nxt == None:
                self.head = None
            elif itr.nxt.nxt == self.head:
                itr.nxt.nxt = None
                itr.nxt = self.head
                return
            itr = itr.nxt
    
    # Deleting element at any position
    def delete_element_at_any(self, position):
        
        length_ll = self.length_circularll()
        
        if position == 0:
            self.delete_element_beginning()
            return
        elif position == length_ll - 1:
            self.delete_element_end()
        else:
            counter = 0
            itr = self.head
            while itr:
                if counter == position-1:
                    temp = itr.nxt.nxt
                    itr.nxt.nxt = None
                    itr.nxt = temp
                    return
                counter += 1
                itr = itr.nxt
                if itr == self.head:
                    break
                    
    # Checks if a linkedlist is a circular linkedlist                
    def is_ll_circularll(self):
        length_ll = self.length_circularll()
        itr = self.head
        i = 0
        circular_ll = 0
        while i < length_ll:
            if i == length_ll-1:
                if itr.nxt == self.head:
                    circular_ll = 1
                    print('It is a Circular Linkedlist')
                    return
            i = i + 1
            itr = itr.nxt
        if circular_ll == 0:
            print('Not a circular Linkedlist')
    
    
##################### Driving code######################## 
if __name__ == '__main__':
    circularll = CircularLinkedlist()
    circularll.insert_element_beginning(121)
    circularll.insert_element_beginning(122)
    circularll.insert_element_beginning(123)
    circularll.insert_element_beginning(124)
    circularll.insert_element_beginning(125)
    circularll.insert_element_beginning(126)
    circularll.insert_element_beginning(127)
    circularll.insert_element_end(120)
    circularll.insert_element_end(119)
    circularll.insert_element_end(118)
    circularll.insert_element_end(117)
    circularll.insert_element_end(116)
    circularll.insert_element_at_any(128, 0)
    circularll.insert_element_at_any(115, 13)
    print('Before deleting any elements')
    circularll.print_circularll()
    print('length of the circular linkedlist before deleting is:', circularll.length_circularll(), '\n') 
    # print('after deleting element', '\n')
    # circularll.delete_element_beginning()
    # circularll.delete_element_beginning()
    # circularll.delete_element_beginning()
    # circularll.delete_element_end()
    # circularll.delete_element_end()
    # circularll.delete_element_at_any(0)
    # circularll.delete_element_at_any(10)
    # circularll.print_circularll()
    # print('length of the circular linkedlist after deleting is:', circularll.length_circularll(), '\n') 
    circularll.is_ll_circularll()