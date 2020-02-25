# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    	#traverse the binary search tree
        def traverse(root,maxvalue,minvalue):
        	# if root found to be None return true as we reached the end of tree
        	# with all the nodes in between found to be tree
            if(not root):
                return True
            # check if the current node val is less than its parent node if the curent node is left child
            # check if the current node val is greater than its parent node if the curent node is right child
            elif((maxvalue!=None and root.val>=maxvalue) or (minvalue !=None and root.val<=minvalue) ):
                return False
            else:
            	# correspondingly change the min and max values
                return traverse(root.left,root.val,minvalue) and traverse(root.right,maxvalue,root.val)
        return traverse(root,None,None)