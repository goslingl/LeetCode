# pass

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        valList = []
        self.res = 0
        self.nodeSum(root, sum, valList)
        return self.res
    
    def nodeSum(self, root, sum, valList):
        if root ==None: return
        valList2 = valList[:]
        valList2.append(0)
        for idx in range(len(valList2)):
            valList2[idx] += root.val
            if valList2[idx] == sum: self.res += 1
        self.nodeSum(root.left, sum, valList2)
        self.nodeSum(root.right, sum, valList2)
        
        
