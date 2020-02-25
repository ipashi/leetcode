# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #empty binary search tree is also a binary search tree
        if(not root):
            return True
        #level order traverse the bst as it gives the sorted list of numbers
        def traverse(root):
            #root none indicates we have reached the end of tree
            if(not root):
                return None
            #inorder traversal left->root->right
            traverse(root.left)
            output.append(root.val)
            traverse(root.right)
        traverse(root)
        i=0
        #check if the elements in list are in order if not return false
        while(i<len(output)-1):
            if(output[i]>=output[i+1]):
                return False
            i+=1
        return True
