class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        #print(nums)

        length = len(nums)

        ans = []

        for i in range(length - 1):
            if nums[i] > 0:
                break
            # 0 0 0    
            
            if nums[i] == nums[i - 1] and i > 0:
                continue
            l = i + 1
            r = length - 1
            #print(i, l, r)
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r = r - 1
                else: 
                    t = [nums[i], nums[l], nums[r]]
                    ans.append(t)
                    #print(t)
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
        return ans
