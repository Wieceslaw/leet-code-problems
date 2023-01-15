from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)
