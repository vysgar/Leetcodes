class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.head = Node(7)
second = Node(10)
third = Node(15)
llist.head.next = second
second.next = third
llist.printlist()