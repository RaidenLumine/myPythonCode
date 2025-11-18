# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]

# 示例 3：
# 输入：head = [1,2], n = 1
# 输出：[1]

# 提示：
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head:Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = ListNode(0)
        pre.next=head
        start,end=pre,pre
        while end.next:
            end=end.next
            if n!=0:
                n-=1
                continue
            if n==0:
                start=start.next
        start.next=start.next.next
        return pre.next