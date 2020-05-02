"""记录递归的一些用法和分治的策略应用"""

import sys

# 更改 python 默认的递归深度 （995）
sys.setrecursionlimit(10000)


def get_sum(nums):
    """
    计算列表中所有元素之和
    :param nums: list
    :return: int
    """

    if len(nums) == 0:
        return 0
    else:
        return nums[0] + get_sum(nums[1:])


def get_length(nums):
    """
    计算列表包含的元素数量
    :param nums: list
    :return: int
    """
    if not nums:
        return 0
    return 1 + get_length(nums[1:])


def get_max(nums):
    """
    找出列表中的最大值
    :param nums: list
    :return: int
    """
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    else:
        x = get_max(nums[1:])
        if nums[0] > x:
            return nums[0]
        else:
            return x


if __name__ == '__main__':
    print(get_sum([i for i in range(100)]))
    print(get_length([1, 2, 3, 4, 5, 6, 8]))
    print(get_max([8, 2, 3, 12, 3, 4, 19]))
