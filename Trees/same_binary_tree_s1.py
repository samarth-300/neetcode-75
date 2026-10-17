## Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkTree(self, a: Optional[TreeNode], arr):
        if not a:
            arr.append(-999)
            return 
        
        arr.append(a.val)
        self.checkTree(a.left,arr)
        self.checkTree(a.right, arr)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arrayOne = []
        arrayTwo = []

        self.checkTree(p, arrayOne)
        self.checkTree(q, arrayTwo)
        
        return (arrayOne == arrayTwo)