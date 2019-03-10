# https://leetcode-cn.com/contest/weekly-contest-127/problems/construct-binary-search-tree-from-preorder-traversal/
#1008. 先序遍历构造二叉树
#题目难度 Medium
#返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
#
#(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        t = TreeNode(0)
        if len(preorder) == 0:
            t = None
            return t
        t.val = preorder[0]
        left = [ e for e in preorder if e < t.val]
        right = [ e for e in preorder if e > t.val]
        t.left = self.bstFromPreorder(left)
        t.right = self.bstFromPreorder(right)
        return t
        
