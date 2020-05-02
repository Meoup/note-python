def get_kth_num(nums, k):
    """
    从一个数组中获取第k小的数
    :param nums: list
    :param k: int
    :return: int
    """
    # 首先对数组进行排序
    nums.sort()
    pre_num = nums[0]
    j = 1
    for i in range(1, len(nums)+1):
        if j == k:
            return pre_num
        if nums[i] != pre_num:
            j += 1
            pre_num = nums[i]
    return


if __name__ == '__main__':
    num = get_kth_num([2, 4, 1, 2, 7, 3, 2, 4], 6)
    print(num)
