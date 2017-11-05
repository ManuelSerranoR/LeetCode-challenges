# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mini = [float('inf')]
        def checkNode(node):
            if not node:
                return
            elif root.val < node.val < mini[0]:
                mini[0] = node.val
            checkNode(node.left)
            checkNode(node.right)
        checkNode(root)
        
        
        return -1 if mini[0] == float('inf') else mini[0]
