"""
Description

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

"""

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
