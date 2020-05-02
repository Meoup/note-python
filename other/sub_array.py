def sub_array_1(nums):
    """
    给一个数组，返回其所有的连续的子数组
    :param nums:
    :return:
    """
    res = []
    for i in range(len(nums)):
        j = i + 3
        while j < len(nums)+1:
            res.append(nums[i:j])
            j += 2
    print(len(res), res)


def sub_array_2(nums):
    """
    给一个数组，返回其所有可能的子数组
    :param nums:
    :return:
    """
    res = [[]]
    for num in nums:
        res += [i + [num] for i in res]
    print(len(res), res)


def max_product(nums):
    """
    给一个数组，返回其连续的子数组中最大的乘积
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        nums[i] *= nums[i-1]

    print(max(nums))


if __name__ == '__main__':
    # sub_array_1([1, 2, 3, 4, 5, 2])
    max_product([2, 3, -2, 4])

