"""
2. 两数相加

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            if l1:
                carry += l1.val  # 节点值和进位加在一起
                l1 = l1.next  # 下一个节点
            if l2:
                carry += l2.val  # 节点值和进位加在一起
                l2 = l2.next  # 下一个节点
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
            
        return dummy.next  # 哨兵节点的下一个节点就是头节点


if __name__ == '__main__':
    # 创建 Solution 实例
    solution = Solution()
    # 通过实例调用方法
    result = solution.addTwoNumbers(
        l1=ListNode(2, ListNode(4, ListNode(3))),
        l2=ListNode(5, ListNode(6, ListNode(4)))
    )

    # 打印链表中的所有节点值
    current = result
    while current:
        print(current.val, end=" -> ")
        current = current.next
        
    print("None")  # 表示链表结束
