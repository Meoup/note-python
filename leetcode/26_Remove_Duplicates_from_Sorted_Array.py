def remove_duplicates(nums):
    """
    原地删除数组中重复的元素，并返回最终的数组长度
    in-place: 空间复杂度 O(1)
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    else:
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                del nums[index]
            else:
                index += 1

        return len(nums)


if __name__ == '__main__':
    print(remove_duplicates([0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 5, 6]))
