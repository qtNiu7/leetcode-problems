输出给定字符串包含的最长有效括号对的子串的长度



动态规划：

令 `dp[i]`表示以 `s[i]` 结尾且是有效的最长子串的长度，显然有

![](https://github.com/qtNiu7/leetcode-problems/blob/master/appendix/32dp.png)


还有一种情况为 *s[i] == s[i - 1] == ' ) '*，即形如 .....)) 的。这种情况下如果`dp[i- 1]`为 *0* ，`dp[i]` 也为0；否则考虑能否将以 `s[i - 1]` 结尾的子串加入到当前字符结尾的子串使其仍然有效。以 `s[i - 1]` 结尾的最长有效子串的开始下标为 *i - 1 - dp[i - 1] + 1*， 若该元素的前一个元素可以与 `s[i]` 匹配，即 `s[i - 1 - dp[i - 1]] == '('` ，则可以加入，所以在这种情况下

*dp[i] = 2 + dp[i - 1] + dp[i - 1 - dp[i - 1] - 1]*

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        l = len(s)
        if l == 0:
            return 0
        dp = [0] * l

        for i in range(1, l):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2
                    if i - 2 >= 0:
                        dp[i] += dp[i - 2]
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(' :
                    dp[i] = dp[i - 1] + 2 
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
                        
        return max(dp)
```





