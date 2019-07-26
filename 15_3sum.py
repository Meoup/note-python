def three_sum(nums):
    """
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
    :type nums: List[int]
    :rtype: List[List[int]]

    解题思路：
    一、暴力破解 时间复杂度： O(n^3)
    1、先取第一个元素：a  循环次数i：range(len(nums)-2)
    2、再从剩下的元素中取出第二个元素：b  循环次数j：range(i+1, len(nums)-1)
    3、再从剩下的元素中取出第三个元素：c  循环次数k：range(j+1, len(nums))
    4、进行条件判断：a+b+c==0，如果符合则添加到 结果中
    要考虑去重

    二、优化方案 时间复杂度：O(n^2)
    1、先排序数组，然后针对每个元素
    2、按双指针方法寻找， 一个 小->大， 一个 大->小
    3、获取3个元素的和，对和进行判断

    """
    res = []
    nums.sort()  # 排序从小到大
    length = len(nums)
    # 如果数组中的元素的都是整数或负数 则无解
    if nums[0] > 0 or nums[length - 1] < 0:
        return res
    for i in range(length-2):
        # 取一个元素， 然后给它配一个最小的数 和 一个最大的数 进行判断
        first = i + 1  # 左边的
        last = length - 1  # 最右边的
        # 如果前后相遇了 或者 三个数的符号一致 则退出
        if first >= last or nums[i] * nums[last] > 0:
            break
        # 如果数字相等，则跳过
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 针对第一个数字进行配对
        while first < last:
            result = nums[i] + nums[first] + nums[last]
            # 如果和为0，则添加
            if result == 0:
                res.append([nums[i], nums[first], nums[last]])

            if result <= 0:
                # 如果和小于0，则表示左边的数太小了，需要加大，即右移一位
                first += 1
                while first < last and nums[first] == nums[first - 1]:
                    # 如果右移后的数字跟之前的相等，则继续往右移，直到不相等为止
                    first += 1
            else:
                # 如果和大于0，则表示右边的数太大了，需要减小，即左移一位
                last -= 1
                while first < last and nums[last] == nums[last + 1]:
                    # 如果左移后的数字跟之前的相等，则继续左移，直到不相等为止
                    last -= 1
    print(res)
    return res


if __name__ == '__main__':
    three_sum([0, 8, 0, -8, -1, 2, -1, 0])
