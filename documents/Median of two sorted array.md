```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        
        left, right = 0, m
        
        total_left = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            left_i = -math.inf if i == 0 else nums1[i - 1]
            left_j = -math.inf if j == 0 else nums2[j - 1]

            right_i = math.inf if i == m else nums1[i]
            right_j = math.inf if j == n else nums2[j]
            
            if left_i <= right_j:
                median1 = max(left_i, left_j)
                median2 = min(right_i, right_j)
                left = i + 1
            else:
                right = i - 1

                
        if (m + n) % 2 == 0:
            return (median1 + median2) / 2
        else:
            return median1
```

