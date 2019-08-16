def insertion_sort(nums):
    """
    插入排序

    :param nums: List[int]
    :return: List[int]
    """
    for i in range(1, len(nums)):
        val = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > val:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = val
    return nums


if __name__ == '__main__':
    print(insertion_sort([4, 1, 2, 7, 6, 3]))
