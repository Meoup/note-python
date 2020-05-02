class Stack:
    """一个数组实现双堆栈"""
    def __init__(self):
        self.stack = []
        self.top1 = -1  # 代表左边的那个堆栈最上层的元素的索引
        self.top2 = len(self.stack)  # 代表右边的那个堆栈最上层的元素的索引

    def push(self, item, tag):
        """
        把数组分成两个堆栈，左边和右边， 插入的时候，都向数组中间push， 弹出的时候，往数组两边弹出
        item是要插入的元素， tag是指插入的堆栈
        """
        # 先判断数组是否已经满了
