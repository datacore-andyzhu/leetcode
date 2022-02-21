class solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        if left == len(nums) or nums[left] != target:
            return False
        
        leftmost = left
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right == 0 or nums[right] != target:
            return False

        if right - leftmost + 1 > len(nums) // 2:
            return True
        else:
            return False
