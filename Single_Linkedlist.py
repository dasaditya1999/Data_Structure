class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

class Linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def length_linklist(self):
        itr = self.head
        
        count = 0
        
        while itr:
            count += 1
            itr = itr.nxt
        return count
    
    def print_linklist(self):
        
        if self.head == None:
            print('list is empty because the head is', self.head)
            return
        
        itr = self.head
        while itr:
            print(itr.data, end='')
            if itr.nxt != None:
                print('-->', end='')
            itr = itr.nxt
        print()
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)

        self.head = node
        if self.head.nxt == None:
            self.tail = self.head
        else:
            itr = self.head
            
            while itr:
                itr = itr.nxt
                if itr.nxt == None:
                    break
            self.tail = itr
        
    def insert_at_end(self, position, data):
        node = Node(data, nxt = None)
        
        itr_var = 0
        itr = self.head
        
        while itr:
            itr_var += 1
            if itr_var == position:
                break
            itr = itr.nxt
        #previous node next = node
        itr.nxt = node
        self.tail = node
        
    def insert_at_any(self, data, position):
        
        length = linklist.length_linklist()
        
        if position == 0:
            self.insert_at_begining(data)
            
        elif position == length:
            self.insert_at_end(position, data)
            
        else:
            itr = self.head
            pos = 0
            
            # print('itr head value', itr)
            # itr_node1 = itr.nxt
            # print('itr node1 nxt value or node2 address', itr.nxt)
            # itr_node2 = itr_node1.nxt
            # print('itr node2 nxt value or node3 address', itr_node2)
            
            while itr:
                if pos == position-1:
                    temp_node_after_new_node = itr.nxt
                    break
                pos = pos + 1
                itr = itr.nxt
                
            node = Node(data, itr.nxt.nxt)
            node.nxt = temp_node_after_new_node
            itr.nxt = node
        
    def delete_at_beginning(self):
        print('Deleting head node....')
        self.head = self.head.nxt
        return
    
    def delete_at_end(self):
        itr = self.head
        while itr:
            if itr.nxt.nxt == None:
                itr.nxt = None
                return
            itr = itr.nxt
    
    def delete_at_any(self, position):
        length_ll = self.length_linklist()-1
        
        if position == 0:
            self.delete_at_beginning()
            
        elif position == length_ll:
            self.delete_at_end()
            
        else:
            pos = 0
            itr = self.head
            temp_address = 0
            
            while itr:
                if pos == position-1:
                    itr.nxt = itr.nxt.nxt
                    return
                pos = pos + 1
                itr = itr.nxt
            
    
    def delete_particular_element(self, del_data):
        
        ##################### First stage of Code ##################
        
        # Deleting the head
        itr_var1 = self.head
        while itr_var1:
            
            if itr_var1.data == del_data and itr_var1 is self.head:
                print('deleting the head element.....')
                self.head = itr_var1.nxt
            itr_var1 = itr_var1.nxt
        
        
        # Deleting the tail
        itr_var2 = self.head
        pos_count = 0
        while itr_var2:
            if del_data == itr_var2.data and itr_var2.nxt == None:
                print('deleting the end/tail element.....')
                self.delete_at_end(pos_count)
            
            pos_count = pos_count + 1
            itr_var2 = itr_var2.nxt
            
            
        Deleting in the middle
        itr_var3 = self.head
        temp_address = 0
        while itr_var3:
            if itr_var3.nxt.data == del_data:
                print('deleting from the middle.....')
                temp_address = itr_var3.nxt.nxt
                itr_var3.nxt = temp_address
                return
            itr_var3 = itr_var3.nxt
            
            
        ################# All in one code for deletion ####################
            
        # condition to delete the head node
        if self.head.data == del_data:
            print('Deleting head node....')
            self.head = self.head.nxt
            return
            
        # Condition to delete the tail node
        elif self.tail.data == del_data and self.tail.nxt == None:
            print('Deleting tail node.....')
            itr_var2 = self.head
            while itr_var2:
                if itr_var2.nxt.data == del_data:
                    itr_var2.nxt = None
                    return
                itr_var2 = itr_var2.nxt

        # Condition to delete the middle node
        else:
            itr_var3 = self.head
            temp_address = 0
            while itr_var3:
                if itr_var3.nxt.data == del_data:
                    print('Deleting any middle Node.....')
                    temp_address = itr_var3.nxt.nxt
                    itr_var3.nxt = temp_address
                    return
                itr_var3 = itr_var3.nxt
    
    # Sorting the linkedlist
    def sort_linklist(self):
        itr = self.head
        
        while itr:
            nested_itr = self.head
            while nested_itr:
                if itr.data < nested_itr.data:
                    # swap data
                    temp = itr.data
                    itr.data = nested_itr.data
                    nested_itr.data = temp
                    
                nested_itr = nested_itr.nxt
            itr = itr.nxt
            

            
############ Driving Code ################

linklist = Linkedlist()

# Inserting elements in the begining & making the linkedlist
linklist.insert_at_begining(1223)
linklist.insert_at_begining(6666)
linklist.insert_at_begining(5555)
linklist.insert_at_begining(4444)

linklist.insert_at_any(9999, 0)
linklist.insert_at_any(789123, 3)
linklist.insert_at_any(18599, 1)
linklist.insert_at_any(10586, 0)

linklist.print_linklist()

linklist.sort_linklist()
print("after sorting")
linklist.print_linklist()

# linklist.delete_particular_element(10586)
# linklist.delete_particular_element(1223)
# linklist.delete_particular_element(4444)
# linklist.print_linklist()
# 9999-->18599-->5555-->789123-->6666

# linklist.delete_at_any(position = 0)
# linklist.print_linklist()

# linklist.delete_at_any(position = 2)
# linklist.print_linklist()