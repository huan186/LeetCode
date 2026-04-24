# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        def dfs(node, depth, d):
            if not node:
                return
            if len(levels) == depth:
                levels.append(deque())
            if d == 0:
                levels[depth].append(node.val)
            else:
                levels[depth].appendleft(node.val)
            dfs(node.left, depth + 1, 1 - d)
            dfs(node.right, depth + 1, 1 - d)
        
        dfs(root, 0, 0)
        
        return list(map(list, levels))
            