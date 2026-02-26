"""
94. 二叉树的中序遍历

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
    