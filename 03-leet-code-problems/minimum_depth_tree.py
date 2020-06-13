# Python program to introduce Binary Tree 

# A class that represents an individual node in a 
# Binary Tree 
class BinaryTree:
    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

class Solution:
    
    def min_depth(self, root: BinaryTree) -> int:
            return self.depth(root)

    def depth(self, root):
        if not root:
            return 0
        elif root.left and root.right:
            return min(self.depth(root.left), self.depth(root.right))+1
        else: 
            return min(self.depth(root.left), self.depth(root.right))+1    

def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getNodeValue())
        printTree(tree.getRightChild())



# create root 
myTree = BinaryTree(1)
myTree.insertLeft(None)
myTree.insertRight(2)
printTree(myTree)

sol = Solution()
print(sol.min_depth(myTree))
