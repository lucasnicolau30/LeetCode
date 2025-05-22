class Solution(object):
    def arrayPairSum(self, nums):
        # Ordena o array em ordem crescente
        nums.sort()
        
        # Soma dos elementos nas posições pares (0, 2, 4, ...) após a ordenação
        return sum(nums[::2])