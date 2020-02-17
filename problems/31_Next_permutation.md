### 31. Next permutation

返回给定列表数字序列的全排列的下一个，若当前是最后一个则返回第一个。



产生下一个排列的一般思路：

要得到比当前排列大的最小的排列，就是要让高位数字(前面的数字)与后面的数字交换，变成比当前大的最小的数字，然后再使该位后面的所有数字为从前到后升序。

- 从后往前找出第一个比其后面数字小的数字，即从后往前第一个非递增的数字，记为 `nums[i]`
- 从后往前找出第一个比 `nums[i]` 大的数字 `nums[j]`， 交换这两个的值。从后往前到 *i* 之前都是升序的，所以 `nums[j]` 就是要找的数。
- 交换之后从 *i + 1* 到最后还是降序的，没有改变之前的顺序，再将这部分翻转即可。

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = j = len(nums) - 1
        t = f = 0

        while i > 0:
			# 先找第一个从后往前第一个非递增的位置: i - 1
            if nums[i] <= nums[i - 1]:
                i -= 1

            else:
                f = 1 # f = 1 表示当前不是最后一个排列
                break

        # print('i :', i, 'f: ', f)

        if f == 0: # 最后一个排列直接翻转数组
            while i < j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
                j -= 1
            return



        # nums[i] > nums[i - 1]

        while j > 0 and j > i - 1:
            if nums[j] > nums[i - 1]:
                break
            else:
                j -= 1

        # print('j: ', j)

        # nums[j] < nums[i - 1]

        t = nums[i - 1]
        nums[i - 1] = nums[j]
        nums[j] = t

        j = len(nums) - 1

        while i < j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            i += 1
            j -= 1

        # return nums
```

