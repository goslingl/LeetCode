# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    迭代计算完全二叉树的节点个数：从根节点开始，其左右子树必有一棵满二叉树，根据其右子树的最左叶子节点深度来判断
    判断后问题可分解为 根节点 + 满二叉树子树 + 另一棵子树，前两者可以直接计算，最后者则作为子问题递归或迭代计算
    '''
    def tree_deep(self, root):
        deep = 0
        node = root
        while node:
            deep += 1
            node = node.left
        return deep

    def tree_count(self, root, deep):
        if root == None or deep == 0:
            return 0
        elif deep == 1:
            return 1
        count = 1
        deep -= 1
        #print('count:%d, deep:%d' %(count, deep))
        rdeep = self.tree_deep(root.right)
        if rdeep == deep: # left child tree is full
            count += (1<<deep)-1
            #print('count add: %d' % ((1<<deep)-1))
            count += self.tree_count(root.right, rdeep) 
        else: # right child tree is full
            count += (1<<rdeep)-1
            count += self.tree_count(root.left, deep)
            #print('count add: %d' % ((1<<deep)-1))
        return count

    def countNodes(self, root: TreeNode) -> int:
        deep = self.tree_deep(root)
        count = self.tree_count(root, deep)
        return count
