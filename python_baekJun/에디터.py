class Node():
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DLinkedList():
    def __init__(self, pre_node, data, next_node):
        self.pre_node = pre_node
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def previouse(self):
        return self.pre_node
    
    def next(self):
        return self.next_node
    
