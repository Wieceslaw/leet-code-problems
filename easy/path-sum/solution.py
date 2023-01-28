from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    return path_req(root, targetSum, 0)


def path_req(root: Optional[TreeNode], target_sum, value):
    if not root:
        return False
    if (root.val + value == target_sum) and (not root.right and not root.left):
        return True
    return path_req(root.right, target_sum, value + root.val) or path_req(root.left, target_sum, value + root.val)
