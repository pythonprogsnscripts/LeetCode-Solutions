def getPermutation(n,k):
    
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)

getPermutation(3,5)