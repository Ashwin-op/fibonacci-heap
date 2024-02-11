# explanations for member functions are provided in requirements.py
from __future__ import annotations


class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False
        self.degree = 0

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

    def __lt__(self, other: FibNode):
        return self.val < other.val

    def __gt__(self, other: FibNode):
        return self.val > other.val

    def __le__(self, other: FibNode):
        return self.val <= other.val

    def __ge__(self, other: FibNode):
        return self.val >= other.val

    def __repr__(self):
        return f"Node({self.val})"


class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min = None
        self.size = 0

    def get_roots(self) -> list[FibNode]:
        return self.roots

    def insert(self, val: int) -> FibNode:
        node = FibNode(val)
        self.roots.append(node)
        if self.min is None or node < self.min:
            self.min = node
        self.size += 1
        return node

    def delete_min(self) -> None:
        self.decrease_priority(self.min, -float("inf"))
        self.extract_min()

    def find_min(self) -> FibNode:
        return self.min

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        if new_val > node.val:
            return
        node.val = new_val
        parent = node.parent
        if parent is not None and node < parent:
            self.cut(node, parent)
            self.cascading_cut(parent)
        if node < self.min:
            self.min = node

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define

    def extract_min(self):
        if not self.min:
            return None
        min_node = self.min
        self.roots.extend(min_node.children)
        for child in min_node.children:
            child.parent = None
        self.roots.remove(min_node)
        if self.roots:
            self.consolidate()
        else:
            self.min = None
        self.size -= 1
        return min_node

    def consolidate(self):
        degree_table = [None] * (2 * self.size.bit_length())
        for root in sorted(self.roots, key=lambda x: x.val):
            degree = root.degree
            while degree_table[degree] is not None:
                item = degree_table[degree]
                if root > item:
                    root, item = item, root
                self.link(item, root)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = root
        self.min = min(self.roots, key=lambda x: x.val)

    def link(self, child: FibNode, parent: FibNode):
        self.roots.remove(child)
        parent.children.append(child)
        child.parent = parent
        parent.degree += 1
        child.flag = False

    def cut(self, child: FibNode, parent: FibNode):
        parent.children.remove(child)
        parent.degree -= 1
        self.roots.append(child)
        child.parent = None
        child.flag = False

    def cascading_cut(self, node: FibNode):
        parent = node.parent
        if parent is not None:
            if not node.flag:
                node.flag = True
            else:
                self.cut(node, parent)
                self.cascading_cut(parent)
