def permute(nums):
    """
    要求：
        给定一个不重复数字元素的数组，返回这些元素的所有可能的排列。
        例：
            Input: [1,2,3]
            Output:
            [
              [1,2,3],
              [1,3,2],
              [2,1,3],
              [2,3,1],
              [3,1,2],
              [3,2,1]
            ]
    解题思路：
        这是一个数学中的排列问题，用数学公式表示就是 A(m,n)。

    :param nums: List[int]
    :return: List[List[int]]
    """
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])  # insert n
        perms = new_perms
    return perms


if __name__ == '__main__':
    print(permute([1, 2, 3]))
