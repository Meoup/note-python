"""
本文件夹主要记录内容：
    1.LeetCode的一些题目的解法 --start：2019-07-04
    2.学习过程中的一些算法的实现
    3.遇到的值得学习的一些代码的用法

文件名的格式：
    LeetCode：题目序号_题目名称.py


"""

from collections import deque
from queue import Queue


a = deque()
b = Queue()
a += {"a": 3, "b": 4}
b.put({"a": 3, "b": 4})
b.put([1, 2, 3, 4])
print(a)
print(a.popleft())
print(a.pop())
print(b.get())
print(b.get())
