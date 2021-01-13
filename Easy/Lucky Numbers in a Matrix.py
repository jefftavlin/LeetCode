class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        l = []
        ROW = [min(row) for row in matrix]

        for i in range(len(matrix[0])):
            lst = []
            for row in matrix:
                lst.append(row[i])
            l.append(lst)
        
        for item in l:
            big = max(item)
            for n in item:
                if n in ROW and n == big:
                    return [n]
