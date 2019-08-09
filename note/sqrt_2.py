def sqrt_2():
    """
    阿里的一道面试题：
        已知sqrt(2)约等于1.414，要求不使用数学库，求sqrt(2)精确到小数点后12位。
    :return: float

    解法：
        使用二分法，已知了sqrt(2)约等于1.414，可在(1.41, 1.42)之间做二分，使得中间值的平方无限接近2
        条件：如果中间值的平方大于2则把上限降低，否则，把下限提高
        当上限与下限的差值小于0.0000000001，则返回中间值
    """
    digit = 0.0000000001
    high = 1.42
    low = 1.41
    mid = 0
    while high-low > digit:
        mid = (high + low) / 2
        if mid*mid > 2:
            high = mid
        else:
            low = mid
    return mid


if __name__ == '__main__':
    print(sqrt_2())
