def merge_sorted_list(a, b):
    """
    合并两个排好序的数组
    :param a: list
    :param b: list
    :return: sorted list
    """
    print(f"a= {a}, b= {b}")
    i, j = 0, 0
    temp = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
    if i < len(a):
        temp += a[i:]
    if j < len(b):
        temp += b[j:]

    return temp


def merge_sort(nums):
    """
    归并排序
    :param nums: unsorted list
    :return: sorted list
    """
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    return merge_sorted_list(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


if __name__ == '__main__':
    l = [7, 2, 3, 4, 6, 5, 1]
    print(merge_sort(l))
