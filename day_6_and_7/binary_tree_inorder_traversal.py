class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def inorder(node:TreeNode):
            nonlocal output
            if node:
                inorder(node.left)
                output.append(node.val)
                inorder(node.right)
        inorder(root)
        return output