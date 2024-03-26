# explanations for member functions are provided in requirements.py
from __future__ import annotations


class FibNodeLazy:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False
        self.degree = 0
        self.vacant = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNodeLazy):
        return self.val == other.val

    def __lt__(self, other: FibNodeLazy):
        return self.val < other.val

    def __gt__(self, other: FibNodeLazy):
        return self.val > other.val

    def __le__(self, other: FibNodeLazy):
        return self.val <= other.val

    def __ge__(self, other: FibNodeLazy):
        return self.val >= other.val

    def __repr__(self):
        return f"Node({self.val})"


class FibHeapLazy:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min = None
        self.size = 0

    def get_roots(self) -> list[FibNodeLazy]:
        return self.roots

    def insert(self, val: int) -> FibNodeLazy:
        node = FibNodeLazy(val)
        self.roots.append(node)
        if self.min is None or node < self.min:
            self.min = node
        self.size += 1
        return node

    def delete_min_lazy(self) -> None:
        if self.min.vacant:
            self.extract_min_lazy()
        self.min.vacant = True

    def find_min_lazy(self) -> FibNodeLazy:
        if self.min.vacant:
            self.extract_min_lazy()
        return self.min

    def decrease_priority(self, node: FibNodeLazy, new_val: int) -> None:
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

    def extract_min_lazy(self) -> FibNodeLazy:
        if not self.min:
            return None
        while root := next((root for root in self.roots if root.vacant), None):
            self.roots.extend(root.children)
            for child in root.children:
                child.parent = None
            self.roots.remove(root)
            self.size -= 1
        self.consolidate_lazy()
        return self.min

    def consolidate_lazy(self):
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

    def link(self, child: FibNodeLazy, parent: FibNodeLazy):
        self.roots.remove(child)
        parent.children.append(child)
        child.parent = parent
        parent.degree += 1
        child.flag = False

    def cut(self, child: FibNodeLazy, parent: FibNodeLazy):
        parent.children.remove(child)
        parent.degree -= 1
        self.roots.append(child)
        child.parent = None
        child.flag = False

    def cascading_cut(self, node: FibNodeLazy):
        parent = node.parent
        if parent is not None:
            if not node.flag:
                node.flag = True
            else:
                self.cut(node, parent)
                self.cascading_cut(parent)
