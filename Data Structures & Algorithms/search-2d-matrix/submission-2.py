class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = [0] * (len(matrix) * len(matrix[0]))
        for r,row in enumerate(matrix):
            for c,val in enumerate(row):
                flat_matrix[r*len(matrix[0]) + c] = val
        def binary_search (left, right):
            mid = (left+right)//2
            if left > right:
                return False
            if target == flat_matrix[mid]:
                return True
            elif target < flat_matrix[mid]:
                return binary_search(left,mid-1)
            elif  target > flat_matrix[mid]:
                return binary_search(mid+1, right)
        return binary_search(0, len(flat_matrix)-1)