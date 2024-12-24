class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self._length = 0   
 
    def append(self, data):
        newNode = Node(data) 
        self.start = newNode
        self.end = newNode 
        self._length += 1     
 
    def len(self):
        return self._length 
  
 
ll = LinkedList() 
ll.append(30) 
ll.append(40) 
ll.append('jovid')  
ll.append('bla bla bla bla la lalalla')  

print("Длина списка:", ll.len())    
