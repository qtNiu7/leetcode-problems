#### 题目要求

在 *O(log n)* 时间内查找升序数组中和给定值相等的元素的第一个和最后一个位置



按照普通二分查找方法查找，遇到 `nums[i]` 和 `target` 相等时，如果是要找最后一个位置就比较当前元素和它后一个元素的大小关系，相等则令 `i = mid + 1` ，否则即为找到最右的位置；第一个位置同理。



```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def leftmost_or_rightmost(is_left):

            l = len(nums)
            i = 0
            j = l - 1

            while i <= j:
                
                mid = int((i + j) / 2)

                if nums[mid] < target:
                 i = mid + 1
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    
                    if not is_left: # 查找最后一个位置
                        if mid == l - 1 or nums[mid] < nums[mid + 1]:
                            return mid
                        else:
                            i = mid + 1
                            
                    else:           # 查找第一个位置
                        if mid == 0 or nums[mid] > nums[mid - 1]:
                            return mid
                        else:
                            j = mid - 1

            return -1
        return [leftmost_or_rightmost(1), leftmost_or_rightmost(0)]
```



