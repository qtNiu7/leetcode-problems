### Description
Given a string, find the length of the longest substring without repeating characters.

**Example 1:**

Input: "abcabcbb"

Output: 3 

Explanation:  The answer is "abc", with the length of 3.

**Thoughts**

It looks like a classic *Dynamic Programmin*g problem. So it's better to try to find a tranformation equation.

Let `dp[i]` repensent the length of substring that ends at *i* and has no repeating characters. 

If `s[i] == s[i - 1]`, it is intuitive that `dp[i]` equals to 1.

Otherwise, the value of `dp[i]` depends on whether `s[i]` has appeared.

If `s[i]` does not appear before, there's nothing like `s[i]` . So `dp[i] = dp[i - 1] + 1`
Otherwise, `dp[i]` can be `1 + dp[i - 1]` or the length of substring that starts from the next position of the previous `s[i]` (`i - mp[s[i]]`). In order to guarantee that no other `s[i]` is in the substring, 
`dp[i]` should be less than or equal to `i - mp[s[i]]`. 

Therefore, in this scenario, `dp[i] = min(1 + dp[i - 1], i - mp[s[i]])`.

Obviously, the time complexity here is O(n * log n)



```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        
        mp = {}
        dp = []
        m = 0
        for i in range(l): 
            dp.append(1)
            #mp[s[i]] = 1
            if i > 0:
                if s[i] != s[i - 1]:
                    if s[i] not in mp:
                        dp[i] = 1 + dp[i - 1]
                    else: dp[i] = min(1 + dp[i - 1], i - mp[s[i]])
                        
            mp[s[i]] = i
                
            if dp[i] > m:
                m = dp[i]
        return m
```

