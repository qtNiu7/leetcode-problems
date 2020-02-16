### **[17.电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)**  

#### Letter combinations of a phone number

由给定的数字的字符串返回其在电话按键上所对应的字母的所有可能的字符串组合。

**示例** 

```
input: "23"
output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```



一个简单的搜索，每一层搜索一个数字，最后返回

复杂度为O($4^n$)



```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
		# mapping from digits to letters
        digits2letter = {'2': ['a', 'b', 'c'],
                         '3': ['d', 'e', 'f'],
                         '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],
                         '6': ['m', 'n', 'o'],
                         '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'],
                         '9': ['w', 'x', 'y', 'z']}


        def dfs(combination, rest): # dfs(本层之前的字母组合，剩下的数字)

            if len(rest) == 0:
                output.append(combination)
				
            else:
                for letter in digits2letter[rest[0]]:
                    dfs(combination + letter, rest[1:])

        output = []

        if len(digits) != 0:
            dfs("", digits)

        return output
```

