import sys
class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.arr = [None for i in range(0,self.Max)]
    
    def get_Hash(self,key):
        ascii = 0
        for i in key:
            ascii = ascii + ord(i)
        memory_pos = ascii%10 ## Hashing Technique i.e. Modulo Hashing
        return memory_pos

    def setItem(self,key,value):
        memory_pos = self.get_Hash(key)
        self.arr[memory_pos] = value
    
    def __setitem__(self,key,value):
        memory_pos = self.get_Hash(key)
        self.arr[memory_pos] = value

    def getItem(self,key):
        memory_pos = self.get_Hash(key)
        if self.arr[memory_pos] == None:
            print('No key is present with this name')
        else:
            print(self.arr[memory_pos])
    
    def __getitem__(self,key):
        memory_pos = self.get_Hash(key)
        return self.arr[memory_pos]

## Driver Code ##
if __name__ == '__main__':
    ht = HashTable()
    ht.setItem('aditya', 20)
    ht.setItem('harris', 76)
    ht.setItem('lucas', 65)

    ht.getItem('lucas')
    ht.getItem('harris')
    ht.getItem('Das')
    
    ht['abc'] = 100
    print('value',ht['abc'])

    # print(sys.getsizeof(ht.arr))