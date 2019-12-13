# 15. 3sum

## Description

Given an array `nums` of n integers, are there three elements *a, b, c* in `nums`that *a + b + c = 0*? 
Find all unique triplets in the array which gives sum of zero.

*Note that the solution set must not contain duplicate triplets.*

## Thoughts

This is like problem 11, Container With Most Water, in which you need to find 2 elements 
in a given list *a* to maxmize min(a[i], a[j]) * |j - i|.

In this problem, we need to find 3 elements that add up to *0*, which means they must contain both 
negative and positive elements or they are all zeros. Just sort the list first. Therefore, it is sort of like
We take one or two elements from the left side of *0* and then select the left elements from the right side of  *0*.

Then we can solve this problem by setting 2 pointers to scan the list, one from the right side of current element and the other from the end of the list to left, until they meet. 

We need also remove those duplicate solutions. Just skip those duplicate elements that we have select one of them to be in our solution.

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []

        for i in range(length - 1):
            if nums[i] > 0: # if current element > 0, there is no other solution left. 
                break  
            
            if nums[i] == nums[i - 1] and i > 0:
                continue
            l = i + 1
            r = length - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    # this means these three elements is too small, so we need to check
                    # larger elements
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else: 
                    ans.append([nums[i], nums[l], nums[r]])
                    # skip duplicate elements
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
        return ans
```



# 11. Container With Most Water

## Description

Given *n* non-negative integers $a_1, a_2, ..., a_n$ , where each represents a point at coordinate (*i*, $a_i$ ) . n vertical lines are drawn such that the two endpoints of line i is at (*i*, $a_i$ ) and (*i*, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="zoom:50%;" />



## Thoughts

If we set the left side of the container to be the shorter side of the bucket, then the maximun volume of the container is decided, from the current to the most right that is greater. So the first element we meet from end to left that is greater than the current guarantees that their distance is maximum. It is the same situation for the right side to be set as the shorter side.

Since the maximum volume of the container on the condition that the current side is the shorter side has been definite, we need to move accordingly if we want a potentially greater volume.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height) - 1

        m = 0

        while(i < j):

            t = (j - i) * min(height[i], height[j])

            if t > m:
                m = t

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        
        
        return m
```

