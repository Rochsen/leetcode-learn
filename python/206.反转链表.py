#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next  # 保存下一个节点
            curr.next = prev       # 反转指针
            prev = curr            # 移动 prev
            curr = next_temp       # 移动 curr
        
        return prev 

# @lc code=end
