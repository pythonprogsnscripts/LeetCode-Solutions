# Python3 code to find number of unique 
# BSTs Dynamic Programming solution 

# Function to find number of unique BST 
def numberOfBST(n):

    # DP to store the number of unique 
    # BST with key i  
    dp = [0] * (n + 1)

    # Base case  
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] = dp[i] + (dp[i - j] * dp[j - 1])
                
    return dp[n] 

# Driver Code 
if __name__ == "__main__": 

	n = 3
	print("Number of structurally Unique BST with", 
				n, "keys are :", numberOfBST(n)) 

# This code is contributed 
# by Rituraj Jain 
