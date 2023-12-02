class Heap:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self):
        self.__left = None
        self.__right = None
        self.__value = None

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        nodes_list = []
        if self.__left:
            nodes_list.append(self.__left)
        if self.__right:
            nodes_list.append(self.__right)
        while self.__left:
            print(self.__left)
        while self.__right:
            print(self.__right)
        if not self.__left and not self.__right:
            print(self.__value)



    def get_value(self):
        return self.__value

    def get_child(self, side = 'left'):
        if side == 'left':
            return self.__left
        elif side == 'right':
            return self.__right
        else:
            return ValueError

    def set_child(self, node, side='left'):
        if side == 'left':
            self.__left = node
            return
        elif side == 'right':
            self.__right = node
        else:
            return ValueError


first_node = Node(5)
second_node = Node(4)
third_node = Node(3, left=first_node, right=second_node)
right = second_node
cinco_node = Node(2)
quatro_node = Node(1, left=third_node, right=cinco_node)
print(quatro_node)

