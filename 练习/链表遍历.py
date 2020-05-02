class ListNode:
    """
    实现链表结构的类
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def build_list_node(n):
    """
    构建链表
    :param n: int
    :return: ListNode
    """
    root = ListNode(0)
    curr = root
    for i in range(1, n):
        curr.next = ListNode(i)
        curr = curr.next
    return root


def get_middle(root):
    """
    求中间节点
    慢指针返回的即中间节点
    :param root: ListNode
    :return: ListNode
    """
    slow = fast = root
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(f"slow: {slow.val} \nfast: {fast.val if fast else None}")


if __name__ == '__main__':
    node = build_list_node(6)
    get_middle(node)
