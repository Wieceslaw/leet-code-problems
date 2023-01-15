from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def inorder_traversal(_root: Optional[TreeNode]) -> list[int]:
        if not _root:
            return [None]
        return inorder_traversal(_root.left) + [_root.val] + inorder_traversal(_root.right)

    def is_palindrome(lst):
        length = len(lst)
        for i in range(length // 2):
            if lst[i] != lst[length - i - 1]:
                return False
        return True

    return is_palindrome(inorder_traversal(root))
