def single_number(nums):
    """
    要求：
        给定一个非空的整数数组，其中只有一个数不重复，其他数都重复了2次，请找出这个数
        leetcode: 时间复杂度为线性，空间复杂度为O(n)
    解题思路：
        把所有元素和其出现次数以字典记录下来，然后找出次数为1的那个key

    LeetCode 牛逼解法：
        采用异或(异或操作符：^ )思路进行求解：
            由于： a ^ 0 = a; a ^ a = 0
            所以有： a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        在本题中其他元素都重复了2次，所以它们所有的数进行异或操作后等于0， 最后跟不重复的数异或即可返回该数
    :param nums: List[int]
    :return: int
    """
    a = 0
    for i in nums:
        a ^= i
    return a
