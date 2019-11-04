# T(n) = 2T(n/2) + O(n)
# T(n) = O(nlogn)
# If n == 1: O(1)

def findMaxSum(v, low, mid, high):
    # verifica e inclui maxSum do meio à esquerda
    sumAux = 0; leftSum = -100000
    maxLeft = maxRight = mid
    for i in range(mid, low-1, -1) : 
        sumAux += v[i]
        if (sumAux > leftSum) : 
            leftSum = sumAux
            maxLeft = i
    # faz o mesmo que o acima só que do meio à direita
    sumAux = 0; rightSum = -10000
    for i in range(mid + 1, high + 1) : 
        sumAux += v[i] 
        if (sumAux > rightSum) : 
            rightSum = sumAux
            maxRight = i
    # retorna a soma da soma do meio p/ esquerda e do meio p/ direita
    # e também as respectivas posições no vetor (maxLeft e maxRight)
    return leftSum + rightSum, maxLeft, maxRight

def maxSubarray(v, low, high, maxL, maxR) : 
    # array com apenas 1 elemento
    if (low == high):
        return v[low], maxL, maxR
    else:
        mid = (low + high) // 2 # divide no meio
        L, maxL, maxR = maxSubarray(v, low, mid, maxL, maxR) # L é soma max da esquerda
        R, maxL, maxR = maxSubarray(v, mid + 1, high, maxL, maxR) 
        C, maxL, maxR = findMaxSum(v, low, mid, high)
        print(maxL, maxR)
        return max(L, R, C), maxL, maxR

# [-3,2,3,4,-4,-1]. ANSWER = [2,3,4]    
v = [3, -4, 6, 2, -1]  #subarray = {6, 2}
n = len(v)
i = j = 0 # variáveis auxiliares p/ 
maxSum, i, j = maxSubarray(v, 0, n - 1, i, j)
subArray = [v[x] for x in range(i, j + 1)]
print("Maximum subarray is: ", subArray, "Sum = ", maxSum)