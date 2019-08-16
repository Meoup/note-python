def search_matrix(matrix, target):
    """
    要求：
        从一个2维矩阵中寻找数值，如果找到了返回 True , 否则返回 False ,该矩阵具有以下特性：
            1.每一行的的数字都是从小到大排序的
            2.每一行的第一个数字都比上一行的末位数字大
    解法思路：
        1.首先确定 target 在矩阵中行的位置：与每一行最后一位对比，如果更大，则往下一行，如果更小，则与行首数字对比；
        2.确定位置后在该行中的一维数组里查询是否存在该值

    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """
    def binary_search(nums, item):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == item:
                return True
            elif nums[mid] > item:
                high = mid - 1
            else:
                low = mid + 1
        return False

    length = len(matrix)
    if length == 0:
        return False
    if len(matrix[0]) == 0:
        return False
    if target < matrix[0][0]:
        return False
    for i in range(length):
        if target <= matrix[i][-1]:
            return binary_search(matrix[i], target)


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    print(search_matrix(matrix, target))
