class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        isToeplitz = True

        for rowIndex, row in enumerate(matrix):
            for colIndex, el in enumerate(row):
                if rowIndex > 0 and colIndex > 0:
                    if matrix[rowIndex][colIndex] != matrix[rowIndex-1][colIndex-1]:
                        isToeplitz = False
                        break

        return isToeplitz
