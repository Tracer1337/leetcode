class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return triangle(numRows)
         
def triangle(n):
    # Triangle filled with 0s
    t = [[0] * i for i in range(1, n+1)]

    # Base Condition
    t[0][0] = 1

    for i in range(1, n):
        row = t[i]
        row[0] = 1
        row[-1] = 1
        for j in range(1, len(row)-1):
            l = t[i-1][j-1]
            r = t[i-1][j]
            row[j] = l + r
    
    return t
