from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: Optional[TreeNode]) -> list[str]:
    if not root:
        return []

    def req(_root: TreeNode, path: list[str]) -> list[str]:
        path = path + [str(_root.val)]
        if not _root.left and not _root.right:
            return ["->".join(path)]
        if _root.left and _root.right:
            return req(_root.left, path) + req(_root.right, path)
        if _root.left:
            return req(_root.left, path)
        return req(_root.right, path)

    return req(root, [])
