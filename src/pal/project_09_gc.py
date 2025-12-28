import weakref
from typing import Any

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Node | None = None

    def __repr__(self):
        return f"Node({self.value})"

def make_cycle() -> weakref.ReferenceType:
    node_a = Node("A")
    node_b = Node("B")

    node_a.next = node_b
    node_b.next = node_a

    spy = weakref.ref(node_a)

    del node_a
    del node_b

    return spy
