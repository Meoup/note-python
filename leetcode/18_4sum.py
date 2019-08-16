def four_sum(nums, target):
    """
    Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
    a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
    Note:
    The solution set must not contain duplicate quadruplets.
    Example:
    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
    A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]

    :param nums:List[int]
    :param target:int
    :return:List[List[int]]

    解题思路：
    该题与3sum、2sum类似
    可以先固定两个数， 在通过双指针寻找剩下的两个数
    本例可以采用递归处理

    """

    # 求元素之和
    def find_sum(new_nums, new_target, n, result, results):
        if len(new_nums) < n or n < 2 or new_nums[0]*n > new_target or new_nums[-1]*n < new_target:
            return
        if n == 2:
            # 此时已经固定好前两个数，只需去匹配后两个数 左右指针
            left, right = 0, len(new_nums) - 1
            while left < right:
                two_sum = new_nums[left] + new_nums[right]
                if two_sum <= new_target:
                    if two_sum == new_target:
                        # 如果等于目标值 则获取
                        results.append(result + [new_nums[left]] + [new_nums[right]])
                    # 如果和比目标值小，则左指针需要右移
                    # 继续移动 匹配下一个指针
                    left += 1
                    while left < right and new_nums[left] == new_nums[left-1]:
                        left += 1
                else:
                    # 如果和比目标值大，则右指针需要左移
                    # 继续移动 匹配下一个指针
                    right -= 1
                    while left < right and new_nums[right] == new_nums[right+1]:
                        right -= 1

        else:
            # 此处是用来固定前两个数
            for i in range(0, len(new_nums)-n+1):
                if i > 0 and new_nums[i] == new_nums[i-1]:
                    # 如果有相等的数字，会跳过，只有不相等的时候才会进入递归
                    continue
                find_sum(new_nums[i+1:], new_target-new_nums[i], n-1, result+[new_nums[i]], results)

    res = []
    nums.sort()
    find_sum(nums, target, 4, [], res)
    print(res)
    return res


if __name__ == '__main__':
    four_sum([-1, 4, 2, 0, -3, 8, 9, 2, -1, 5, 3], 3)
