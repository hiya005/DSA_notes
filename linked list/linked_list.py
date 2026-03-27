# linkedlist.py

# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Stores the value
        self.next = None      # Pointer to the next node


# LinkedList class to handle operations
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, list is empty

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)        # Create new node
        new_node.next = self.head    # Point new node to current head
        self.head = new_node         # Update head

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:  # If list is empty
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:       # Traverse till last node
            temp = temp.next
        
        temp.next = new_node   # Link last node to new node

    # Insert at a specific position (0-based index)
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            self.insert_at_beginning(data)
            return

        temp = self.head
        for i in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None

    # Search for a value
    def search(self, key):
        temp = self.head
        position = 0

        while temp:
            if temp.data == key:
                return position
            temp = temp.next
            position += 1

        return -1  # Not found

    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(20)
    ll.insert_at_position(15, 2)

    print("Linked List:")
    ll.display()

    print("Position of 15:", ll.search(15))

    ll.delete(10)
    print("After deleting 10:")
    ll.display()