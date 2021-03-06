# Utility function to create a new 
# tree node  

# def invertTree(self, root):
#     if root:
#         invert = self.invertTree
#         root.left, root.right = invert(root.right), invert(root.left)
#         return root

class newNode: 
    def __init__(self,data): 
        self.data = data 
        self.left = self.right = None

def mirror(node):
    if (node == None):
        return
    else:
        temp = node  
        
        """ do the subtrees """
        mirror(node.left)  
        mirror(node.right)  

        """ swap the pointers in this node """
        temp = node.left  
        node.left = node.right  
        node.right = temp  

    """ Helper function to print Inorder traversal."""
def inOrder(node) : 
    if (node == None):  
        return
          
    inOrder(node.left)  
    print(node.data, end = " ")  
    inOrder(node.right)  
  
# Driver code  
if __name__ =="__main__":  
  
    root = newNode(1)  
    root.left = newNode(2)  
    root.right = newNode(3)  
    root.left.left = newNode(4)  
    root.left.right = newNode(5)  
  
    """ Print inorder traversal of 
        the input tree """
    print("Inorder traversal of the",  
               "constructed tree is")  
    inOrder(root)  
      
    """ Convert tree to its mirror """
    mirror(root)  
  
    """ Print inorder traversal of  
        the mirror tree """
    print("\nInorder traversal of",  
              "the mirror treeis ")  
    inOrder(root)  