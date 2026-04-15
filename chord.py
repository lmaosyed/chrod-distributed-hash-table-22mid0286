import random

M = 6  # ID space (0–63)

def hash_key(key):
    return hash(key) % (2**M)

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.finger_table = []
        self.successor = None

    def __repr__(self):
        return f"Node({self.id})"


def build_ring(node_ids):
    nodes = sorted([Node(i) for i in node_ids], key=lambda x: x.id)

    # Assign successors
    for i in range(len(nodes)):
        nodes[i].successor = nodes[(i + 1) % len(nodes)]

    # Build finger tables
    for node in nodes:
        node.finger_table = []
        for i in range(M):
            start = (node.id + 2**i) % (2**M)
            successor = find_successor(nodes, start)
            node.finger_table.append(successor)

    return nodes


def find_successor(nodes, key):
    for node in nodes:
        if node.id >= key:
            return node
    return nodes[0]


def closest_preceding_node(node, key):
    for finger in reversed(node.finger_table):
        if node.id < finger.id < key:
            return finger
    return node


def lookup(start_node, key):
    hops = [start_node.id]
    current = start_node

    while not (current.id < key <= current.successor.id):
        current = closest_preceding_node(current, key)
        hops.append(current.id)

    hops.append(current.successor.id)
    return hops