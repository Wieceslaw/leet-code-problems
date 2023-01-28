from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    def req(_root: TreeNode, is_left):
        if not _root:
            return 0
        if not _root.left and not _root.right:
            if is_left:
                return _root.val
            else:
                return 0
        return req(_root.left, True) + req(_root.right, False)

    return req(root, False)
