class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data) 
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
        
    def insert_value(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count    
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(data)
                new_node.next = itr.next
                itr.next = new_node
                break
            itr = itr.next
            count += 1
        
    def print_list(self):
        if self.head is None:
            print("Its an empty list.")
            return
            
        itr = self.head
        while itr:
            print(itr.data, end=" ---> ")
            itr = itr.next
        print("None")
            
new_list = LinkedList()
new_list.insert_at_beginning(16)
new_list.insert_at_end(45)
new_list.insert_at_beginning(75)
new_list.insert_value(["Mango", "Orange"])
new_list.remove_at(4)
new_list.insert_at(1, 26)
new_list.print_list()
print(f"length: {new_list.get_length()}")
