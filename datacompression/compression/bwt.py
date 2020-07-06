import struct


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        if self.data == other.data:
            return self.next < other.next
        return self.data < other.data

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return self.__repr__()


class CircularLinkedList:

    def __init__(self, nodes=None):
        self.head = None
        self.len = 0

        if nodes is not None:
            node = Node(data=nodes[0])
            self.head = node
            self.len = len(nodes)

            for elem in nodes[1:]:
                node.next = Node(data=elem)
                node.next.next = self.head
                node.next.prev = node
                node = node.next
                self.head.prev = node

    def __iter__(self):
        node = self.head
        counter = 0

        while node is not None and counter < self.len:
            yield node
            node = node.next
            counter += 1

    def __len__(self):
        return self.len

    def __repr__(self):
        node = self.head
        nodes = []
        counter = 0

        while node is not None and counter < self.len:
            nodes.append(node.data)
            node = node.next
            counter += 1

        return str(bytes(nodes))

    def __str__(self):
        return self.__repr__()

    def first(self):
        return self.head

    def last(self):
        return self.head.prev

    def shiftr(self):
        self.head = self.head.next
        return self.head

    def shiftl(self):
        self.head = self.head.prev
        return self.head

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return

        for current_node in self:
            pass

        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception(f"Node with data '{target_node_data}' not found")


def bwt(data: bytes) -> bytes:
    """
    table = [(i, data[i], data[-1+i]) for i in range(len(data))]
    table = sorted(table, key=lambda x: x[1])
    index = table.index(next(x for x in table if x[0] == 0))
    last_column = [row[2] for row in table]
    return index, bytes(last_column)
    """
    cll = CircularLinkedList(data)
    table = [(i, cll.shiftr()) for i in range(len(cll))]
    table = sorted(table, key=lambda x: x[1])
    index = table.index(next(x for x in table if x[0] == 0))
    last_column = [row[1].prev.data for row in table]
    for b in struct.pack('>I', index):
        last_column.insert(0, b)
    return bytes(last_column)


def ibwt(last: bytes) -> bytes:
    index, = struct.unpack('<I', last[:4])
    last = last[4:]
    first = bytes(sorted(last))
    uncompressed = bytearray()

    # pylint: disable=unused-variable
    for i in range(len(last)):
        l, f = last[index], first[index]
        uncompressed.append(l)
        count = first[:index].count(f)

        for k in range(len(last)):
            if last[k] == f:
                if count == 0:
                    index = k
                    break
                count -= 1

    return bytes(uncompressed)
