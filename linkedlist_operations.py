class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add_elements_beginning(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def add_at_any(self,data,index):
        if index == 0:
            self.add_elements_beginning(data)
            return
        else:
            count = 0
            itr = self.head

            while itr:
                if count == index - 1:
                    node = Node(data)
                    node.next = itr.next
                    itr.next = node
                    return
                itr = itr.next
                count = count + 1

    def remove_duplicate(self):
        itr = self.head

        while itr:
            if itr.next == None:
                break
            if itr.data == itr.next.data:
                itr.next = itr.next.next
                continue
            itr = itr.next

    def checkCircularity(self):
        itr = self.head
        listOfNodes = []
        while itr:
            if itr.next in listOfNodes:
                print('Hurrah!! Circular Linked List')
            listOfNodes.append(itr)
            itr = itr.next
        print(listOfNodes)
    
    def reverseLinkedList(self):
        # print('Reversed Linkedlist')
        prev = None
        counter = 0
        itr = self.head
        while itr:
            if counter == 0:
                temp_address = itr.next
                itr.next = prev
                prev = itr
                counter = counter + 1
            else:
                temp_address = itr.next
                itr.next = prev
                prev = itr

            if temp_address == None:
                self.head = itr
                break
            itr = temp_address
        
        return self
    
    def reverseLinkedListv2(self, itr):
        address = None
        while itr:
            data = itr.data
            node = Node(data, address)
            address = node
            itr = itr.next
            if itr == None:
                self.head = node

        return self

    def checkPalindrome(self):

        ## let's Reverse the LinkedList First & store the reversed linkedlist in a new linkedlist
        revll = Linkedlist()

        itr = self.head

        rev = revll.reverseLinkedListv2(itr)

        itr2 = rev.head

        ''' Now we have the reversed linkedlist. 
        Let's now check if the linkedlist is palindrom or not by comparing the original
        and the reversed one'''

        palindromeChecker = True
        while itr and itr2:
            if itr.data != itr2.data:
                palindromeChecker = False
                break
            itr = itr.next
            itr2 = itr2.next

        if palindromeChecker:
            print('Palindrome')
        else:
            print('Not palindrome')
            

    def print_ll(self):
        itr = self.head
        # print('Old Linkedlist')
        while itr:
            print(itr.data, itr.next, end='--->')
            itr = itr.next

if __name__ == '__main__':
    ll = Linkedlist()

    # ll.add_elements_beginning(124)
    # ll.add_elements_beginning(124)
    # ll.add_elements_beginning(121)
    # ll.add_elements_beginning(121)
    # ll.add_elements_beginning(118)
    # ll.add_elements_beginning(118)
    # ll.add_elements_beginning(117)
    # ll.add_elements_beginning(117)

    # print('Old LinkedList')
    # ll.print_ll()

    # ll = ll.reverseLinkedList()

    # print()
    # print('New LinkedList')
    # ll.print_ll()

    # print('before removing the duplicate')
    # ll.print_ll()
    # print('after removing the duplicate')
    # ll.remove_duplicate()
    # ll.print_ll()

    # ll.checkCircularity()

    ll.add_elements_beginning(1)
    ll.add_elements_beginning(2)
    ll.add_elements_beginning(118)
    ll.add_elements_beginning(2)
    ll.add_elements_beginning(1)

    # ll.print_ll()

    ll.checkPalindrome()
