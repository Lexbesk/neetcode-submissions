# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the same as finding a node with value between p and q (including both)
        l = r = None
        if p.val < q.val:
            l = p
            r = q
        elif p.val > q.val:
            l = q
            r = p
        else:
            return p
        # traverse the tree
        temp = root
        while True:
            # print(temp.val)
            if l.val <= temp.val and temp.val <= r.val:
                return temp
            elif temp.val < l.val:
                temp = temp.right
            else:
                temp = temp.left
