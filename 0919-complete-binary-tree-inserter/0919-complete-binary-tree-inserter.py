class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nodes = []
        self.__bfs__()

    def __bfs__(self) -> None:
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            self.nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        self.nodes.append(node)
        parent = self.nodes[(len(self.nodes) - 2) // 2]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root