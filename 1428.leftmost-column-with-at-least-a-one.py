from typing import *
class BinaryMatrix:
    def get(self, row: int, col: int) -> int:
        pass
    def dimensions(self) -> list[list]:
        pass

def leftMostColumnWithOne(binaryMatrix: 'BinaryMatrix') -> int:
    m, n = binaryMatrix.dimensions()
    left = 0
    right = n-1
    res = -1
    while left <=right:
        mid = left + (right-left)//2
        for row in range(m):
            if binaryMatrix.get(row, mid):
                res = mid
                right = mid-1
        else:
            left = mid+1
    
    return res