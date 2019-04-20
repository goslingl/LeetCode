class Solution:
    def countNodes(self, root: TreeNode) -> int:
    '''
    从根节点开始，查找右子节点直到叶节点，如何深度等于树的深度，返回结果；否则往上一级查找左子节点
    直到找到从根节点到最后一个叶子节点的路径，按左0右1编码，编码二进制的值即叶子节点个数
    '''
        deep = 0
        stk = list()

        if root == None: return 0
        node = root
        while node:
            deep += 1
            node = node.left
        #print('deep:', deep)
        stk.append((None, root))

        while len(stk) > 0 and len(stk) < deep:
            pnode, node = stk[-1]
            if node.right:
                stk.append((node, node.right))

            elif node.left:
                stk.append((node, node.left))

            else:
                stk.pop()
                #print('pop node %d' % (node.val))
                if node == pnode.right:
                    stk.append((pnode, pnode.left))

                elif node == pnode.left:
                    while True:
                        pnode2, node2 = stk.pop()
                        if pnode2.right == pnode:
                            stk.append((pnode2, pnode2.left))

                            break
                        else:
                            pnode, node = pnode2, node2
        encode = ''
        for pnode, node in stk:
            if pnode == None: encode += '1'
            elif pnode.left == node: encode += '0'
            else: encode += '1'
            #print(node.val)
        return int(encode, base=2)
