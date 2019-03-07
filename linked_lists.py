# linked_lists.py
"""Volume 2: Linked Lists.
Jake Callahan
2018/09/27

Basic demonstration of linked list data structures
"""

class Node:
    """A basic node class for storing data."""
    def __init__(self, data):
        """Store the data in the value attribute. Only accept int, str, or float."""
        if type(data) != str and type(data) != float and type(data) != int:
            raise TypeError("Data must be int, str, or float")
        self.value = data


class LinkedListNode(Node):
    """A node class for doubly linked lists. Inherits from the Node class.
    Contains references to the next and previous nodes in the linked list.
    """
    def __init__(self, data):
        """Store the data in the value attribute and initialize
        attributes for the next and previous nodes in the list.
        """
        Node.__init__(self, data)       # Use inheritance to set self.value.
        self.next = None                # Reference to the next node.
        self.prev = None                # Reference to the previous node.


class LinkedList:
    """Doubly linked list data structure class.

    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
        size (int):            the size of the list.
    """
    def __init__(self):
        """Initialize the head and tail attributes by setting
        them to None, since the list is empty initially.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """Append a new node containing the data to the end of the list."""
        # Create a new node to store the input data.
        new_node = LinkedListNode(data)
        if self.head is None:
            # If the list is empty, assign the head and tail attributes to
            # new_node, since it becomes the first and last node in the list.
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, place new_node after the tail.
            self.tail.next = new_node               # tail --> new_node
            new_node.prev = self.tail               # tail <-- new_node
            # Now the last node in the list is new_node, so reassign the tail.
            self.tail = new_node
        self.size += 1                              # Update size of linked list

    def find(self, data):
        """Return the first node in the list containing the data.

        Parameters:
            data (int): Desired data to find

        Raises:
            ValueError: if the list does not contain the data.

        Examples:
            >>> l = LinkedList()
            >>> for x in ['a', 'b', 'c', 'd', 'e']:
            ...     l.append(x)
            ...
            >>> node = l.find('b')
            >>> node.value
            'b'
            >>> l.find('f')
            ValueError: <message>
        """
        node_found = False                          # Set initial conditions
        current_node = self.head                    # Set initial position
        for n in range(self.size):
            # Iterate through every node and check if the data is stored at
            # that node
            if current_node.value == data:
                node_found = True                   # Record that the data is found
                return current_node                 # Return desired node
                break                               # Exit the loop
            else:
                current_node = current_node.next    # Move to the next node
                n += 1                              # Update index

        if node_found is False:                     # Raise error if data does not exist
            raise ValueError("Data not found!")

    def get(self, i):
        """Return the i-th node in the list.

        Parameters:
            i (int): Position of desired node.

        Raises:
            IndexError: if i is negative or greater than or equal to the
                current number of nodes.

        Examples:
            >>> l = LinkedList()
            >>> for x in ['a', 'b', 'c', 'd', 'e']:
            ...     l.append(x)
            ...
            >>> node = l.get(3)
            >>> node.value
            'd'
            >>> l.get(5)
            IndexError: <message>
        """
        if i >= self.size:
            raise IndexError("i is out of range!")  # Check for input error
        current_node = self.head                    # Set initial node
        for n in range(i):
            # Iterate through the nodes until position i is reached
            current_node = current_node.next
            n += 1                                  # Update index
        return current_node                         # Return desired node

    def __len__(self):
        """Return the number of nodes in the list.

        Examples:
            >>> l = LinkedList()
            >>> for i in (1, 3, 5):
            ...     l.append(i)
            ...
            >>> len(l)
            3
            >>> l.append(7)
            >>> len(l)
            4
        """
        return self.size                            # Return the size of the list

    # Problem 3
    def __str__(self):
        """String representation: the same as a standard Python list.

        Examples:
            >>> l1 = LinkedList()       |   >>> l2 = LinkedList()
            >>> for i in [1,3,5]:       |   >>> for i in ['a','b',"c"]:
            ...     l1.append(i)        |   ...     l2.append(i)
            ...                         |   ...
            >>> print(l1)               |   >>> print(l2)
            [1, 3, 5]                   |   ['a', 'b', 'c']
        """
        # Print '[]' when list is empty
        if self.size == 0:
            ostring = "[]"
            return ostring

        else:
            current_node = self.head                    # Set intial node

            ostring = '['                               # Begin creating string
            for n in range(self.size - 1):
                # For each node, add that node's value to the string in the correct
                # formatting
                if type(current_node.value) == str:     # Format for strings
                    ostring += repr(current_node.value) + ', '
                else:                                   # Format for ints
                    ostring += str(current_node.value) + ', '
                current_node = current_node.next

            # Add the final value to the string and close the brackets
            if type(current_node.value) == str:
                ostring += repr(current_node.value) + ']'
            else:
                ostring += str(current_node.value) + ']'

            return ostring

    def remove(self, data):
        """Remove the first node in the list containing the data.

        Raises:
            ValueError: if the list is empty or does not contain the data.

        Examples:
            >>> print(l1)               |   >>> print(l2)
            ['a', 'e', 'i', 'o', 'u']   |   [2, 4, 6, 8]
            >>> l1.remove('i')          |   >>> l2.remove(10)
            >>> l1.remove('a')          |   ValueError: <message>
            >>> l1.remove('u')          |   >>> l3 = LinkedList()
            >>> print(l1)               |   >>> l3.remove(10)
            ['e', 'o']                  |   ValueError: <message>
        """

        delete_node = self.find(data)               # Set node to delete

        delete_node.next.prev, delete_node.prev.next = delete_node.prev, delete_node.next   # Link prev node and next node

    def insert(self, index, data):
        """Insert a node containing data into the list immediately before the
        node at the index-th location.

        Raises:
            IndexError: if index is negative or strictly greater than the
                current number of nodes.

        Examples:
            >>> print(l1)               |   >>> len(l2)
            ['b']                       |   5
            >>> l1.insert(0, 'a')       |   >>> l2.insert(6, 'z')
            >>> print(l1)               |   IndexError: <message>
            ['a', 'b']                  |
            >>> l1.insert(2, 'd')       |   >>> l3 = LinkedList()
            >>> print(l1)               |   >>> l3.insert(1, 'a')
            ['a', 'b', 'd']             |   IndexError: <message>
            >>> l1.insert(2, 'c')       |
            >>> print(l1)               |
            ['a', 'b', 'c', 'd']        |
        """
        # Check that index is in range
        if index < 0 or index > self.size - 1:
            raise IndexError("Index must be in range of list!")

        # Set node to append and node to append it before
        add_node = LinkedListNode(data)
        next_node = self.get(index)

        # Inserting at the head
        if index == 0:
            next_node.prev = add_node               # Insert add_node in the list
            add_node.next = next_node               # Link add_node to next_node
            self.head = add_node                    # Reassign the head
        # Inserting anywhere else
        else:
            prev_node = self.get(index - 1)         # Set previous node
            prev_node.next = add_node               # Forward link prev_node to add_node
            next_node.prev = add_node               # Back link next_node to add_node
            add_node.prev = prev_node               # Forward link add node to next_node
            add_node.next = next_node               # Back link add node to prev_node

        self.size +=1

class Deque(LinkedList):
    """Doubly linked list data structure class inherited from LinkedList, only
    allows additions or removals at either end of the list.

    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
        size (int):            the size of the list.
    """
    def __int__(self, data):
        # Set initial values
        self.head = None
        self.tail = None
        self.size = 0

    def appendleft(self, data):
        """Append a new node containing the data to the beginning of the list.
        Parameters:
        data (int, string, or float): Data to add to the list
        """
        add_node = LinkedListNode(data)             # Create node to append
        add_node.next = self.head                   # Reassign head to add_node
        self.head.prev = add_node                   # Link next element to new head
        self.head = add_node                        # Link new head to next element

        self.size +=1                               # Update size index

    def pop(self):
        """Removes the last node from the list and returns its value."""
        #Check to ensure pop is possible
        if self.size == 0:
            raise ValueError("The list is empty!")
        #Pop for deques of one node
        elif self.size == 1:                        # Check size
            old_last = self.get(0)                  # Store head of deque
            self.head = None                        # Delete head from deque
            self.size -= 1                          # Update size index
            return old_last.value                   # Return value of head
        #Pop for deques of all other size
        else:
            old_last = self.get(self.size -1)       # Store final node of deque
            new_last = old_last.prev                # Set new tail
            new_last.next = None                    # Delete old tail from deque
            self.size -= 1                          # Update size index
            return old_last.value                   # Return value of old tail

    def popleft(self):
        """Removes the first node from the list and returns its value."""
        # Check to ensure pop is possible
        if self.size == 0:
            raise ValueError("The list is empty!")
        # popleft() for deques of one node
        elif self.size == 1:                        # Check size
            old_first = self.get(0)                 # Store old head
            self.head = None                        # Delete head from deque
            self.size -= 1                          # Update size index
            return old_first.value                  # Return value of old head
        # popleft() for deques of all other size
        else:
            old_first = self.head                   # Store value of old head
            new_first = self.get(1)                 # Get node for new head
            new_first.prev = None                   # Delete old head
            self.head = new_first                   # Reassign head
            self.size -= 1                          # Update size index
            return old_first.value                  # Return value of old head

    def remove(*args, **kwargs):
        """Overwrites LinkedList.remove() and prevents it from being used..."""
        raise NotImplementedError("Use pop() or popleft() for removal")
    def insert(*args, **kwargs):
        """Overwrites LinkedList.insert() and prevents it from being used."""
        raise NotImplementedError("Use append() or appendleft() to add data")

def reverse_file(infile, outfile):
    """Reverse the contents of a file by line and write the results to
    another file.

    Parameters:
        infile (str): the file to read from.
        outfile (str): the file to write to.
    """

    with open(infile, 'r') as infile:               # Open file to read
        incontents = infile.readlines()             # Read lines into a list

    outcontents = Deque()                           # Create a deque for writing
    for n in incontents:
        outcontents.append(n)                       # Append lines of file into deque

    with open(outfile, 'w') as outfile:             # Open file to write
        ostring = ""
        for n in range(len(incontents)):
            writeline = incontents.pop()
            if n == 0:
                if writeline[len(writeline) - 1] != "\n":
                    writeline += "\n"
            ostring += writeline
            outfile.write(writeline)
