# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        init = []
        init.append(root)
        def bfs(listToTrav, result):
            if len(listToTrav) == 0:
                return result
            result.append(listToTrav[-1].val)
            queue = []
            for r in listToTrav:
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            return bfs(queue, result)
        return bfs(init, [])