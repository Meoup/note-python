def insert_sort(nums):
    """
    对一个无序数组进行插入排序:
        可以理解为摸牌，从数组里取一个元素，与已排序的元素进行比较，然后把它放到对应的位置处
        插入排序是在原处进行操作，不需要多余的空间
    :param nums: unsorted list
    :return: sorted list
    """
    # 取牌, 手中默认拥有第一张牌
    for i in range(1, len(nums)):
        j = i
        # 把取出的牌与手中已排好序的牌进行比较，找到其正确位置
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums


if __name__ == '__main__':
    input_nums = input("请输入要排序的序列，以','间隔开:")
    nums = [int(i) for i in input_nums.strip().split(',')]
    print(insert_sort(nums))
