class Queue:
    """
    实现队列结构的类
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # 添加元素到队首
        self.queue.insert(0, item)

    def dequeue(self):
        # 移除队尾元素 并返回
        return self.queue.pop()

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)



