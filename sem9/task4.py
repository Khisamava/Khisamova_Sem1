class Box:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None



class LinkedList:
    def __init__(self):
        self.start = None

    def insert_in_empty(self, value):
        if self.start is None:
            new_node = Box(value)
            self.start = new_node
        else:
            print("list is not empty")

    def insert_begin(self, value):
        if self.start is None:
            new_node = Box(value)
            self.start = new_node
            return
        new_node = Box(value)
        new_node.next = self.start
        self.start.previous = new_node
        self.start = new_node

    def insert_end(self, value):
        if self.start is None:
            new_node = Box(value)
            self.start = new_node
            return
        n = self.start
        while n.next is not None:
            n = n.next
        new_node = Box(value)
        n.next = new_node
        new_node.previous = n

    def insert_after(self, x, value):
        if self.start is None:
            print("List is empty))")
            return
        else:
            n = self.start
            while n is not None:
                if n.value == x:
                    break
                n = n.next
                if n is None:
                    print("Value is not in the list")
                else:
                    new_node = Box(value)
                    new_node.previous = n
                    new_node.next = n.next
                    if n.next is not None:
                        n.next.prev = new_node
                    n.next = new_node

    def insert_before(self, x, value):
        if self.start is None:
            print("List is empty")
            return
        else:
            n = self.start
            while n is not None:
                if n.value == x:
                    break
                n = n.next
            if n is None:
                print("Value is not in the list")
            else:
                new_node = Box(value)
                new_node.next = n
                new_node.previous = n.previous
                if n.previous is not None:
                    n.previous.next = new_node
                n.previous = new_node

    def delete_element(self, x):
        if self.start is None:
            print("List is empty")
            return
        if self.start.next is None:
            if self.start.value == x:
                self.start = None
            else:
                print("Value not found")
            return
        if self.start.value == x:
            self.start.previous = None
            return
        n = self.start
        while n.next is not None:
            if n.value == x:
                break;
            n = n.next
        if n.next is not None:
            n.previous.next = n.next
            n.next.prev = n.previous
        else:
            if n.value == x:
                n.previous.next = None
            else:
                print("Value not found")

    def see_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            n = self.start
            while n is not None:
                print(n.value, " ")
                n = n.next



linked_list = LinkedList()
linked_list.insert_in_empty(70)
linked_list.insert_begin(10)
linked_list.insert_end(40)
linked_list.insert_before(40, 6)
linked_list.insert_after(70, 44)
linked_list.delete_element(10)
linked_list.see_list()
