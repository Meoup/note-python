def smallest_range_2(A, K):
    """
    题目说明：
        Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K,
        and add x to A[i] (only once).
        After this process, we have some array B.
        Return the smallest possible difference between the maximum value of B and the minimum value of B.
    解法：
        因为需要返回的是最小的差值，所以要尽可能地使数组里的元素大小相近，即 大数 -K，小的数 +K，
        所以第一步就是要确定大小，可先采用排序，然后再执行 + or - 的操作
        最后再取最大值和最小值的最小的差值返回

    :param A: List[int]
    :param K: int
    :return: int
    """
    # 排序
    A.sort()
    # 原数组最大值与最小值的差值
    diff = A[-1] - A[0]
    for i in range(len(A)-1):
        diff = min(diff, max(A[-1]-K, A[i]+K)-min(A[0]+K, A[i+1]-K))
    print(diff)
    return diff


if __name__ == '__main__':
    smallest_range_2([1, 3, 9, 2, 6, 3, 5], 3)
