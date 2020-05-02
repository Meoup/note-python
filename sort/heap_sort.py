def build_heap(nums, index, size):
    """
    堆：是一种完全二叉树，按不同的性质分成两种：大顶堆和小顶堆
    1.大顶堆：每个节点的值大于或等于其左右子节点的值
    2.小顶堆：每个节点的值小于或等于其左右子节点的值
    一般升序排序则构建大顶堆，降序排序则构建小顶堆
    """
    # 当前节点索引
    large_index = index
    # 左节点索引
    left_index = 2*index + 1
    # 右节点索引
    right_index = 2*index + 2
    # 判断当前节点的值与其左右节点的值的大小
    if left_index < size and nums[left_index] > nums[large_index]:
        large_index = left_index
    if right_index < size and nums[right_index] > nums[large_index]:
        large_index = right_index
    # 如果large_index!=index 代表需要调整当前节点
    if large_index != index:
        nums[index], nums[large_index] = nums[large_index], nums[index]
        # 同时对该节点继续延伸调整
        build_heap(nums, large_index, size)


def heap_sort(nums):
    """
    堆排序
    任何情况下的时间复杂度都为 O(n*logn)
    :param nums: unsorted list
    :return: list
    """
    size = len(nums)
    for i in range(size//2 - 1, -1, -1):
        build_heap(nums, i, size)
    for i in range(size-1, 0, -1):
        # 0索引位置的值就是堆顶的值，也就是最大值，移到数组的最右边
        nums[0], nums[i] = nums[i], nums[0]
        # 每次都从0索引位置开始构建， 同时把最大的值移除，不加入堆的构建
        build_heap(nums, 0, i)
    print(f"堆排序的结果: {nums}")
    return nums


if __name__ == '__main__':
    s = input("请输入要排序的数字，以','隔开:")
    unsorted_list = [int(i) for i in s.strip().split(',')]
    heap_sort(unsorted_list)
