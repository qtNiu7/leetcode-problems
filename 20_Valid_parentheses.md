### Task

 判断给定的括号字符串是否有效，即左右括号能否一一正确匹配



如果全是左括号，可以一直叠加下去。但是如果第一个右括号出现，它就必须跟它前面第一个左括号匹配。匹配之后就消去这对括号，继续上述过程。最后如果所有都被消去，则是有效的括号字符串。

用列表来模拟一个栈，可以完美地还原匹配过程。

```python
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True
		# 空串被认为是有效的
             
        char2int = {'(': 10, ')': 11,
                    '[': 20, ']': 21,
                    '{': 30, '}': 31}
        # 用于判定是否匹配

        l = []
        # 用来模拟栈的列表

        for i in range(len(s)):
            top = len(l) - 1
            if top >= 0 and char2int[s[i]] - char2int[l[top]] == 1:
                l.pop()
            # 当前是右括号并且匹配
            else:
                l.append(s[i])

        if len(l) == 0:
            return True

        return False
```



