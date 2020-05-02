def bucket_sort(nums, bucket_size=5):
    """
    桶排序
    :param nums: unsorted list
    :param bucket_size: int
    :return: sorted list
    """
    if len(nums) <= 1:
        return nums
    max_num = max(nums)
    min_num = min(nums)
    # 计算桶的数量
    bucket_count = (max_num - min_num) // bucket_size + 1
    # 创建桶
    buckets = [[] for _ in range(bucket_count)]
    # 把数组中的元素分散到桶中
    for i in range(len(nums)):
        index = (nums[i] - min_num) // bucket_size
        buckets[index].append(nums[i])
        buckets[index] = insertion_sort(buckets[index])
    ans = []
    for bucket in buckets:
        if bucket:
            ans += bucket
    return ans


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
    input_nums = input("请输入要排序的序列，以','间隔开:")
    nums = [int(i) for i in input_nums.strip().split(',')]
    print(bucket_sort(nums))

