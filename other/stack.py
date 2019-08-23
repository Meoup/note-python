class Stack:
    """
    实现栈的类
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        # 压入
        self.stack.append(item)

    def pop(self):
        # 弹出
        return self.stack.pop()

    def peek(self):
        # 返回栈顶元素
        return self.stack[-1]

    def is_empty(self):
        # 判断栈是否为空
        return self.stack == []

    def size(self):
        # 返回栈的长度
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(9)
    stack.push(4)
    print(stack.peek())
    print(stack.pop())
    print(stack.size())
