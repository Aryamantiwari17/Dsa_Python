class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    
    def append(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        
        last=self.head
        while last.next:
           last= last.next
        last.next=node
        node.prev=last


    def traverse_forward(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        print()



    def traverse_backward(self):
        current=self.head
        if not current:
            return
        while current.next:
            current=current.next
        while current :
            print(current.data,end=" ")
            current=current.prev
        print()


# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Forward traversal:")
dll.traverse_forward()

print("Back traversal:")
dll.traverse_backward()
