#Nodes implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Queue implementation
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Empty queue.")
        else:
            item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return item

    def is_empty(self):
        return self.front is None

    def print(self):
        if self.front is None:
            print("Empty queue.")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

#Linked list implementation
class linkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def pushback(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def pushfront(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def popback(self):
        if self.tail is None:
            print("Empty list.")
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            temp = current_node.data
            current_node.next = None
            self.tail = current_node
            return temp

    def print(self):
        if self.head is None:
            raise IndexError("Empty list.")
        else:
            current_node = self.head
            print('[', end='')
            while current_node is not None:
                if current_node.next is None:
                    print(current_node.data,end=']')
                else:
                    print(current_node.data, end=" ")
                current_node = current_node.next

cases = int(input())

for l in range(cases):
    
    quantity = int(input())
    items = Queue()
    temp = input().split()
    items_store = []

    for i in temp:
        items.enqueue(i)

    stores = int(input())
    store_quantity = input().split()

    for i in store_quantity:
        items_list = linkedList()
        for i in range(int(i)):
            try:
                items_list.pushback(items.dequeue())
            except:
                break
        items_store = items_store + [items_list]
    
    for j in items_store:
        if items_store.index(j) == len(items_store)-1:
            try:
                j.print()
            except:
                print("[]", end="")
        else:
            try:
                j.print()
                print()
            except:
                print("[]")

    if l  != cases-1:
        print()
    
