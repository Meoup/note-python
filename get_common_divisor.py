def get_highest_common_divisor(x, y):
    """
    求两数的最大公约数

    解法a：更相减损法 出自中国古代《九章算法》
        （1）判断两数是否相等，如果相等，则该数本身就是最大公约数；不相等则进入第二步
        （2）用大的数减去小的数，然后比较差值和较小的数，如果相等，则该值就是最大公约数；
        如果不相等，则使用差值和较小的数作为输入，重复步骤（2）
    解法b：欧几里得算法（辗转相除法）
        （1）判断两数a，b是否相等，如果相等，则该数本身就是最大公约数；不相等则进入第二步
        （2）用较大的数a除以较小的数b得到余数c，如果c=0，则b就是最大公约数；否则，将b，c作为输入值，重复步骤（2）

    """
    # 解法a
    # if x == y:
    #     return x
    # elif x > y:
    #     x -= y
    # else:
    #     y -= x
    # return get_highest_common_divisor(x, y)

    # 解法b
    if x == y or x*y == 0:
        res = x if x >= y else y
        return res
    elif x > y:
        x = x % y
    else:
        y = y % x
    return get_highest_common_divisor(x, y)


if __name__ == '__main__':
    print(get_highest_common_divisor(160, 64))
