#Dynamic Programming problems and solutions

# Simple Fibonacci
def fib(n):
    a,b = 0,1
    if n==0:
        return a
    for i in range(1,n):
        a,b = b,a+b
    return b

# Length of Longest Common Subsequence between 2 strings, eg. LCS("ABC","AxByC")=3
def LCS(a,b):
    W = len(a)+1
    H = len(b)+1
    memo = [[0]*W for i in range(H)]
    for i in range(1,H):
        for j in range(1,W):
            if b[i-1]==a[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j],memo[i][j-1])
    return memo[-1][-1]

# Length of Longest Increasing Subsequence in list, eg. LCS([1,2,5,3,6]])=3
def LIS(a):
    size = len(a)
    memo = [1] * size
    for i in range(1,size):
        for j in range(i):
            if a[j]<a[i]:
                memo[i] = max(memo[i],memo[j]+1)
    return memo[-1]

def editDistance(a,b):
    W = len(a)+1
    H = len(b)+1
    memo = [[0]*W for i in range(H)]
    for i in range(1,H):
        for j in range(1,W):
            if b[i-1]==a[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = min(memo[i-1][j],memo[i][j-1],memo[i-1][j-1])+1
    return memo[-1][-1]



print("Fibonacci Sequence:")
for i in range(10):
    print(fib(i), end=" ")
print("\n-------------------")

print("LCS test cases:")
testCases = [("cato","cao"), ("abcdef","axbyyexf")]
for test in testCases:
    print(test)
    print(LCS(test[0],test[1]))
print("-------------------")

print("LIS test cases:")
testCases = [[1,5,2,3,9,8], [2,1,5,3,4,8,6,7]]
for test in testCases:
    print(test)
    print(LIS(test))
print("-------------------")

print("EditDistance test cases:")
testCases = [("cato","cao"), ("abcdef","axbyyexf")]
for test in testCases:
    print(test)
    print(editDistance(test[0],test[1]))
print("-------------------")
