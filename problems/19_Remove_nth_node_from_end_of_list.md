#### Task：

 删除给定链表的倒数第n个元素，并返回链表的头结点



简单一想就是遍历两次链表，第一遍得到链表长度，第二遍找到相应位置的节点删除。

现在需要得到的是距离末节点是 *n - 1* 的节点的位置。既然距离末节点 *n - 1* 的节点一次遍历找不到，但是一次遍历可以找到距离头结点 *n - 1* 的节点。然后再让头结点和该节点同步向后遍历，后面节点到达末节点后，前面节点就是相应的倒数第 *n* 个节点。



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        i = 1
        s1 = head
        s2 = head
        
        while(i <= n):
            i += 1
            s1 = s1.next
        # 此时s1为正数第n + 1个

        if s1 is None:
            return head.next
        # 若第n + 1个为空，则n为链表长度，返回第二个节点
        
        while(s1.next):
            s1 = s1.next
            s2 = s2.next

        s2.next = s2.next.next

        return head
```

