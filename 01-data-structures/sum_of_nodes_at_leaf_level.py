# Python3 implementation to find the sum 
# of leaf node at minimum level 
from collections import deque 

# Structure of a node in binary tree 
class Node: 
	
	def __init__(self, data): 
		
		self.data = data 
		self.left = None
		self.right = None

# function to find the sum of leaf nodes 
# at minimum level 
def sumOfLeafNodesAtLeafLevel(root): 

	# if tree is empty 
	if not root: 
		return 0

	# if there is only root node 
	if not root.left and not root.right: 
		return root.data 

	# Queue used for level order traversal 
	Queue = deque() 
	sum = f = 0

	# push root node in the queue 
	Queue.append(root) 

	while not f: 
		
		# count no. of nodes present at current level 
		nc = len(Queue) 

		# traverse current level nodes 
		while nc: 
			top = Queue.popleft() 

			# if node is leaf node 
			if not top.left and not top.right: 
				sum += top.data 

				# set flag = 1 to signify that 
				# we have encountered the minimum level 
				f = 1
			else: 

				# if top's left or right child exist 
				# push them to Queue 
				if top.left: 
					Queue.append(top.left) 
				if top.right: 
					Queue.append(top.right) 
			nc -= 1

	# return the sum 
	return sum

# Driver code 
if __name__ == "__main__": 

	# binary tree creation 
	root = Node(1) 
	root.left = Node(2) 
	root.right = Node(3) 
	root.left.left = Node(4) 
	root.left.right = Node(5) 
	root.right.left = Node(6) 
	root.right.right = Node(7) 
	root.left.right.left = Node(8) 
	root.right.left.right = Node(9) 

	print("Sum = ", sumOfLeafNodesAtLeafLevel(root)) 
