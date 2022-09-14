54. **Spiral Matrix**

    Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

     

    **Example 1:**

    ![img](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

    ```
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    ```

    **Example 2:**

    ![img](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

    ```
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    ```

     

    **Constraints:**

    - `m == matrix.length`

    - `n == matrix[i].length`

    - `1 <= m, n <= 10`

    - `-100 <= matrix[i][j] <= 100`

      ```python
      class Solution:
          def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
              m = len(matrix)
              n = len(matrix[0])
              
              left = 0
              right = n - 1
              top = 0
              bottom = m - 1
              
              res = []
              while left <= right and top <= bottom:
                  for y in range(left, right+1):
                      res.append(matrix[top][y])
                  for x in range(top+1, bottom+1):
                      res.append(matrix[x][right])
                  for y in range(right-1, left-1, -1):
                      if bottom > top:
                          res.append(matrix[bottom][y])
                  for x in range(bottom-1, top, -1):
                      if right > left:
                          res.append(matrix[x][left])
                  left += 1
                  right -= 1
                  top += 1
                  bottom -= 1
              return res
      ```

      

    59. **Spiral Matrix II**

        Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from `1` to `n2` in spiral order.

         

        **Example 1:**

        ![img](https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg)

        ```
        Input: n = 3
        Output: [[1,2,3],[8,9,4],[7,6,5]]
        ```

        **Example 2:**

        ```
        Input: n = 1
        Output: [[1]]
        ```

         

        **Constraints:**

        - `1 <= n <= 20`

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        
        
        while left <= right and top <= bottom:
            for y in range(left, right+1):
                res[top][y] = num
                num += 1
            
            for x in range(top+1, bottom+1):
                res[x][right] = num
                num += 1
            
            for y in range(right-1, left-1, -1):
                if bottom > top:
                    res[bottom][y] = num
                    num += 1
            
            for x in range(bottom-1, top, -1):
                if right > left:
                    res[x][left] = num
                    num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        # we do not need this, if we add this
        # we need to change the above while loop from <= to < 
        
        # if n % 2 !=0:
        #     res[n//2][n//2] = num
        
        return res
```

885. **Spiral Matrix III**

     You start at the cell `(rStart, cStart)` of an `rows x cols` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

     You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all `rows * cols` spaces of the grid.

     Return *an array of coordinates representing the positions of the grid in the order you visited them*.

      

     **Example 1:**

     ![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png)

     ```
     Input: rows = 1, cols = 4, rStart = 0, cStart = 0
     Output: [[0,0],[0,1],[0,2],[0,3]]
     ```

     **Example 2:**

     ![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png)

     ```
     Input: rows = 5, cols = 6, rStart = 1, cStart = 4
     Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
     ```

      

     **Constraints:**

     - `1 <= rows, cols <= 100`
     - `0 <= rStart < rows`
     - `0 <= cStart < cols`

```python
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        if rows * cols == 1:
            return res
        
        # the walk will be in step of 1, 3, 5, ...
        for k in range(1, 2*(rows*cols), 2):
            # direction vector is the shape of (row, col, steps)
            # but in the sequence of east, south, west, north
            # east, south 1 step, then west, north need to be 2 steps
            # then east, south 3 steps, then west, north need to be 4 steps, etc
            for dr, dc, dk in [(0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)]:
                # we need to walk each step
                for _ in range(dk):
                    rStart += dr
                    cStart += dc
                    
                    # if the the walk is in the grid, we need to add to res
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                        # once we walked all the cells in the grid, we need to
                        # break, otherwise, we will walk endlessly
                        if len(res) == rows * cols:
                            return res
```

