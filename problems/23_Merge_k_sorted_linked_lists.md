合并k个有序链表



链表的头结点的值是最小的，每次从所有的k个链表头取最小值后加入新链表。
可以将所有头结点放到一个堆(优先队列)里，这里的优先级是值越小优先级越高。
维护这个优先队列的复杂度为 *log k* ，共n个节点总的时间复杂度为 *O(n  log k)*





```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Node:
#     def __init__(self, val, node):
#         self.val = val
#         self.node = node
#         
#         return
 
#     def __lt__(self, other):
#         return self.val < other.val


from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        q = PriorityQueue()

        new = ListNode(0) # 结果链表
        current = new     # 当前节点
        i = 0

        for head in lists:
            if head:
                q.put((head.val, i, head))
                # 这里将 i 也置于队列中是因为当两个对象的val相等时，确定优先级时
                # 会比较这两个对象的下一个元素，但是ListNode类型是不可比的
                i += 1
            
        while not q.empty():

            val, j, node = q.get()
            current.next = ListNode(node.val)
            current = current.next

            if node.next:
                q.put((node.next.val, i, node.next))
                i += 1

        return new.next
```

