def selection_sort(nums):
    """
    选择排序算法：
        遍历数组，把最小的元素移到最左边，依次执行
    时间复杂度：O(n^2)
    空间复杂度：O(1)

    :param nums: list[integer]
    :return: list
    """
    length = len(nums)
    if length <= 1:
        return nums

    # 总次数
    for i in range(length-1):
        least = i
        for j in range(i+1, length):
            # 从i索引位置及其右边的所有元素中找出最小的元素
            if nums[j] < nums[least]:
                least = j
        # 把最小的元素移到左边
        nums[i], nums[least] = nums[least], nums[i]

    return nums


if __name__ == '__main__':
    print(selection_sort([9, 4, 2, 7, 2, 3, 6]))

