class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_dif = float('inf')
        resultado = []

        for i in range(1, len(arr)):
            dif = arr[i] - arr[i - 1]
            if dif < min_dif:
                min_dif = dif
                resultado = [[arr[i - 1], arr[i]]]
            elif dif == min_dif:
                resultado.append([arr[i - 1], arr[i]])

        return resultado
