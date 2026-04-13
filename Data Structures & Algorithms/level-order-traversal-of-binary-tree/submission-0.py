# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return ans
        ans.append([root.val])
        currNode = root
        nextLevel = []
        if currNode.left is not None:
            nextLevel.append(currNode.left)
        if currNode.right is not None:
            nextLevel.append(currNode.right)
        # above is starting point
        while len(nextLevel) != 0:
            valueOfThisLevel = []
            tempNextLevel = nextLevel
            nextLevel = []
            for node in tempNextLevel:
                valueOfThisLevel.append(node.val)
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
            ans.append(valueOfThisLevel)
        return ans
