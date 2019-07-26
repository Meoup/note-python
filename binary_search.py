def binary_search(item, nums):
    """
    二分查找算法：
        给定一个有序数组和一个元素，查找该元素并返回该元素在这个数组里的索引
    时间复杂度：O(log n)
    最好：O(1)
    最坏：O(log n)
    空间复杂度：O(1)

    :param item: int
    :param nums: list
    :return: int
    """
    # 本例默认数组从小到大排序的
    low = 0
    high = len(nums)-1
    while high >= low:
        mid = (high+low) // 2  # 求整
        if nums[mid] == item:
            return mid
        elif nums[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return


if __name__ == '__main__':
    print(binary_search(5, [1, 3, 6, 7, 9, 12, 18, 20, 25]))
