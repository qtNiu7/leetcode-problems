### 题目要求

给定n， 输出所有有效的括号组合.



这个题乍一看可以用搜索来解决，但是之前刚做了一个用栈匹配括号的，所以想着这个题也用栈不用搜索来写写试试，最后写着写着还是写成了搜索，想明白了向后搜索和回溯过程实际上和栈的操作是一样的。

一开始肯定是先生成左括号，有了左括号才可以有右括号，而且左括号的数量不能小于右括号也不能大于n。每一步可以生成左括号也可以是右括号，但必须符合上述约束条件。

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def generate(combination, num_of_left, num_of_right):

            if len(combination) == 2 * n:
                res.append(combination)
                return
			# 达到长度要求
            
            if num_of_left < n:
                generate(combination + '(', num_of_left + 1, num_of_right)
			
            if num_of_right < num_of_left:
                generate(combination + ')', num_of_left, num_of_right + 1)

        

        generate("", 0, 0)

        return res
```



*以下是一开始写的弱弱的代码*

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(p, num_of_left, combination):

            # print(p, num_of_left, stack, combination)

            if p == n * 2:
                res.append(combination)
                return

            top = len(stack)


            temp = []

            # print(p, num_of_left, stack, combination)

            if num_of_left < n:

                stack.append('(')
                # temp = stack
                combination += '('
                num_of_left += 1
                generate(p + 1, num_of_left, combination)
                # stack = temp
                stack.pop()
                combination = combination[0 : len(combination) - 1]
                num_of_left -= 1

                if top > 0:
                    stack.pop()
                    combination += ')'
                    generate(p + 1, num_of_left, combination)
                    stack.append('(')

            else:
                stack.pop()
                combination += ')'
                generate(p + 1, num_of_left, combination)
                stack.append('(')


        # combination = ""
        res = []
        # num_of_left = 0
        stack = []
        generate(0, 0, "")

        return res
```

