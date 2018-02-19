class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = Node()

    def add_node(self, data):
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node(data)

    def remove_node(self, data):
        current_node = self.head
        while current_node.next_node is not None:
            last_node = current_node
            current_node = current_node.next_node
            if current_node.data == data:
                last_node.next_node = current_node.next_node
                return

    def display_node_data(self):
        items = []
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
            items.append(current_node.data)
        print(items)

if __name__ == '__main__':
    x = LinkedList()
    x.add_node(10)
    x.add_node(11)
    x.add_node(12)
    x.add_node(13)
    x.add_node(14)
    x.add_node(15)
    x.display_node_data()
    x.remove_node(13)
    x.display_node_data()
