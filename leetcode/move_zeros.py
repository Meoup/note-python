def move_zeros(nums):
    """
    移动所有的元素0到数组的右边，并保持原有非零元素的排序。
    请在原数组中完成操作，不产生额外的空间
    :param nums: List
    :return: None
    """
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    print(nums)


if __name__ == '__main__':
    a = [6, 6, 0, 14, 0]
    move_zeros(a)

