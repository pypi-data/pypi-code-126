class LinkedList:
    """A base class for singly and doubly linked lists
    """
    def __init__(self) -> None:
        """The init function
        """
        self.head = None

        self._size = 0
        
    def peek(self) -> int:
        """Peek the head value of the linked lsit

        Returns:
            int: the value of the head
        """
        return self.head.data
    
    def __len__(self) -> int:
        """Gets the size of the linked list

        Returns:
            int: the size of the linked list
        """
        return self._size
    
    def contains(self, data: int) -> bool:
        """Tests if the linked list contains data

        Args:
            data (int): the data to find in the list

        Returns:
            bool: if the data is contained in the list
        """
        # If the list is empty
        if self.head is None:
            return

        # If data from head is equal to data, return True
        if self.head.data == data:
            return True

        # Loop over all the items in the linked list
        current = self.head
        while current is not None:
            # Return true if the current's data is equal to the to search data
            if current.data == data:
                return True
            
            current = current.next
        
        # Return false if it doesn't contain
        return False
    
    
    def print_items(self):
        """Print the list
        """
        if self.head is None:
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")

            current = current.next
        
        print()