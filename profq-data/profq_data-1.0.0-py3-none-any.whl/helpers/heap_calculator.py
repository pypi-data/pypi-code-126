class HeapCalculator:
    """A helper class for the heap to calculate indeces
    """
    def __init__(self, heap) -> None:
        """The init function
        """
        self.heap = heap

    def get_left_child_index(self, parent_index: int) -> int:
        """Get the left child index of a parent index

        Args:
            parent_index (int): the parent index

        Returns:
            int: the index of the left child
        """
        return 2 * parent_index + 1
    
    def get_right_child_index(self, parent_index: int) -> int:
        """Get the right child index of a parent index

        Args:
            parent_index (int): the parent index

        Returns:
            int: the index of the right child
        """
        return 2 * parent_index + 2
    
    def get_parent_index(self, child_index: int) -> int:
        """Get the parent index of a child index

        Args:
            child_index (int): the child index

        Returns:
            int: the index of the parent
        """
        return (child_index - 1) // 2
    
    def has_left_child(self, parent_index: int) -> bool:
        """Check if a parent index has a left child

        Args:
            parent_index (int): the parent index

        Returns:
            bool: whether the parent has a left child
        """
        return self.get_left_child_index(parent_index) < len(self.heap)
    
    def has_right_child(self, parent_index: int) -> bool:
        """Check if a parent index has a right child

        Args:
            parent_index (int): the parent index

        Returns:
            bool: whether the parent has a right child
        """
        return self.get_right_child_index(parent_index) < len(self.heap)
    
    def has_parent(self, child_index: int) -> bool:
        """Check if a child index has a parent

        Args:
            child_index (int): the child index

        Returns:
            bool: whether the child has a parent
        """
        return self.get_parent_index(child_index) >= 0
    
    def get_left_child(self, parent_index: int) -> int:
        """Get the left child of a parent index

        Args:
            parent_index (int): the parent index

        Returns:
            int: the left child
        """
        return self.heap[self.get_left_child_index(parent_index)]
    
    def get_right_child(self, parent_index: int) -> int:
        """Get the right child of a parent index

        Args:
            parent_index (int): the parent index

        Returns:
            int: the right child
        """
        return self.heap[self.get_right_child_index(parent_index)]
    
    def get_parent(self, child_index: int) -> int:
        """Get the parent of a child index

        Args:
            child_index (int): the child index

        Returns:
            int: the parent
        """
        return self.heap[self.get_parent_index(child_index)]
    

