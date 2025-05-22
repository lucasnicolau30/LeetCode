class Solution(object):
    def heightChecker(self, heights):
        ordenada = sorted(heights)

        sum = 0
        for i in range(len(heights)):
            if ordenada[i] != heights[i]:
                sum += 1
        return sum