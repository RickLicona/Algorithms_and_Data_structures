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
        global a
        if root:
            self.inorder(root.left)
            a.append(root.val)
            print(root.val)
            self.inorder(root.right)

    def search(self, root, val):
        if root:
            if val < root.val:
                self.search(root.left, val)
            elif val > root.val:
                self.search(root.right, val)
            elif root.val == val:
                print("\nFound value: ", val)
                return 0


if __name__ == "__main__":
    a = []
    btree = Btree()
    btree.head = btree.insert(btree.head, 50)
    btree.head = btree.insert(btree.head, 30)
    btree.head = btree.insert(btree.head, 20)
    btree.head = btree.insert(btree.head, 40)
    btree.head = btree.insert(btree.head, 70)
    btree.head = btree.insert(btree.head, 60)
    btree.head = btree.insert(btree.head, 80)

    btree.inorder(btree.head)
    btree.search(btree.head, 30)
    print("Minimum Value in BT: ", min(a))
