class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Btree:
    def __init__(self, data=None):
        self.head = None

    def insert(self, root, data):
        if root is None:
            root = Node(data)
            return root
        else:
            if data > root.val:
                root.right = self.insert(root.right, data)
            else:
                root.left = self.insert(root.left, data)
            return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)

        return self.search(root.left, key)


if __name__ == "__main__":
    btree = Btree()
    btree.head = btree.insert(btree.head, 50)
    btree.head = btree.insert(btree.head, 30)
    btree.head = btree.insert(btree.head, 20)
    btree.head = btree.insert(btree.head, 40)
    btree.head = btree.insert(btree.head, 70)
    btree.head = btree.insert(btree.head, 60)
    btree.head = btree.insert(btree.head, 80)
    btree.inorder(btree.head)
