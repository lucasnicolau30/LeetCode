class Solution(object):
    def countPairs(self, nums, target):
      
        cont = 0
        for i in range(len(nums) - 1):
            soma = 0
            for j in range(i + 1, len(nums)):
                soma = nums[i] + nums[j]
                if soma < target:
                    cont += 1
        return cont    
