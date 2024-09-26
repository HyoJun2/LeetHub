class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        temp = k - numOnes - numZeros
        if temp <= 0:
            return numOnes
        return numOnes - temp