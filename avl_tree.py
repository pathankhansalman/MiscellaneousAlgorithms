class AVLNode:
    """A node in the AVL Tree."""
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """Self-balancing binary search tree (AVL Tree) implementation."""
    def get_height(self, node: AVLNode) -> int:
        if not node:
            return 0
        return node.height

    def get_balance(self, node: AVLNode) -> int:
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root: AVLNode, key: int) -> AVLNode:
        # 1. Perform standard BST insert
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor to check if it became unbalanced
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def pre_order(self, root: AVLNode, res=None) -> list:
        if res is None:
            res = []
        if root:
            res.append(root.key)
            self.pre_order(root.left, res)
            self.pre_order(root.right, res)
        return res

if __name__ == "__main__":
    tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        root = tree.insert(root, key)

    print("Pre-order traversal of the balanced AVL tree is:")
    print(tree.pre_order(root)) # Should be balanced
