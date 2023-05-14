class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, curr_node):
        if val < curr_node.val:
            if not curr_node.left:
                curr_node.left = Node(val)
            else:
                self._insert(val, curr_node.left)
        elif val > curr_node.val:
            if not curr_node.right:
                curr_node.right = Node(val)
            else:
                self._insert(val, curr_node.right)

    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, curr_node):
        if not curr_node:
            return False
        elif curr_node.val == val:
            return True
        elif val < curr_node.val:
            return self._search(val, curr_node.left)
        else:
            return self._search(val, curr_node.right)

    def delete(self, val):
        self.root = self._delete(val, self.root)

    def _delete(self, val, curr_node):
        if not curr_node:
            return curr_node
        elif val < curr_node.val:
            curr_node.left = self._delete(val, curr_node.left)
        elif val > curr_node.val:
            curr_node.right = self._delete(val, curr_node.right)
        else:
            if not curr_node.left:
                return curr_node.right
            elif not curr_node.right:
                return curr_node.left
            else:
                successor_node = self._find_min_node(curr_node.right)
                curr_node.val = successor_node.val
                curr_node.right = self._delete(successor_node.val, curr_node.right)
        return curr_node

    def _find_min_node(self, curr_node):
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node
import random

bst = BinarySearchTree()

for i in range(20):
    val = random.randint(1, 100)
    bst.insert(val)

print(bst.search(2))
print(bst.search(5))
print(bst.delete(2))
print(bst.delete(5))
print(bst.search(2))
print(bst.search(5))