from itertools import cycle


def get_count(n, m):
    """
    使用列表
    :param n:
    :param m:
    :return:
    """
    nums = [i for i in range(1, n+1)]
    while len(nums) > 1:
        for i in range(m-1):
            nums.append(nums.pop(0))
        nums.pop(0)

    print(nums)


def get_count_cycle(n, m):
    """
    使用环
    :param n:
    :param m:
    :return:
    """
    nums = list(range(1, n+1))
    while len(nums) > 1:
        c = cycle(nums)
        for i in range(m):
            e = next(c)
        index = nums.index(e)
        nums = nums[index+1:] + nums[:index]

    print(nums)


if __name__ == '__main__':
    get_count(20, 3)
    get_count_cycle(20, 3)
