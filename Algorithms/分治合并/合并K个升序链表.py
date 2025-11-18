# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 示例 1：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6

# 示例 2：
# 输入：lists = []
# 输出：[]

# 示例 3：
# 输入：lists = [[]]
# 输出：[]

# 提示：
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(l1:Optional[ListNode], l2:Optional[ListNode])->Optional[ListNode]:
            if l1==None or l2==None:
                return l1 if l1 else l2
            
            head = ListNode
            tail = head
            aPtr = l1
            bPtr = l2
            while aPtr and bPtr:
                if aPtr.val < bPtr.val:
                    tail.next=aPtr
                    aPtr=aPtr.next
                else:
                    tail.next=bPtr
                    bPtr=bPtr.next
                tail=tail.next
            tail.next=aPtr if aPtr else bPtr
            return head.next

        def merge(lists:List[Optional[List]],l:int,r:int)->Optional[ListNode]:
            if l==r: return lists[l]
            if l>r: return None
            mid = (l+r)>>1
            return mergeTwoLists(merge(lists,l,mid),merge(lists,mid+1,r))
        
        return merge(lists,0,len(lists)-1)
