from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if root.left and root.right:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    if root.left:
        return 1 + minDepth(root.left)
    if root.right:
        return 1 + minDepth(root.right)
    return 0
