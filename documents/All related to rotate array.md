##### 【旋转数组】从易到难，各个击破！

这里从易到难总结一下**旋转数组**相关的题，都是二分法的套路，看了这篇题解，一次搞定6道题！

###### [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/)

**题目：**
<img src="https://pic.leetcode-cn.com/1614342022-CcPoNe-189.png" alt="189.png" style="zoom:50%;" />

**题解：**

```
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        n=len(nums)
        # 向右移动的位置k可能会大于n，因此对n取余
        k=k%n
        if k==0 or n<2:
            return 
        # 以此为例：nums = [1,2,3,4,5,6,7], k = 3
        # 先整个数组反转：[7,6,5,4,3,2,1]
        reverse(0,n-1)
        # 前k个反转：[5,6,7,4,3,2,1]
        reverse(0,k-1)
        # 后n-k个反转：[5,6,7,1,2,3,4]
        reverse(k,n-1)
```

###### [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

**题目：**
<img src="https://pic.leetcode-cn.com/1614331948-oeQkSL-153.png" alt="153.png" style="zoom:50%;" />



- nums 中的所有整数都是 **唯一** 的
- nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转

**题解：**

```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=n-1
        # 这里控制条件没取等号，取等号大多是为了在while中直return mid，不取等号就跳出while返回l的值。
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                # 中间数字大于右边数字，比如[3,4,5,1,2]，则左侧是有序上升的，最小值在右侧
                left=mid+1
            else:
                # 中间数字小于等于右边数字，比如[6,7,1,2,3,4,5]，则右侧是有序上升的，最小值在左侧
                right=mid
        return nums[left]
```

###### [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

**题目：**
<img src="https://pic.leetcode-cn.com/1614331907-SXkPOM-154.png" alt="154.png" style="zoom:50%;" />



- 这道题是 153.寻找旋转排序数组中的最小值 的延伸题目。
- 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

**题解：**

```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=n-1
        # 这里控制条件没取等号，取等号大多是为了在while中直return mid，不取等号就跳出while返回l的值。
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                # 中间数字大于右边数字，比如[3,4,5,1,2]，则左侧是有序上升的，最小值在右侧
                left=mid+1
            elif nums[mid]<nums[right]:
                # 中间数字小于等于右边数字，比如[6,7,1,2,3,4,5]，则右侧是有序上升的，最小值在左侧
                right=mid
            else:
                # 中间数字等于右边数字，比如[2,3,1,1,1]或者[4,1,2,3,3,3,3]
                # 则重复数字可能为最小值，也可能最小值在重复值的左侧
                # 所以将right左移一位
                right-=1
        return nums[left]        
```

平均时间复杂度为 O(logn)，而在最坏情况下，如果数组中的元素完全相同，那么 while 循环就需要执行 n次，每次忽略区间的右端点，时间复杂度为 O(n)。

上面两道题是在旋转数组里寻找最小值，下面两道题是在旋转数组里寻找指定的值，这两道题的区别也是存不存在重复值。

###### [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

**题目：**
<img src="https://pic.leetcode-cn.com/1614333837-WoOixM-33.png" alt="33.png" style="zoom:50%;" />



**题解：**

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r=0,len(nums)-1
        # 这里控制条件取等号，取等号大多是为了在while中直return mid，不取等号就跳出while返回l的值。
        while l<=r:
            mid=l+(r-l)//2
            # 中间值即为target，直接返回
            if nums[mid]==target:
                return mid
            # 左半部分是有序
            if nums[0]<=nums[mid]:
                # target落在左半部分有序区域内
                if nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    # target落在右半部分无序区域内
                    l=mid+1
            else: # 右半部分是有序
                # target落在右半部分有序区域内
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    # target落在左半部分无序区域内
                    r=mid-1
        return -1
```

###### [81. 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)

**题目：**
<img src="https://pic.leetcode-cn.com/1614335927-tYYpNz-81.png" alt="81.png" style="zoom:50%;" />



**题解：**

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return False
        l,r=0,len(nums)-1
        while l<=r:
            # 重点在于处理重复数字
            # 左边有重复数字，将左边界右移
            while l<r and nums[l]==nums[l+1]:
                l+=1
            # 右边有重复数字，将右边界左移
            while l<r and nums[r]==nums[r-1]:
                r-=1
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            # 左半部分有序
            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:# 右半部分有序
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    r=mid-1
        return False
```

###### [面试题 10.03. 搜索旋转数组](https://leetcode-cn.com/problems/search-rotate-array-lcci/)

这道题与81题很像，唯一的区别就是81题要求只要存在target就返回true，而这道题要 返回多个重复target中最靠前的那个
**题目：**
<img src="https://pic.leetcode-cn.com/1614336561-VRccXk-1003.png" alt="1003.png" style="zoom:50%;" />



**题解：** 此题边界case很多，与上面的几道题相比，注释里给出了三个重点改变，仔细体会。

```
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n=len(arr)
        left=0
        right=n-1
        while left<=right:
            # 重点1：当left符合时直接返回, 因为找的是最小的索引
            if arr[left]==target:
                return left
            mid=left+(right-left)//2
            # 重点2：当中间值等于目标值，将右边界移到中间，因为左边可能还有相等的值
            if arr[mid]==target:
                right=mid
            elif arr[0]<arr[mid]:
                if arr[0]<=target<arr[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif arr[0]>arr[mid]:
                if arr[mid]<target<=arr[n-1]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                # 重点3：当中间数字与左边数字相等时，将左边界右移
                    left+=1
        return -1
```

------

