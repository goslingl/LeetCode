from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.arr = []

    def dfs(self, node):
        sum = 0
        if node == None:
            return sum
        acc = 0
        stack = [ (node, acc) ]
        while len(stack) > 0:
            node, acc = stack.pop()
            acc = acc * 2 + node.val
            if node.right != None:
                stack.append((node.right, acc))
            if node.left != None:
                stack.append((node.left, acc))
            if node.right == None and node.left == None:
                sum += acc
                print(acc)
                #acc = (acc - node.val)/2
        return int(sum)%(10**9+7)

    def bfs(self, node, layer):
        if node == None: return
        q = Queue()
        value_list = []
        q.put((node, 1))
        while q.empty() == False:
            node, layer = q.get()
            value_list.append((node.val, layer))
            if node.left != None:
                q.put((node.left, layer+1))
            if node.right != None:
                q.put((node.right, layer+1))
        print(value_list)
        # calc sum of tree num
        max_layer = value_list[-1][1]
        total_num = len(value_list)
        last_layer_left = 1<<(max_layer-1)
        sum = 0
        for idx in range(len(value_list)):
            val, layer = value_list[idx]
            if max_layer > layer:
                child_left = (idx+1)<<(max_layer-layer)
                child_right = child_left + (1<<(max_layer-layer)) -1
                num = (child_right - child_left+1) - (0 if total_num >= child_right else child_right-total_num)
                print('idx, child_left, child_right, num:', idx, child_left, child_right, num)
            else:
                num = 1
            if val > 0:
                sum += num * (1<<(max_layer-layer)) * val
        return sum%(10**9+7)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        #return self.bfs(root, 1)
        return self.dfs(root)

def main():
    tree = TreeNode(1)
    tree.left = TreeNode(1)
    tree.right = TreeNode(0)
    s= Solution()
    print(s.sumRootToLeaf(tree))
    tree = TreeNode(1)
    tree.left = TreeNode(1)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(0)
    tree.right = TreeNode(0)
    tree.right.left = TreeNode(1)
    print(s.sumRootToLeaf(tree))

main()
