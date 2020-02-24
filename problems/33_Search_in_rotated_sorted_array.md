按升序排序的数组将某个位置后的元素全部移到前面。

例如，数组 `[0,1,2,4,5,6,7]` 可能变为 `[4,5,6,7,0,1,2]` 

要求在 *O(log n)* 的时间复杂度下返回给定值在数组中的下标



可以先二分查找找到数组递增发生变化的位置，如`[4,5,6,7,0,1,2]` 中 *7* 的位置，这样其两边的数组都是递增的了，然后再根据target与 `nums[0]` 的大小关系选择在哪段中进行二分查找。

有一组数据是 `[1, 3], 3` , 意思是将 `[1, 3]` 前移到了当前位置，即如果本来是 `[0, 1, 3]` ，就会变成 `[1, 3, 0]` 。



```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = len(nums)
        if l == 0:
            return -1
        i = 0
        j = l - 1

        # 得到数组中最大元素的下标，即单调性发生变化的地方
        def get_board(i, j):
            while i < j:
                mid = int((i + j) / 2)
                if nums[mid] >= nums[i]:
                    i = mid + 1
                    if nums[i] < nums[i - 1]:
                        return i - 1
                else:
                    j = mid - 1
                    if nums[j] > nums[j + 1]:
                        return j
            
            # 这种情况就是上面提到的[1, 3]，即数组本质上没变        
            return len(nums) - 1
        
        p = get_board(i, j)

        # 查找target的下标
        def find(left, right):
            while left <= right:
                mid = int((left + right) / 2)

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        if target >= nums[0]:
            return find(0, p)
        else:
            return find(p + 1, l - 1)


```





 