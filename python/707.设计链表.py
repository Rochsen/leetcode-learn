#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class Node:
    """
    单向链表节点
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:
    """
    单向链表
    """

    def __init__(self):
        """
        初始化头节点
        """
        self.dum_head = Node(0)     # 哨兵节点
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:  # index 超出范围
            return -1
        prev = self.dum_head.next  # 获取实在的头节点，下标0
        for _ in range(index):  # 准确找到节点
            prev = prev.next
        return prev.value

    def addAtHead(self, val: int) -> None:
        """
        将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        将一个值为 val 的节点追加到链表中作为链表的最后一个元素
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        将一个值为 val 的节点插入到链表中下标为 index 的节点之前。
        如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。
        如果 index 比长度更大，该节点将 不会插入 到链表中。
        """
        if index > self.size or index < 0:  # index 大于链表长度，无法插入
            return

        # 新节点
        new = Node(val)

        # 哨兵节点
        prev = self.dum_head
        # 从哨兵节点开始，找到插入位置的前一个节点
        for _ in range(index):
            prev = prev.next

        # 先接后断
        new.next = prev.next
        prev.next = new

        # 链表长度加 1
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        如果下标有效，则删除链表中下标为 index 的节点。
        """
        if index < 0 or index >= self.size:  # index 超出范围
            return
        prev = self.dum_head  # 哨兵节点
        for _ in range(index):  # 找到删除位置的前一个节点
            prev = prev.next

        # 先接后断
        prev.next = prev.next.next
        # 链表长度减 1
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

